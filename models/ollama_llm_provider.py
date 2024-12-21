from langchain_community.llms import Ollama
from langchain.callbacks import AsyncIteratorCallbackHandler
from langchain.callbacks.manager import CallbackManager


class OllamaLLMProvider:
    def __init__(self, model_name, format, base_url):
        self.model_name = model_name
        self.llm = Ollama(
            model=model_name,
            base_url=base_url,
            callback_manager=CallbackManager([AsyncIteratorCallbackHandler()]),
            format=format,
        )

    def getLLM(self):
        return self.llm
