# RAG Pipeline from Almost Scratch

> **A learning and tinkering repo for Retrieval-Augmented Generation (RAG) pipeline with deployment capabilities in the future**

## Overview

This repository implements a comprehensive RAG pipeline built from almost scratch, development to production. The system combines intelligent document processing, vector search, and advanced reasoning capabilities using DeepSeek's state-of-the-art LLM.

### Current State

- **📄 PDF Processing**: Extract text from PDFs and split into chunks using PyMuPDF + LangChain
- **🔍 Vector Database**: Weaviate setup with Docker Compose for local development
- **🤖 Embedding Model**: SentenceTransformers with multilingual support (Vietnamese/English)
- **🧠 LLM Integration**: DeepSeek R1 reasoning model via OpenRouter API
- **🔄 RAG Pipeline**: Complete retrieval → context → generation workflow

### Roadmap to Production

This project is designed to evolve into a full-scale production system with:

```
Development & Research  → Staging → Production
     ↓                      ↓         ↓
  Local Dev             → Cloud     → Enterprise
  Notebook              → Frontend  → Full Stack
  Manual                → CI/CD     → Automated
```

*Note: This is an experimental project. Features will be added incrementally based on learning and exploration.*

## Architecture

### Current Architecture (v1.0)
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   PDF Files     │──→ │   Text Chunks   │──→ │   Weaviate DB   │
│   (test-pdf/)   │    │   (Processed)   │    │   (Docker)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                        │
┌─────────────────┐    ┌─────────────────┐              │
│   User Query    │──→ │   Vector Search │←─────────────┘
│   (Notebook)    │    │   (Similarity)  │
└─────────────────┘    └─────────────────┘
                                │
                                |
                                ↓
┌─────────────────┐    ┌─────────────────┐
│   Final Answer  │←── │   DeepSeek R1   │
│   (Streamed)    │    │   (OpenRouter)  │
└─────────────────┘    └─────────────────┘
```

### Planned Production Architecture
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   API Gateway   │    │   Load Balancer │
│   (Next.js)     │──→ │   (Kong/Nginx)  │──→ │   (ALB/ELB)     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                        │
┌─────────────────┐    ┌─────────────────┐              │
│   Kubernetes    │    │   Microservices │←─────────────┘
│   Cluster       │──→ │   (FastAPI)     │
└─────────────────┘    └─────────────────┘
                                │
                                |
                                ↓
┌─────────────────┐    ┌─────────────────┐
│   Monitoring    │←── │   Vector DB     │
│                 │    │   (Weaviate)    │
└─────────────────┘    └─────────────────┘
```

## Quick Start

### Prerequisites
- Python 3.8+
- Docker & Docker Compose
- OpenRouter API key (for DeepSeek)

### 1. Clone & Setup
```bash
git clone https://github.com/yourusername/RAG-pipeline.git
cd RAG-pipeline

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Start Vector Database
```bash
# Start Weaviate with Docker
docker-compose up -d

# Verify Weaviate is running
curl http://localhost:8080/v1/meta
```

### 3. Configure Environment
```bash
# Copy environment template
cp .env.example .env

# Edit .env with your API keys
# OPENROUTER_DEEPSEEK_KEY=your_key_here
```

### 4. Testing the Pipeline (at the moment, manual)
```bash
# Open Jupyter notebook
jupyter notebook testing.ipynb

# Follow the notebook cells to:
# 1. Install dependencies
# 2. Connect to Weaviate
# 3. Process PDF documents
# 4. Test the RAG pipeline
```
Put your PDF files in the `test-pdf/` directory and change the queries in the notebook for more suitable tests.

## Project Structure

```
RAG-pipeline/
├── 📄 README.md                 # Overview
├── 🐳 docker-compose.yml        # Local development setup
├── 📋 requirements.txt          # Python dependencies
├── 🔧 main.py                   # FastAPI server (basic)
├── 📊 testing.ipynb             # Interactive pipeline testing
├── 🔒 .env.example              # Environment template
├── 📁 test-pdf/                 # PDF documents directory
└── 📁 json/                     # Processed document storage
```

## Core Components

### 1. Document Processing Pipeline
```python
# PDF → Text → Chunks → Embeddings → Vector Store
pdf_to_raw_doc() → split_doc() → embed() → import_texts_and_embeds_to_db()
```

### 2. RAG Query System
```python
# Query → Retrieval → Context → LLM → Response
query_with_rag() → vector_search → context_retrieval → deepseek_generation
```

### 3. Utility Functions
```python
# Document conversion and storage
docs_to_json() → save_to_json() → json_to_docs()
docs_to_strings() → clear_document_collection()
```

## Future Plans

### Completed
- [x] Basic RAG pipeline in Jupyter notebook
- [x] Weaviate vector database setup
- [x] PDF document processing
- [x] DeepSeek LLM integration
- [x] Vietnamese/English multilingual support

### Next Steps
- [ ] Add agent to handle complex queries and re-retrieval
- [ ] Integrate query calling with FastAPI
- [ ] **Web Interface**: Simple frontend for easier interaction
- [ ] **CI/CD**: GitHub Actions for automated testing and deployment
- [ ] **Cloud Deployment**: AWS services (EKS, S3, etc.)
- [ ] **Monitoring**: Basic observability with Prometheus/Grafana
- [ ] **Kubernetes**: Container orchestration for scaling

## Technology Stack

### Current Stack
| Component | Technology | Purpose |
|-----------|------------|---------|
| **Language** | Python 3.8+ | Core development |
| **Vector DB** | Weaviate | Semantic search |
| **LLM** | DeepSeek R1 | Text generation |
| **Embeddings** | SentenceTransformers | Text vectorization |
| **Processing** | PyMuPDF, LangChain | Document handling |
| **Deployment** | Docker Compose | Local development |

### Planned Production Stack
| Component | Technology | Purpose |
|-----------|------------|---------|
| **Frontend** | Next.js | User interface |
| **Backend** | FastAPI | REST API |
| **Container** | Docker + Kubernetes | Orchestration |
| **Cloud** | AWS EKS | Managed Kubernetes |
| **Monitoring** | Prometheus + Grafana | Observability |
| **CI/CD** | GitHub Actions + Jenkins | Automation |

   