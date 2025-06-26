# 🧠 AI Agent Assistant with FastAPI, LlamaIndex & SerpAPI

This project is an intelligent assistant that combines natural language prompts with structured data querying. It uses LlamaIndex and OpenAI to answer questions about:

- 🌍 World population statistics
- 📄 Country-specific data (e.g., Canada)
- ☕ Coffee shops around the National Gallery of Canada (using SerpAPI)
- 📝 Note-taking (save user-generated text to a file)

A simple `FastAPI` server exposes the agent through a REST API running on `localhost`.

---

## 📦 Features

- 🤖 **ReAct Agent** powered by OpenAI (`gpt-4o` or `gpt-3.5`)
- 🧾 **CSV querying** via `PandasQueryEngine` (world population)
- 📄 **PDF querying** via `LlamaIndex` (Canada data)
- ☕ **Live coffee shop data** from SerpAPI + distance filtering
- 💡 **Note-saving tool**
- 🚀 **FastAPI endpoint** for local interaction: `/query?prompt=...`

---

## 🧰 Tech Stack

| Layer        | Tools Used |
|--------------|------------|
| Backend      | FastAPI, Python |
| LLM Agent    | LlamaIndex, OpenAI |
| Embeddings   | OpenAI Embeddings |
| Data Sources | CSV, PDF, SerpAPI |
| Query Engine | ReActAgent + Pandas |
| Scraping     | SerpAPI |
| Environment  | Python 3.10+ |

---



## Features

- Integration with OpenAI’s `gpt-4o-mini` model, supporting a 128k context window.
- Modular code structure including components like `main.py`, `pdf`.`py`, `prompts.py`, and `note_engine.py`.
- Advanced indexing and querying via `llama-index` and `llama-index-experimental` libraries.

## Installation

### 1. Clone this repository
bash
git clone https://github.com/yourusername/ai-agent-assistant.git
cd ai-agent-assistant

### 2. Create and activate virtual environment
python -m venv env
source env/bin/activate        # macOS/Linux
env\Scripts\activate           # Windows


### 3. Install dependencies
pip install -r requirements.txt


### 4. Create a .env file
OPENAI_API_KEY=sk-...
SERPAPI_API_KEY=your-serpapi-key


## ▶️ Running the App
### 1. Start the FastAPI server
uvicorn app:app --reload

### 2. Access it at
http://localhost:8000/docs

Use the /query endpoint: GET /query?prompt=Find the highest rated coffee shop within 1km


## 📁 Project Structure
.
├── data/
│   ├── Canada.pdf
│   ├── notes.txt
│   └── population.csv
├── env/                   # virtual env (not committed)
├── app.py                 # FastAPI app
├── main.py                # Agent + tools + engine setup
├── pdf.py                 # PDF querying tool
├── coffee_scraper.py      # SerpAPI coffee shop scraper
├── note_engine.py         # Tool to save notes
├── prompts.py             # Prompt templates
├── test.py                # Test file (optional)
├── .env                   # API keys
├── .gitignore
├── README.md              # This file
└── requirements.txt

### ✅ Example Prompts
What is the population of India in 2020?
Find the closest 3 coffee shops
How many people live in Europe?
List coffee shops with rating > 4.5 and distance < 1km
Save note: Remember to try Café Art next week.

### 🧠 Future Ideas
Add Vue.js/React frontend to interact visually
Save query history in a database
Extend to multiple countries and datasets
Add authentication to secure the endpoint

