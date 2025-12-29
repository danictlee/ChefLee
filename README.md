# 🍜 Chef Lee's Digital Kitchen

**A RAG-based AI Recipe Assistant built with Python.**

## 🍽️ About The Project
Chef Lee is a digital sous-chef that helps you decide what to cook. It uses **Retrieval-Augmented Generation (RAG)** to read a real cookbook (*Asian Takeout* by RecipeTin Eats) and answer questions based *only* on the recipes in that book.

If you ask for a dish, it searches the PDF, finds the best matches, and uses Google Gemini to explain the recipe to you.

## 🥘 Tech Stack (The Ingredients)
* **Brain:** Google Gemini 2.0 Flash (via LangChain)
* **Memory:** ChromaDB (Vector Database)
* **API:** FastAPI
* **Frontend:** Streamlit
* **Language:** Python 3.12+

## 🔪 Setup Instructions

### 1. Clone & Install

```bash
# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file in the root folder and add your Google API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

### 3. Prep the Kitchen (Ingestion)

Before running the app, you need to "teach" the AI the cookbook:

```bash
python ingest.py
```

This will create a `chroma_db` folder with the vectorized recipes.

## 👨‍🍳 How to Run

### 1. Start the API (The Kitchen)

```bash
uvicorn main:app --reload
```

### 2. Start the Frontend (The Menu)

Open a new terminal and run:

```bash
streamlit run frontend.py
```

## 📸 Usage

Type in what ingredients you have (e.g., "I have shrimp and rice") and Chef Lee will suggest a recipe from the knowledge base!