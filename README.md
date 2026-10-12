# GenAI Chunking Strategies

This repository contains a set of Python experiments for different text chunking strategies commonly used in Retrieval-Augmented Generation (RAG), semantic search, and large-language-model pipelines.

The examples are designed to explore how documents can be split into chunks depending on the use case, such as fixed-size token windows, recursive splitting, semantic grouping, hierarchical structure, contextual augmentation, and agent-driven splitting.

## Repository contents

- `fixed_size_chunking.py` — Fixed-size character chunking using `CharacterTextSplitter`.
- `Recursive_Chunking.py` — Recursive splitting with separators such as paragraphs, new lines, spaces, and characters.
- `Semantic_Chunking.py` — Semantic chunking using sentence embeddings and `SemanticChunker`.
- `Document_based_chunking.py` — Markdown-aware chunking using `MarkdownHeaderTextSplitter`.
- `Hierarchical_Chunking.py` — Parent/child document structure for hierarchical retrieval.
- `Contextual_Chunking.py` — Adds a contextual prefix before a chunk to improve retrieval relevance.
- `Agent_Chunking.py` — Uses an LLM to decide chunk boundaries dynamically.
- `proposition_based_chunking.py` — Breaks text into fact-like propositions using an LLM.
- `Late_Chunking.py` — Performs chunking after contextual token embedding generation using late chunking.
- `India's.pdf` — Sample PDF used across many examples.
- `ALL_CHUNKING_STRATEGIES.jpeg` — Visual summary of the chunking strategies in this repo.
- `requirements.txt` — Python dependencies.

## Why chunking matters

Chunking is a key preprocessing step in RAG systems:

- It controls the granularity of retrieved context.
- It helps preserve semantic meaning within each chunk.
- It improves retrieval accuracy and reduces irrelevant context.
- It influences LLM performance, cost, and memory usage.

Different strategies work better for different document types, such as:

- very long documents
- structured markdown or headings
- semantically dense text
- tables and multi-section reports
- retrieval with hierarchical memory

## Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure your environment has access to the required models and API keys:
   - OpenAI key if any script uses `openai` or LLM-based splitting.
   - A local environment file (`.env`) if you use `load_dotenv()`.

## Important note about the sample PDF

Most scripts are hardcoded to load this PDF path:

```python
r"C:\Users\Megha\Desktop\GENAI_CONCEPTS\Chunking_Strategies\India's.pdf"
```

If your project is stored elsewhere, update the file paths in each script to point to the correct PDF location.

Alternatively, keep the PDF in the same repository root and update the loader calls as needed.

## Running the scripts

Each script is runnable directly with Python:

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

Some scripts require:

- a valid OpenAI API key
- internet access for model downloads
- enough system memory for embedding models

## Strategy overview

### 1. Fixed-size chunking
Useful for simple, consistent chunk windows. Best for straightforward retrieval use cases where token limits are strict.

### 2. Recursive chunking
A practical default for documents with mixed structure. It recursively splits by paragraphs, lines, and words while trying to preserve meaningful boundaries.

### 3. Semantic chunking
Groups text based on semantic similarity rather than fixed character counts. This is useful when preserving conceptual continuity matters more than exact size.

### 4. Document-based / Markdown chunking
Uses section headers to split documents into logical parts, which works well for technical documentation, knowledge bases, and structured markdown files.

### 5. Hierarchical chunking
Stores a parent document plus smaller child chunks to balance breadth and detail during retrieval. Common in multi-level indexing systems.

### 6. Contextual chunking
Adds a short prefix that explains the surrounding document context before a chunk, helping downstream retrieval or prompting.

### 7. Agentic chunking
Uses an LLM to decide where chunk boundaries should go. This is flexible but may be more expensive and less deterministic than rule-based methods.

### 8. Proposition-based chunking
Breaks content into atomic facts or statements. This is effective for dense factual content and QA systems that need precise evidence fragments.

### 9. Late chunking
Generates contextual embeddings across the whole document before chunking the token ranges. This can improve chunk representation quality for certain retrieval architectures.

## Project notes

This repository is intended as a learning and experimentation space. It demonstrates multiple chunking paradigms rather than one production-ready pipeline.

For real-world projects, you may want to:

- benchmark each method on your own documents
- tune chunk size and overlap
- add metadata like section titles or source IDs
- validate retrieval performance using evaluation queries
- combine chunking strategies based on document type

## License

This project is provided for educational and experimental purposes. Add a license file if you plan to distribute or reuse the code publicly.
