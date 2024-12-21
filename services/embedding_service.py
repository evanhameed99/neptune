from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingService:
    def __init__(
        self,
        model_name="all-MiniLM-L6-v2",
    ):
        self.model = HuggingFaceEmbeddings(model_name=model_name)

    def embed_query(self, doc):
        return self.model.embed_query(doc)

    def embed_documents(self, docs):
        return self.model.embed_documents(docs)
