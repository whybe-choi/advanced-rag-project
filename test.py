import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import chromadb
from llama_index.core import VectorStoreIndex
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.vector_stores.chroma import ChromaVectorStore

# chroma db를 local로부터 불러오기
chroma_client = chromadb.PersistentClient(path="./chromadb")
chroma_collection = chroma_client.get_or_create_collection("doctor-khu")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
vector_index = VectorStoreIndex.from_vector_store(
    vector_store,
    embed_model="local:./models/bge-m3",
    show_progress=True
    )

# retriever
retriever = VectorIndexRetriever(
    index=vector_index,
    similarity_top_k=5,
)

# retrieval 결과 확인
nodes = retriever.retrieve("머리가 아프고 속이 더부룩해요")
for node in nodes:
    print(node.text)