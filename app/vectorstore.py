from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import CSVLoader
import os

def build_vectorstore(csv_path: str = "data/faqs.csv", persist_path: str = "vectorstore"):
    # Load documents
    loader = CSVLoader(file_path=csv_path)
    documents = loader.load()

    # HuggingFace sentence transformer
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Build and save FAISS vectorstore
    db = FAISS.from_documents(documents, embeddings)
    db.save_local(persist_path)
    print("✅ Vectorstore created and saved at:", persist_path)

if __name__ == "__main__":
    build_vectorstore()
