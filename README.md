# 🧠 AI-Powered Multi-Agent Query Router (LangGraph Project)

This project is an intelligent query-routing system built using [LangGraph](https://python.langchain.com/docs/langgraph/), [LangChain](https://www.langchain.com/), and **Google Gemini**.

It routes user queries to the most relevant knowledge module based on intent:

- 📄 **RAG Module** → For questions related to internal PDF documents (e.g., PLR company reports)
- 🌐 **Web Module** → For up-to-date or real-time information (e.g., current affairs, weather)
- 🤖 **LLM Module** → For general knowledge and reasoning

---

## 📦 Folder Structure


```

app/
├── core/ # Shared logic and schema definitions
│ ├── state.py
│ ├── llm_factory.py
│ ├── template_manager.py
│ ├── parser.py
│ └── pydantic_schema.py
├── nodes/ # Nodes and workflows (RAG, LLM, Web, Validation)
│ ├── llm_node.py
│ ├── rag_node.py
│ ├── validation.py
│ ├── web_crawler.py
│ └── rag/ # RAG internals
│ ├── chunking.py
│ ├── chromaDb.py
│ ├── retriever.py
│ ├── embed.py
│ └── load_file.py
├── orchestrator/ # Supervisor LLM
│ └── supervisor.py
├── router/ # Routing logic
│ └── supervisor_router.py
├── workflows/ # LangGraph builder
│ └── graph_builder.py
├── main.py # Entry point to run the workflow
└── data/ # Input PDF files

```

---

## 🚀 Features

✅ LangGraph-based conditional workflow  
✅ Multi-agent routing using Gemini-1.5 Flash  
✅ Pydantic-validated JSON parsing  
✅ PDF ingestion and chunking with LangChain  
✅ MMR-based retrieval using Chroma vector DB  
✅ LLM-powered answer validation with retry logic

---

## 📌 Setup Instructions 
```
pip install -r requirements.txt
```



### Set up your .env file

Create a .env file with the following content:

```
GOOGLE_GEN_API_KEY=your_google_genai_key
```

### Add your PDF

Place the target PDF (e.g., company report) in the data/ folder. Update the file path in main.py if needed.

### Run the app
```
python main.py
```

---

### Sample Query
```
state = {'message': ['What is the profit of PLR in 2025?']}
```

---
### The system will:

Use the Supervisor to classify the query

Route to RAG / WEB / LLM module

Use the Validator to ensure response relevance

Loop back to Supervisor if incomplete
---

### 🧠 Technologies Used
LangGraph

LangChain

Google Gemini 1.5 Flash

HuggingFace Embeddings (BAAI/bge-small-en)

Chroma Vector Store

Tavily Web Search API

Pydantic for parsing and validation


---

### 📌 TODO / Future Improvements

 Add Streamlit or FastAPI frontend

 Integrate better validation with confidence scores

 Add retry logic and timeout handling for LLM calls

 Dockerize the project for production deployment

 Add tests for parser, templates, and routers

