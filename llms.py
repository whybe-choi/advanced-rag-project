import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from llama_index.core import Settings
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.query_engine import SubQuestionQueryEngine
from llama_index.core.callbacks import CallbackManager, LlamaDebugHandler
from llama_index.llms.cohere import Cohere
from utils import load_from_local, load_prompt

llama_debug = LlamaDebugHandler(print_trace_on_end=True)
callback_manager = CallbackManager([llama_debug])

Settings.callback_manager = callback_manager
Settings.llm = Cohere(temperature=0.1)

# chroma db를 local로부터 불러오기
vector_index = load_from_local(
    persist_path="./chromadb",
    collection_name="doctor-khu"
)

vector_query_engine = vector_index.as_query_engine()

query_engine_tools = [
    QueryEngineTool(
        query_engine=vector_query_engine,
        metadata=ToolMetadata(
            name="sub-query analyzer",
            description="break down a complex question into simpler sub-questions in Korean",
        ),
    ),
]

query_engine = SubQuestionQueryEngine.from_defaults(
    query_engine_tools=query_engine_tools,
    use_async=True,
)

new_prompt_qa = load_prompt("qa_template.txt")
new_prompt_refine = load_prompt("refine_template.txt")

query_engine.update_prompts(
    {
        "response_synthesizer:text_qa_template" : new_prompt_qa,
        "response_synthesizer:refine_template" : new_prompt_refine
    }
)

def get_response(query):
    response = query_engine.query(query)
    return response