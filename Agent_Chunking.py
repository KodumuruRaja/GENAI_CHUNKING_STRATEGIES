from langchain_community.document_loaders import PyPDFLoader

from dotenv import load_dotenv
load_dotenv()

def pdf_loader(file_path):
    loader = PyPDFLoader(file_path)
    data = loader.load()
    return data

documents = pdf_loader(r"C:\Users\Megha\Desktop\GENAI_CONCEPTS\Chunking_Strategies\India's.pdf")
print(f"Successfully loaded {len(documents)} pages.")

import openai

def agentic_splitter(text, target_size=20):
    client = openai.OpenAI()
    
    prompt = f"""
    You are an agent specializing in document chunking. Read the text below and split it 
    into logical sections of roughly {target_size} characters. 
    Insert a unique delimiter '|||' where each chunk should split.
    
    Text: {text}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content.split("|||")

agentic_chunks = agentic_splitter(documents[0].page_content)
print(f"Number of agentic chunks created: {len(agentic_chunks)}")