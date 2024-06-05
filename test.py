import chromadb
from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# embedding model load
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-m3")

#기본 embedding model 변경
Settings.embed_model = embed_model

# chroma db를 local로부터 불러오기
chroma_client = chromadb.PersistentClient(path="./chromadb")
chroma_collection = chroma_client.get_or_create_collection("doctor-khu")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
vector_index = VectorStoreIndex.from_vector_store(
    vector_store,
    embed_model=embed_model,
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