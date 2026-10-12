from litellm import completion

from langchain_community.document_loaders import PyPDFLoader

def pdf_loader(file_path):
    loader = PyPDFLoader(file_path)
    data = loader.load()
    return data

documents = pdf_loader(r"C:\Users\Megha\Desktop\GENAI_CONCEPTS\Chunking_Strategies\India's.pdf")
print(f"Successfully loaded {len(documents)} pages.")

def generate_contextual_chunk(document_context: str, chunk_content: str) -> str:
    prompt = f"""Given the following document overview context, provide a short 1-sentence 
    prefix providing missing context to anchor the specific text snippet.
    Document Context: {document_context}
    Text Snippet: {chunk_content}"""
    
    response = completion(
        model="openai/gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    
    context_prefix = response.choices[0].message.content
    return f"[Context: {context_prefix}] \n {chunk_content}"

doc_summary = documents[0].page_content
snippet = "Revenue grew 3% relative to projections."
print(generate_contextual_chunk(doc_summary, snippet))
