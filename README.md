# GenAI Chunking Strategies 🚀

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Community-1C3C5C?style=for-the-badge)
![RAG](https://img.shields.io/badge/RAG-Chunking-FF6B6B?style=for-the-badge)
![LLM](https://img.shields.io/badge/LLM-Experiments-6C63FF?style=for-the-badge)

</div>

A practical collection of Python experiments for exploring different text chunking strategies used in Retrieval-Augmented Generation (RAG), semantic search, and LLM pipeline design.

This repository compares multiple approaches to splitting long documents into meaningful chunks, helping you understand how chunk size, structure, and retrieval strategy affect downstream AI performance.

## Why this repo matters ✨

Chunking is one of the most important preprocessing decisions in a RAG workflow:

- It controls the size and granularity of retrieved context
- It affects semantic relevance and retrieval accuracy
- It impacts the cost and latency of LLM calls
- It influences how well the model understands document structure

## Repository highlights 📌

This project demonstrates several chunking techniques, including:

- Fixed-size chunking
- Recursive chunking
- Semantic chunking
- Markdown/document-aware chunking
- Hierarchical chunking
- Contextual chunking
- Agent-based chunking
- Proposition-based chunking
- Late chunking

## Project structure 🗂️

```text
GENAI_CHUNKING_STRATEGIES/
├── Agent_Chunking.py
├── Contextual_Chunking.py
├── Document_based_chunking.py
├── Hierarchical_Chunking.py
├── India's.pdf
├── Late_Chunking.py
├── README.md
├── Recursive_Chunking.py
├── Semantic_Chunking.py
├── fixed_size_chunking.py
├── proposition_based_chunking.py
├── requirements.txt
├── ALL_CHUNKING_STRATEGIES.jpeg
└── .venv/   # optional local environment
```

## Strategy overview 🧠

### 1) Fixed-size chunking
File: `fixed_size_chunking.py`

Creates chunks of a fixed character size with overlap. Best for simple and fast document splitting when uniform chunk length is required.

### 2) Recursive chunking
File: `Recursive_Chunking.py`

Splits text by natural boundaries like paragraphs, lines, and spaces before falling back to character-level splitting.

### 3) Semantic chunking
File: `Semantic_Chunking.py`

Uses embeddings and semantic similarity to group related text into coherent chunks instead of rigid size boundaries.

### 4) Document / Markdown-aware chunking
File: `Document_based_chunking.py`

Uses document structure and headers to split content by section, which is useful for technical documentation, knowledge bases, and markdown-heavy corpora.

### 5) Hierarchical chunking
File: `Hierarchical_Chunking.py`

Creates a parent-child relationship between large and small chunks so retrieval can balance context breadth and detail.

### 6) Contextual chunking
File: `Contextual_Chunking.py`

Adds short contextual metadata around each chunk to help retrieval and prompting systems keep track of surrounding meaning.

### 7) Agent-based chunking
File: `Agent_Chunking.py`

Uses an LLM to decide chunk boundaries dynamically based on document content and task intent.

### 8) Proposition-based chunking
File: `proposition_based_chunking.py`

Breaks text into atomic statements or facts to support more precise retrieval and fact-grounded QA.

### 9) Late chunking
File: `Late_Chunking.py`

Creates contextual embeddings before splitting token ranges, which can improve representation quality in some retrieval pipelines.

## Setup ⚙️

### 1. Clone the repository

```bash
git clone https://github.com/KodumuruRaja/GENAI_CHUNKING_STRATEGIES.git
cd GENAI_CHUNKING_STRATEGIES
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

- Linux / macOS:

```bash
source .venv/bin/activate
```

- Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Dependencies 📦

```text
langchain_community == 0.4.2
pypdf == 6.20.0
langchain_huggingface == 1.2.3
sentence-transformers == 6.1.0
langchain_experimental == 0.4.2
openai == 3.29.0
einops == 0.8.2
litellm == 1.105.0
```

## Run the scripts ▶️

```bash
python fixed_size_chunking.py
python Recursive_Chunking.py
python Semantic_Chunking.py
python Document_based_chunking.py
python Hierarchical_Chunking.py
python Contextual_Chunking.py
python Agent_Chunking.py
python proposition_based_chunking.py
python Late_Chunking.py
```

If your system uses `python3`, replace `python` accordingly.

## Important note about the PDF 📄

Most scripts currently use a hardcoded Windows path such as:

```python
r"C:\Users\Megha\Desktop\GENAI_CONCEPTS\Chunking_Strategies\India's.pdf"
```

This path is environment-specific and may not exist on your machine. To run the scripts successfully:

- keep `India's.pdf` in the repository root, or
- update each script to use your local PDF path

Example:

```python
pdf_path = "./India's.pdf"
```

## Notes 📝

- This repository is designed for learning and experimentation
- Some scripts may require internet connectivity or model access
- Production systems should benchmark strategies on real data
- Tuning chunk size, overlap, and embedding settings is often essential

## Visual summary 🖼️

The repo also includes a quick visual reference:

- `ALL_CHUNKING_STRATEGIES.jpeg`

## License 📜

This project is shared for educational and experimental purposes. If you plan to reuse or distribute it publicly, adding a formal license file is recommended.

<div align="center">

Made with ❤️ for exploring GenAI chunking strategies.

</div>
