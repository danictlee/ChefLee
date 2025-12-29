import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

# 2. Initialize the API
app = FastAPI(title="The Chef 🍳")

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.0)

embedding_function = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vector_store = Chroma(persist_directory="chroma_db", embedding_function=embedding_function)

class QuestionRequest(BaseModel):
    query: str

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    print(f"Searching for: {request.query}")
    docs = vector_store.similarity_search(request.query, k=3)
    
    context_text = "\n\n".join([doc.page_content for doc in docs])
    
    prompt = f"""
    You are an expert chef assistant. Answer the question based ONLY on the following context.
    If the answer is not in the context, say "I don't have that recipe."
    
    Context from Cookbook:
    {context_text}
    
    Question: {request.query}
    """

    response = llm.invoke(prompt)
    
    return {"answer": response.content}

@app.get("/")
def read_root():
    return {"message": "The Chef is ready! 👨‍🍳"}