import json
import os
from typing import AsyncGenerator, List
from configuration.config import config
from services import EmbeddingService
from langchain_redis import RedisChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from templates.default_prompt_template import default_prompt_template
from sentence_transformers.util import cos_sim


class CompletionService:
    def __init__(self, session_id: str, model):
        self.session_id = session_id
        self.model = model
        self.splits_dir = config["dirs"]["splits_dir"]
        self.embedding_service = EmbeddingService()

    async def process_completion(self, prompt: str) -> AsyncGenerator[str, None]:

        # Step 2: Load document splits
        chunks = self._load_document_splits()

        # Step 3: Embed user's prompt
        prompt_embedding = self.embedding_service.embed_query(prompt)

        # Step 4: Embed document chunks
        chunk_contents = [chunk["content"] for chunk in chunks]
        splits_embeddings = [
            self.embedding_service.embed_query(content) for content in chunk_contents
        ]

        # Step 5: Find the most relevant document chunk
        best_match_chunk = self._get_most_relevant_chunk(
            prompt_embedding, chunk_contents, splits_embeddings
        )

        # Step 6: Initialize LLM-Prompt Chain
        chain = default_prompt_template | self.model.model.llm

        # Step 7: Initialize chain-history Chain
        chat_history_chain = RunnableWithMessageHistory(
            chain,
            self.get_chat_history,
            history_messages_key="history",
            input_messages_key="input",
        )

        # Step 8: Invoke model and yield chunks
        async for chunk in chat_history_chain.astream(
            input={"input": prompt, "context": best_match_chunk},
            config={"configurable": {"session_id": self.session_id}},
        ):
            yield f"data: {chunk} \n\n"

    def get_chat_history(self) -> BaseChatMessageHistory:
        """Fetches chat history from Redis."""
        return RedisChatMessageHistory(
            session_id=self.session_id,
            redis_url=f"redis://{config['redis']['host']}:{config['redis']['port']}",
        )

    def _load_document_splits(self) -> List[dict]:
        """Loads and parses document splits for the current session."""
        file_path = os.path.join(self.splits_dir, f"{self.session_id}.json")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found for session_id: {self.session_id}")

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def _get_most_relevant_chunk(
        self,
        prompt_embedding: List[float],
        chunk_contents: List[str],
        splits_embeddings: List[List[float]],
    ) -> str:
        """Finds the most relevant document chunk based on cosine similarity."""
        similarities = cos_sim(prompt_embedding, splits_embeddings).squeeze(0).tolist()
        max_index = similarities.index(max(similarities))
        return chunk_contents[max_index]
