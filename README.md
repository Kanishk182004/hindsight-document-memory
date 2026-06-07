# Hindsight Document Memory

A simple Python application that demonstrates document ingestion and memory-powered question answering using Hindsight.

The application loads PDF and TXT documents, stores them in a Hindsight memory bank using the Retain API, and answers questions using Hindsight Reflect.

---

## Features

* PDF document ingestion
* TXT document ingestion
* Hindsight Memory Bank integration
* Retain → Reflect workflow
* Multi-provider LLM support
* Source-aware document formatting
* Interactive command-line interface

---

## Project Structure

```text
.
├── data/
│   └── d1.txt
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Prerequisites

Before running this project, make sure you have:

* Python 3.10+
* Hindsight installed
* A Hindsight Memory Bank
* API key for any supported provider (Gemini, OpenAI, Groq, Anthropic, etc.)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Kanishk182004/hindsight-document-memory.git
cd hindsight-document-memory
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root:

```env
HINDSIGHT_BASE_URL=http://localhost:8080
BANK_ID=your_bank_id

HINDSIGHT_API_LLM_PROVIDER=gemini # Change to a provider of your wish if you want to change
HINDSIGHT_API_LLM_API_KEY=your_api_key
HINDSIGHT_API_LLM_MODEL=gemini-2.5-flash # Change to a model of your wish
```

---

## Start the Hindsight API

Before running the application, start the Hindsight API server in a separate terminal.

Terminal 1:

```bash
hindsight-api
```

Leave this terminal running.

---

## Run the Application

Open a second terminal.

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Run the application:

```bash
python main.py
```

---

## Quick Start

Terminal 1:

```bash
hindsight-api
```

Terminal 2:

```bash
python main.py
```

---

## Adding Documents

Place your files inside the `data/` folder.

Example:

```text
data/
├── DBMS_Notes.pdf
├── Operating_System.pdf
└── notes.txt
```

The application automatically detects:

* `.pdf` files
* `.txt` files

and ingests them into the configured memory bank.

---

## Document Storage Format

### TXT Files

```text
FILE: notes.txt
PAGE: 1

Document content...
```

### PDF Files

```text
FILE: DBMS_Notes.pdf
PAGE: 42

Page content...
```

Each PDF page is stored as a separate memory item, making retrieval more precise.

---

## Workflow

### 1. Retain

Documents are loaded and stored in the memory bank.

```python
client.retain(
    bank_id=BANK_ID,
    content=content
)
```

### 2. Reflect

Questions are answered using Hindsight's memory-aware reasoning.

```python
client.reflect(
    bank_id=BANK_ID,
    query=query
)
```

---

## Example

```text
Memory bank ready.
Type 'exit' to quit.

Question: What is normalization?

Answer:

Normalization is a database design technique used to reduce data redundancy and improve data integrity.
```

---

## Supported Providers

Hindsight supports a wide range of LLM providers, including:

* OpenAI
* Anthropic
* Google Gemini
* Vertex AI
* Groq
* Ollama
* Ollama Cloud
* LM Studio
* llama.cpp
* MiniMax
* DeepSeek
* z.ai
* opencode-go
* Volcano Engine
* OpenRouter
* OpenAI Codex
* Claude Code
* AWS Bedrock
* Fireworks AI
* OpenAI-Compatible Endpoints
* LiteLLM (100+ providers)

This project uses Gemini by default, but you can switch providers by updating the environment variables in `.env`.

Example:

```env
HINDSIGHT_API_LLM_PROVIDER=gemini
HINDSIGHT_API_LLM_API_KEY=your_api_key
HINDSIGHT_API_LLM_MODEL=gemini-2.5-flash
```


## Requirements

Example requirements:

```txt
hindsight-client
python-dotenv
pypdf
```

Install with:

```bash
pip install -r requirements.txt
```

---

## Notes

* Keep your API keys inside `.env`
* Never commit `.env` to GitHub
* Add `.env` to `.gitignore`
* Large PDFs are automatically split page-by-page before ingestion
* TXT files are stored as a single document

---

## License

MIT License

---

## Acknowledgements

Built using Hindsight Memory Infrastructure. Compatible with Gemini, OpenAI, Groq, Anthropic, DeepSeek, and other supported providers.
