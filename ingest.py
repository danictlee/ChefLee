import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

def ingest_docs():
    print("Loading the cookbook...")
    loader = PyPDFLoader("PDFs/Asian-Takeout-eCookbook-RecipeTin-Eats.pdf")
    documents = loader.load()
    print(f"Loaded {len(documents)} pages.")
    print("Splitting text into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)
    print(f"    Created {len(chunks)} text chunks (recipes/sections).")

    print("Saving to memory (ChromaDB)...")
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )
    print("Ingestion complete!")
if __name__ == "__main__":
    ingest_docs()
