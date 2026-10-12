from langchain_community.document_loaders import PyPDFLoader
import openai
from dotenv import load_dotenv
load_dotenv()
def pdf_loader(file_path):
    loader = PyPDFLoader(file_path)
    data = loader.load()
    return data

documents = pdf_loader(r"C:\Users\Megha\Desktop\GENAI_CONCEPTS\Chunking_Strategies\India's.pdf")
print(f"Successfully loaded {len(documents)} pages.")

def get_propositions(text_chunk):
    client = openai.OpenAI()
    
    prompt = f"Break down the following text into a list of atomic statements/facts:\n\n{text_chunk}"
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.split("\n")

text = documents[0].page_content
propositions = get_propositions(text)

print(len(propositions))
print("--- Generated Propositions ---")
for prop in propositions:
    print(prop)
