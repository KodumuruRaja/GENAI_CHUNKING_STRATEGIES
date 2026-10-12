from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter

def pdf_loader(file_path):
    loader = PyPDFLoader(file_path)
    data = loader.load()
    return data

documents = pdf_loader(r"C:\Users\Megha\Desktop\GENAI_CONCEPTS\Chunking_Strategies\India's.pdf")
print(f"Successfully loaded {len(documents)} pages.")

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

def chunk_documents_by_markdown(documents):
    text_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

    full_text = "\n".join([doc.page_content for doc in documents])
    
    chunks = text_splitter.split_text(full_text)
    return chunks

chunks = chunk_documents_by_markdown(documents)
print(f"Number of chunks created: {len(chunks)}")


