# 🧠 AI-Powered Multi-Agent Query Router (LangGraph Project)

This project is an intelligent query-routing system built using [LangGraph](https://python.langchain.com/docs/langgraph/), [LangChain](https://www.langchain.com/), and **Google Gemini**.

It routes user queries to the most relevant knowledge module based on intent:

- 📄 **RAG Module** → For questions related to internal PDF documents (e.g., PLR company reports)
- 🌐 **Web Module** → For up-to-date or real-time information (e.g., current affairs, weather)
- 🤖 **LLM Module** → For general knowledge and reasoning

---

## 📦 Folder Structure

---
```

app/
├── core/ # Shared logic and schema definitions
│ ├── state.py
│ ├── llm_factory.py
│ ├── template_manager.py
│ ├── parser.py
│ └── pydantic_schema.py
├── pipelines/ # Nodes and workflows (RAG, LLM, Web, Validation)
│ ├── llm_agent.py
│ ├── rag_agent.py
│ ├── validation_agent.py
│ ├── web_agent.py
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