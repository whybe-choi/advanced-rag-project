import chromadb
from llama_index.readers.json import JSONReader
from llama_index.core import VectorStoreIndex, StorageContext, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from sentence_transformers import SentenceTransformer

embed_model_path = "./models/bge-m3"
model = SentenceTransformer("BAAI/bge-m3")
model.save(embed_model_path)

# embedding model load
embed_model = HuggingFaceEmbedding(model_name=embed_model_path)

#기본 embedding model 변경
Settings.embed_model = embed_model

# jsonreader
reader = JSONReader(
    ensure_ascii=False,
    is_jsonl=True
)

# documents load
documents = reader.load_data(input_file="./data/faq_list.jsonl", extra_info={})

# chunking
text_splitter = SentenceSplitter(
    chunk_size=512,
    chunk_overlap=50,
    )
nodes = text_splitter.get_nodes_from_documents(documents)

# chroma db를 local에 저장
chroma_client = chromadb.PersistentClient(path="./chromadb")
chroma_collection = chroma_client.create_collection("doctor-khu")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# vectorstore 
vector_index = VectorStoreIndex.from_documents(
    documents, 
    storage_context=storage_context,
    show_progress=True
    )