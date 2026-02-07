# YouTube Semantic Q&A RAG System

<div align="center">

**A high-performance RAG pipeline for indexing, searching, and querying YouTube video transcripts with semantic precision.**

[Overview](https://www.google.com/search?q=%23-overview) • [Features](https://www.google.com/search?q=%23-features) • [Installation](https://www.google.com/search?q=%23-installation) • [Usage](https://www.google.com/search?q=%23-usage) • [Architecture](https://www.google.com/search?q=%23-architecture)

</div>

---

## 📖 Overview

This project is an end-to-end **Retrieval-Augmented Generation (RAG)** system designed to transform unstructured video content into a structured, queryable knowledge base. Built using a modular Python architecture, it processes massive amounts of YouTube transcript data, generates high-dimensional embeddings, and stores them in a serverless vector database.

The system is engineered to solve "needle in a haystack" problems within long-form video content, allowing users to extract specific technical insights without watching hours of footage. It strictly grounds its responses in the provided transcript context to ensure high factual accuracy and includes source citations (YouTube URLs) for every answer.

### 🏆 Key Achievements

* ✅ **Semantic Precision**: Utilizes `text-embedding-3-small` to capture deep contextual meaning, moving beyond simple keyword matching.
* ✅ **Cloud-Scale Retrieval**: Implements **Pinecone Serverless** for low-latency, high-accuracy similarity search.
* ✅ **Source-Backed Generation**: Every response is appended with the specific video title and timestamped URL from which the information was retrieved.
* ✅ **Robust Data Engineering**: Features a batch-upserting logic that handles large datasets efficiently while managing API rate limits.

---

## 🚀 Features

* **Metadata-Rich Ingestion**: Captures video IDs, timestamps, channel info, and URLs alongside text chunks.
* **Advanced LLM Orchestration**: Powered by **GPT-5.2-chat** (Azure OpenAI) for superior reasoning and context synthesis.
* **Serverless Vector Ops**: Uses Pinecone namespaces to isolate data environments (e.g., `youtube-data`).
* **Automated Testing**: Built-in `pytest` suite for validating prompt formatting and end-to-end pipeline integrity.
* **Deterministic Prompting**: Optimized system prompts that force the model to stay within the bounds of the retrieved context.

---

## 🏗 Architecture

### System Pipeline

```text
┌─────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│ YouTube CSV Data│  →   │ Batch Processor  │  →   │ Azure OpenAI     │
│ (Transcripts)   │      │ (100-row chunks) │      │ (Embeddings Gen) │
└─────────────────┘      └──────────────────┘      └────────┬─────────┘
                                                            │
                                                            ↓
┌─────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│ Final Answer    │      │ GPT-5.2-chat     │      │ Pinecone Vector  │
│ + Source Links  │  ←   │ (Answer Synthesis)│  ←   │ Database (Index) │
└─────────────────┘      └──────────────────┘      └──────────────────┘

```

---

## 🛠 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/RAG-Chatbot-For-Youtube_Data.git
cd RAG-Chatbot-For-Youtube_Data

# Install project dependencies
pip install -r requirements.txt

```

### 1. Data Ingestion & Indexing

Load your YouTube transcript CSV and sync it with your Pinecone index. This step handles batching and embedding generation.

```bash
# Set your environment variables first (.env)
python src/ingest_data.py

```

### 2. Semantic Querying (Inference)

Ask technical questions about the video content.

```python
from src.pipeline import rag_pipeline

query = "How to build next-level Q&A with OpenAI?"
answer = rag_pipeline(query)
print(answer)

```

**Example Output:**

> **Answer:** To build next‑level Q&A, you use an **Open Domain Question Answering (ODQA) pipeline**. This involves taking a user query, converting it into a vector, and retrieving the most semantically relevant chunks from a vector database...
> **Sources:**
> * How to build a Q&A AI in Python: [https://youtu.be/w1dMEWm7jBc](https://youtu.be/w1dMEWm7jBc)
> 
> 

### 3. Running Tests

Ensure the logic and integration are functioning correctly.

```bash
pytest tests/

```

---

## 📁 Project Structure

```text
RAG-Chatbot_For-Youtube-Data/
├── src/
│   ├── __init__.py       
│   ├── core_logic.py        
│   ├── ingest_data.py      
│   └── main.py         
├── tests/
│   ├── test_logic.py       
│   └── test_pipeline.py    
├── data/                   
├── requirements.txt       
└── .gitignore              

```

---

## 🛠 Technical Complexity & Design Decisions

1. **Batch-Limited Upserting**: To prevent API timeouts and memory overflows, data is split into batches of 100 before being embedded and upserted.
2. **Metadata Filtering**: We store the full text, title, and URL within the Pinecone metadata, allowing the system to return complete citations without a secondary database lookup.
3. **Strict Context Prompting**: The `prompt_with_context_builder` uses a specific delimiter strategy (`\n\n--\n\n`) to help the LLM distinguish between separate video segments, reducing context blending.
4. **Environment Isolation**: The code utilizes Pinecone namespaces (`youtube-data`), allowing the same index to host multiple datasets (e.g., YouTube transcripts vs. Documentation) without collision.

---

## 👨‍💻 Author

**Yajat Pawar**


* GitHub: [@yajatpawar24-beep](https://github.com/yajatpawar24-beep)
* LinkedIn: [Yajat Pawar](https://www.linkedin.com/in/yajat-pawar-47369337b/)

---

<div align="center">

**Bridging the gap between video content and actionable intelligence.**

[⬆ back to top](https://www.google.com/search?q=%23-youtube-semantic-qa-rag-system)

</div>
