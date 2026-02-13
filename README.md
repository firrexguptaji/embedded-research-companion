# 🧠 Embedded Research Companion

A fully containerized, multi-agent AI research assistant that analyzes research papers, retrieves contextual knowledge (Wikipedia + document memory), and generates structured responses using local LLMs.

**Built with:**

- **LangGraph** (multi-agent orchestration)
- **LangChain**
- **Ollama** (local LLM + embeddings)
- **Chroma** (vector database)
- **Gradio** (web UI)
- **Docker** (fully containerized stack)

## 🚀 What This Project Does

This system allows you to:

- 📄 Upload research papers (PDF)
- 🧠 Store document chunks in a vector database
- 🔍 Retrieve relevant context via semantic search
- 🌐 Pull knowledge from Wikipedia
- 🤖 Generate intelligent responses using a local LLM
- 🧩 Orchestrate multiple agents via LangGraph
- 🐳 Run everything with a single Docker command
- 💻 Install it like a desktop app (Windows installer included)

## 🏗 System Architecture

```
User
  ↓
Gradio UI
  ↓
LangGraph Multi-Agent Engine
  ├── Planner Agent
  ├── Router Agent
  ├── Document Agent (RAG)
  ├── Wikipedia Agent
  ├── Memory Agent
  └── Aggregator Agent
  ↓
Ollama (mistral + nomic-embed-text)
  ↓
Chroma Vector Database
```

## 🧠 Multi-Agent Design

| Agent | Responsibility |
|-------|----------------|
| **Planner** | Understands user intent |
| **Router** | Routes to correct agent(s) |
| **Document Agent** | Retrieves relevant document chunks |
| **Wikipedia Agent** | Fetches external knowledge |
| **Memory Agent** | Maintains session context |
| **Aggregator** | Synthesizes final response |

*This is not a simple RAG app — it is a modular agent system.*

## 📦 Tech Stack

- Python 3.11
- LangChain
- LangGraph
- Ollama
- ChromaDB
- Gradio
- Docker & Docker Compose
- Inno Setup (Windows installer)

## ⚡ Quick Start (Docker Only)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/firrexguptaji/embedded-research-companion
cd embedded-research-companion
```

### 2️⃣ Start Everything

```bash
docker compose up
```

**First run:**
- Ollama auto-pulls models
- Containers build
- Gradio launches

**Open:** http://localhost:7860

## 🖥 Windows Installer Version

For non-technical users:

1. Run `EmbeddedResearchInstaller.exe`
2. Choose installation directory
3. Installer runs first-time setup
4. Browser opens automatically
5. Future launches use Start Menu shortcut

**Scripts included:**

- `setup.ps1` → First-time initialization
- `run.ps1` → Normal launch
- `stop.ps1` → Stop containers
- `reset.ps1` → Factory reset

## 🐳 Docker Architecture

Two services:

### **ollama**
- Runs local LLM server
- Auto-pulls:
  - `mistral`
  - `nomic-embed-text`
- Persistent model storage

### **research-companion**
- Gradio UI
- LangGraph engine
- Chroma vector DB
- Connects internally to Ollama
- Fully containerized. No host networking hacks.

## 📂 Project Structure

```
embedded-research-companion/
│
├── app/
│   ├── agents/
│   ├── graph/
│   ├── memory/
│   └── engine.py
│
├── ui/
│   └── gradio_app.py
│
├── config/
│   └── llm.py
│
├── docker-compose.yml
├── Dockerfile
├── setup.ps1
├── run.ps1
├── stop.ps1
├── reset.ps1
└── installer.iss
```

## 🧪 Features

- ✅ Session-based memory
- ✅ PDF ingestion + chunking
- ✅ Persistent vector storage
- ✅ Multi-agent orchestration
- ✅ Wikipedia integration
- ✅ Local LLM inference
- ✅ Dockerized deployment
- ✅ Windows installer packaging
- ✅ Clean separation of setup/run/reset lifecycle

## 🔄 Script Lifecycle

| Script | Purpose |
|--------|---------|
| `setup.ps1` | First-time build + launch |
| `run.ps1` | Start system normally |
| `stop.ps1` | Stop containers |
| `reset.ps1` | Delete containers & volumes |

*Installer runs `setup.ps1`. Shortcut runs `run.ps1`.*

## ⚙ Requirements

- Docker Desktop
- 16GB+ RAM recommended
- GPU optional (CPU works)
- Windows 10/11 (for installer)

## 🧠 Models Used

- **mistral** → generation
- **nomic-embed-text** → embeddings

Both served via Ollama.

## 🔐 Local & Private

- ✅ No external API calls required
- ✅ Fully local inference
- ✅ No OpenAI dependency
- ✅ No cloud data exposure

## 🛠 Development Mode

To rebuild manually:

```bash
docker compose down -v
docker compose build --no-cache
docker compose up
```

## 🚀 Future Improvements

- 🔄 GPU acceleration in Docker
- 📊 Agent performance tracing
- 🎯 Tool confidence scoring
- 📑 Citation extraction
- 🏗 Structured output planning
- 🖥 Background system tray launcher
- ☁ Cloud deployment option
- 🔄 Auto-update mechanism

## 📜 License

MIT License (or choose your preferred license)

## 👤 Author

Built as a modular, production-ready AI research assistant system.

## 🎯 Summary

This project demonstrates:

- ✨ Multi-agent orchestration
- 🔍 Retrieval-augmented generation
- 🤖 Local LLM infrastructure
- 🐳 Containerized AI stack
- 💻 Desktop-style distribution
- ⚙️ Real product engineering discipline
