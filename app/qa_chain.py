# import os
# from langchain.chains import RetrievalQA
# from langchain_community.vectorstores import FAISS
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_openai import ChatOpenAI  # ✅ ye generic wrapper hai
# from dotenv import load_dotenv
# from langchain_huggingface import HuggingFaceEmbeddings
#
# load_dotenv()
#
# def get_qa_chain():
#     together_api_key = os.getenv("TOGETHER_API_KEY")
#     if not together_api_key:
#         raise ValueError("⚠️ TOGETHER_API_KEY missing in .env file")
#
#     embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
#     db = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)
#     retriever = db.as_retriever()
#
#     # ✅ Use Together.ai by setting OpenAI base + key
#     os.environ["OPENAI_API_BASE"] = "https://api.together.xyz/v1"
#     os.environ["OPENAI_API_KEY"] = together_api_key
#
#     llm = ChatOpenAI(
#         model_name="mistralai/Mixtral-8x7B-Instruct-v0.1",  # ✅ Free + Serverless
#         # openai_api_base="https://api.together.xyz/v1",
#         temperature=0.5,
#         max_tokens=512
#     )
#
#     return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
import os
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def get_qa_chain():
    together_api_key = os.getenv("TOGETHER_API_KEY")
    if not together_api_key:
        raise ValueError("⚠️ TOGETHER_API_KEY missing in .env file")

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)
    retriever = db.as_retriever()

    os.environ["OPENAI_API_BASE"] = "https://api.together.xyz/v1"
    os.environ["OPENAI_API_KEY"] = together_api_key

    llm = ChatOpenAI(
        model_name="mistralai/Mixtral-8x7B-Instruct-v0.1",  # ✅ Free Together model
        temperature=0.5,
        max_tokens=512
    )

    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=False)
