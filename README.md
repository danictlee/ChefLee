# ChefLee 🍳

An intelligent recipe assistant powered by AI that uses semantic search to help you discover and cook amazing Asian recipes.

## 🎯 About

ChefLee is an application that combines PDF processing, vector embeddings, and semantic search to create an AI-driven recipe discovery experience. It processes recipe books in PDF format and allows you to find recipes using natural language.

## 🚀 Features

- **PDF Processing**: Extract recipes from PDF documents
- **Semantic Search**: Find recipes using natural language descriptions
- **Vector Database**: Uses Chroma DB for efficient embedding storage
- **User-Friendly Interface**: Intuitive frontend for exploring recipes
- **AI-Powered Responses**: Google Gemini integration for intelligent recipe assistance

## 📁 Project Structure

```
ChefLee/
├── main.py                                          # FastAPI application entry point
├── frontend.py                                      # Streamlit user interface
├── ingest.py                                        # Script to ingest and process PDFs
├── requirements.txt                                 # Project dependencies
├── .env                                             # Environment variables (DO NOT COMMIT)
├── .gitignore                                       # Git configuration
├── chroma_db/                                       # Vector database storage
│   ├── chroma.sqlite3                              # Embeddings storage
│   └── [uuid]/                                      # Data collections
├── PDFs/                                            # Recipe PDF folder
│   └── Asian-Takeout-eCookbook-RecipeTin-Eats.pdf
└── __pycache__/                                     # Python cache
```

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/danictlee/ChefLee.git
   cd ChefLee
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root with:
   ```env
   GOOGLE_API_KEY=your_google_api_key
   ```

   > **Important**: The `.env` file is included in `.gitignore` and will NOT be uploaded to GitHub.

## ⚙️ Configuration

### Environment Variables

The following environment variable is required:

| Variable | Description |
|----------|-------------|
| `GOOGLE_API_KEY` | Your Google Gemini API key for AI-powered recipe assistance |

Obtain your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

## 🏃 Usage

### 1. Ingest Recipes (Process PDFs)

First, place your recipe PDF files in the `PDFs/` folder, then run:

```bash
python ingest.py
```

This will:
- Extract text from PDF files
- Create vector embeddings
- Store recipes in Chroma DB for semantic search

### 2. Run the API Server

Start the FastAPI backend:

```bash
python main.py
```

The API will be available at `http://localhost:8000`

### 3. Launch the Frontend

In another terminal, start the Streamlit interface:

```bash
streamlit run frontend.py
```

The application will open in your default browser at `http://localhost:8501`

## 🗄️ Database

ChefLee uses **Chroma DB** for storing and retrieving vector embeddings of recipes. Data is persisted in `chroma.sqlite3` within the `chroma_db/` directory.

- **Embeddings Model**: Uses sentence transformers for semantic understanding
- **Storage**: Lightweight SQLite-based persistence
- **Collections**: Organized by recipe categories for efficient retrieval

## 📚 Recipe Content

Currently processing the **"Asian Takeout e-Cookbook"** with 99+ pages featuring:

- **Stir Fries**: Beef and Broccoli, Kung Pao Chicken, etc.
- **Main Courses**: Chinese BBQ Pork, Thai Curries, etc.
- **Noodles and Rice**: Various Asian noodle dishes
- **Soups and Salads**: Traditional Asian soups and fresh salads
- **Appetizers**: Thai Fish Cakes, Spring Rolls, etc.

## 🔧 Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | FastAPI + LangChain |
| **Frontend** | Streamlit |
| **AI Models** | Google Gemini 2.0 Flash |
| **Vector Database** | Chroma DB |
| **Language** | Python 3.x |
| **Environment** | Docker (Ubuntu 24.04.3 LTS) |

## 👨‍💻 Author

- **Daniel Lee** - [GitHub Profile](https://github.com/danictlee)
- **Repository**: [ChefLee](https://github.com/danictlee/ChefLee)