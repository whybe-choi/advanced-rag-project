import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import chromadb
import yaml
from llama_index.core import VectorStoreIndex, PromptTemplate, Settings
from llama_index.vector_stores.chroma import ChromaVectorStore

Settings.embed_model = "local:./models/bge-m3"

def load_from_local(persist_path: str, collection_name: str) -> VectorStoreIndex:
    """Load Vector Index from local"""

    chroma_client = chromadb.PersistentClient(path=persist_path)
    chroma_collection = chroma_client.get_or_create_collection(collection_name)
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    vector_index = VectorStoreIndex.from_vector_store(
        vector_store,
        show_progress=True,
        use_async=True,
    )

    return vector_index

def load_prompt(template_name: str) -> PromptTemplate:
    """Load prompt template from local"""
    template_path = f"./templates/{template_name}"

    with open(template_path, "r") as template:
        template = template.read()
        prompt = PromptTemplate(template)

    return prompt
