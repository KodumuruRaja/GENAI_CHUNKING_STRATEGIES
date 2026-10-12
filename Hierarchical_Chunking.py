from litellm import completion

from langchain_community.document_loaders import PyPDFLoader

def pdf_loader(file_path):
    loader = PyPDFLoader(file_path)
    data = loader.load()
    return data

documents = pdf_loader(r"C:\Users\Megha\Desktop\GENAI_CONCEPTS\Chunking_Strategies\India's.pdf")
print(f"Successfully loaded {len(documents)} pages.")

# Conceptual framework natively implemented within Vector Stores (e.g., LlamaIndex / LangChain)
from langchain_core.documents import Document

def create_hierarchical_structures(parent_text: str, child_size: int = 100):
    # The parent document holds the complete text body
    parent_doc = Document(page_content=parent_text, metadata={"doc_id": "parent_001"})
    
    # Generate smaller child slices referencing the parent
    child_chunks = []
    words = parent_text.split()
    for i in range(0, len(words), child_size):
        child_text = " ".join(words[i:i+child_size])
        child_chunks.append(Document(
            page_content=child_text,
            metadata={"parent_id": "parent_001"} # Links back to parent during retrieval
        ))
        
    return parent_doc, child_chunks

parent, children = create_hierarchical_structures(documents[0].page_content)
print(f"Created 1 parent and {len(children)} child nodes.")
