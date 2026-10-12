# GenAI Chunking Strategies

This repository contains Python experiments and reference implementations for different document chunking techniques used in Retrieval-Augmented Generation (RAG), semantic search, and LLM-powered pipelines.

The goal is to explore how text should be split into chunks depending on the use case, model, and retrieval objective. Each script demonstrates a different strategy and helps compare trade-offs in granularity, semantic preservation, retrieval quality, and cost.

## Repository overview

This project includes multiple chunking approaches:

- Fixed-size chunking
- Recursive chunking
- Semantic chunking
- Document/Markdown-aware chunking
- Hierarchical chunking
- Contextual chunking
- Agent-based chunking
- Proposition-based chunking
- Late chunking

It also includes a sample PDF (`India's.pdf`) to run the examples end-to-end.

## Project structure

```text
.
├── Agent_Chunking.py
├── Contextual_Chunking.py
├── Document_based_chunking.py
├── Hierarchical_Chunking.py
├── India\'s.pdf
├── Late_Chunking.py
├── README.md
├── Recursive_Chunking.py
├── Semantic_Chunking.py
├── fixed_size_chunking.py
├── proposition_based_chunking.py
├── requirements.txt
├── ALL_CHUNKING_STRATEGIES.jpeg
└── .venv/   (optional, created locally)
```

## Chunking strategies in this repo

### 1. Fixed-size chunking
File: `fixed_size_chunking.py`

Splits documents into chunks of a fixed number of characters or tokens with a configurable overlap. This is useful for simple retrieval systems and strict context windows.

### 2. Recursive chunking
File: `Recursive_Chunking.py`

Recursively splits text using meaningful boundaries like paragraphs, new lines, and spaces before falling back to character-based splits. This is a strong default for mixed-format documents.

### 3. Semantic chunking
File: `Semantic_Chunking.py`

Uses embeddings and similarity-based logic to group text into semantically coherent chunks. This is especially helpful when preserving topic continuity matters more than fixed length.

### 4. Document/Markdown-based chunking
File: `Document_based_chunking.py`

Uses headers and document structure to split content based on sections or markdown hierarchy. This works well for docs, knowledge bases, and technical writing.

### 5. Hierarchical chunking
File: `Hierarchical_Chunking.py`

Creates parent-child chunk relationships so retrieval can access both broad context and more detailed nested chunks.

### 6. Contextual chunking
File: `Contextual_Chunking.py`

Adds surrounding context to each chunk before embedding or retrieval, which can improve relevance and downstream prompt quality.

### 7. Agent-based chunking
File: `Agent_Chunking.py`

Uses an LLM to decide where chunk boundaries should be placed dynamically based on content semantics and context.

### 8. Proposition-based chunking
File: `proposition_based_chunking.py`

Breaks text into atomic facts or propositions so retrieval can surface precise, question-relevant evidence.

### 9. Late chunking
File: `Late_Chunking.py`

Creates contextual embeddings across the whole document before splitting token ranges, which can improve retrieval quality for some architectures.

## Why chunking matters

Chunking is a crucial preprocessing step in RAG systems because it affects:

- retrieval quality
- context relevance
- cost and latency
- LLM reasoning quality
- memory efficiency

A poor chunking strategy can reduce retrieval accuracy even when the model itself is strong.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/KodumuruRaja/GENAI_CHUNKING_STRATEGIES.git
cd GENAI_CHUNKING_STRATEGIES
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Requirements

The project uses the following Python packages:

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

## Run the scripts

Each script can be executed directly with Python:

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

If you are using Python 3 on some systems, replace `python` with `python3`.

## Important note about the sample PDF

Most scripts currently reference the PDF through a hardcoded Windows-style path like:

```python
r"C:\Users\Megha\Desktop\GENAI_CONCEPTS\Chunking_Strategies\India's.pdf"
```

This path is environment-specific and may not exist on your machine. To run the scripts successfully:

- place the `India's.pdf` file in the project root, or
- update the file path in each script to match your local environment

Example:

```python
pdf_path = "./India's.pdf"
```

## Notes

- This repository is designed for learning and experimentation.
- Some scripts may require internet access or access to an LLM API depending on the implementation.
- For production use, you should benchmark and compare chunking strategies on your own documents and retrieval tasks.
- You may want to tune chunk size, overlap, and embedding settings based on your dataset.

## License

This project is provided for educational and experimental purposes. If you plan to share or reuse it publicly, consider adding an explicit license file.

## Visual overview

The repository includes a visual summary image:

- `ALL_CHUNKING_STRATEGIES.jpeg`

This file provides a quick comparison of the strategies implemented in this project.
