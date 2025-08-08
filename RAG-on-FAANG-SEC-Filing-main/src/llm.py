import os
from langchain_community.llms import Ollama

def build_llm():
    model_name = "llama3"
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")  # fallback

    return Ollama(model=model_name, base_url=base_url)