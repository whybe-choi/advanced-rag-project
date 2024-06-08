from llama_index.core.retrievers import VectorIndexRetriever
from utils import load_from_local

# chroma db를 local로부터 불러오기
vector_index = load_from_local(
    persist_path="./chromadb",
    collection_name="doctor-khu"
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