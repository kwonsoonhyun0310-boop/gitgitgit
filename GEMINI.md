# LLM Agent Workspace

This project is a comprehensive workspace for exploring, learning, and building Large Language Model (LLM) agents. It demonstrates the integration of modern LLM frameworks and tools, progressing from basic components to a fully functional RAG-based chatbot.

## Project Overview

The repository is structured as a series of educational Jupyter Notebooks (`.ipynb`) and supporting Python scripts. It focuses on the **LangChain** ecosystem and integrates with observability and prompt management tools like **LangSmith** and **Langfuse**.

**Key Technologies:**
*   **Language:** Python 3.12+
*   **Framework:** LangChain (and LangChain OpenAI)
*   **Vector Database:** ChromaDB (for RAG)
*   **Observability:** LangSmith, Langfuse
*   **UI:** Gradio (for Chat Interface)
*   **Package Management:** `uv`
*   **Protocols:** MCP (Model Context Protocol)

## Directory Structure

The project uses a numbered prefix system to guide the learning path:

*   **Notebooks:**
    *   `LLM_001_Langchain_Components.ipynb`: Introduction to LangChain basics.
    *   `LLM_002_LangSmith_LCEL.ipynb`: Using LangChain Expression Language (LCEL) and tracing with LangSmith.
    *   `LLM_003_Langfuse_Prompt_Management.ipynb`: Managing prompts and monitoring with Langfuse.
    *   `LLM_004_LangChain_PDF_RAG.ipynb`: Implementing Retrieval-Augmented Generation (RAG) with PDFs.
    *   `LLM_005_Prompt_Engineering_Fewshot.ipynb`: Advanced prompting techniques (Few-shot).
    *   `LLM_006_Prompt_Engineering_CoT.ipynb`: Chain-of-Thought prompting.
    *   `LLM_007_Housing_FAQ_Bot.ipynb`: Capstone project - a Housing FAQ Chatbot using RAG and Gradio.

*   **Directories:**
    *   `data/`: Contains source documents for RAG (e.g., `housing_faq.txt`, `labor_law.pdf`, `personal_info_law.pdf`) and formatted JSON datasets.
    *   `chroma_db/`: Persisted SQLite database for ChromaDB vector embeddings.
    *   `005_llm_rag/`: Additional or alternative RAG implementation notebooks.
    *   `.venv/`: Python virtual environment.

*   **Configuration:**
    *   `pyproject.toml` & `uv.lock`: Project dependencies and lockfile.
    *   `mcp_servers.json`: Configuration for Model Context Protocol servers (currently `docs-langchain`).
    *   `main.py`: Simple entry point (currently a placeholder).

## Getting Started

### Prerequisites

*   Python 3.12 or higher
*   `uv` (fast Python package installer and resolver)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd 004_llm_agent
    ```

2.  **Install dependencies:**
    This project uses `uv` for dependency management.
    ```bash
    uv sync
    ```
    Alternatively, using pip with the generated requirements (if available) or `pyproject.toml`:
    ```bash
    pip install .
    ```

3.  **Environment Setup:**
    Create a `.env` file in the root directory to store your API keys. You will likely need:
    ```ini
    OPENAI_API_KEY=sk-...
    LANGCHAIN_API_KEY=...
    LANGCHAIN_TRACING_V2=true
    LANGCHAIN_PROJECT=...
    LANGFUSE_PUBLIC_KEY=...
    LANGFUSE_SECRET_KEY=...
    LANGFUSE_HOST=...
    ```

### Usage

**Running Notebooks:**
The primary way to interact with this project is through the Jupyter Notebooks.
```bash
# Activate the virtual environment if not using uv directly
source .venv/bin/activate
jupyter notebook
```
Open the notebooks in order (001 -> 007) to follow the curriculum.

**Running the Housing FAQ Bot:**
The `LLM_007_Housing_FAQ_Bot.ipynb` notebook contains the code to launch a Gradio interface. Run all cells in this notebook to start the chatbot server locally.

**MCP Server:**
The `mcp_servers.json` file configures the MCP endpoints. This can be used with MCP-compatible clients (like certain IDEs or AI assistants) to provide context from external documentation (e.g., LangChain docs).
