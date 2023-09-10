from langchain.embeddings.openai import OpenAIEmbeddings
import faiss
from langchain.vectorstores import FAISS
from langchain.docstore import InMemoryDocstore


class FaissVector:
    def __init__(self):
        # OpenAI Embedding 模型
        embeddings_model = OpenAIEmbeddings() 

        # OpenAI Embedding 向量维数
        embedding_size = 1536

        # 使用 Faiss 的 IndexFlatL2 索引
        index = faiss.IndexFlatL2(embedding_size)

        # 实例化 Faiss 向量数据库
        self.vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})

       # return vectorstore