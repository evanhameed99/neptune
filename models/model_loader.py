from langchain_community.llms import Ollama
from models.ollama_llm_provider import OllamaLLMProvider
from configuration.config import config


class ModelLoader:
    def __init__(self, model_name, format=""):
        self.model_name = model_name
        self.model = OllamaLLMProvider(
            model_name, format, base_url=config["ollama"]["base_url"]
        )

    def invoke(self, query: str):
        return self.model.llm.invoke(query)

    async def astream(self, query: str):
        async for chunk in self.model.llm.astream(query):
            yield chunk
