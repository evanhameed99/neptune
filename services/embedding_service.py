from langchain_huggingface import HuggingFaceEmbeddings
from configuration.config import config


class EmbeddingService:
    def __init__(
        self,
        model_name=config["hugging_face_embedding_model_name"],
    ):
        self.model = HuggingFaceEmbeddings(model_name=model_name)

    def embed_query(self, doc):
        return self.model.embed_query(doc)

    def embed_documents(self, docs):
        return self.model.embed_documents(docs)
