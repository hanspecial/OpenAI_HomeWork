
from langchain_experimental.autonomous_agents import AutoGPT
from langchain.chat_models import ChatOpenAI
from faiss_vector import FaissVector

class AutoAgent:
    def __init__(self, tools, vectorstore, verbose: bool = True):
        self.agent = AutoGPT.from_llm_and_tools(
        ai_name="Jarvis",
        ai_role="Assistant",
        tools= tools,
        llm=ChatOpenAI(temperature=0),
        memory= vectorstore.as_retriever(), # 实例化 Faiss 的 VectorStoreRetriever
        )