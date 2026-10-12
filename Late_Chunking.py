from langchain_community.document_loaders import PyPDFLoader

def pdf_loader(file_path):
    loader = PyPDFLoader(file_path)
    data = loader.load()
    return data

documents = pdf_loader(r"C:\Users\Megha\Desktop\GENAI_CONCEPTS\Chunking_Strategies\India's.pdf")
print(f"Successfully loaded {len(documents)} pages.")


import torch
import torch.nn.functional as F
from transformers import AutoModel, AutoTokenizer

def late_chunking(model_id: str, text: str, boundaries: list[tuple[int, int]]):
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    # Change line 8 in Late_Chunking.py to this:
    model = AutoModel.from_pretrained(model_id, trust_remote_code=True, force_download=True).eval()

    
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        # Get contextualized representations across the full document text
        outputs = model(**inputs)
        token_embeddings = outputs[0][0]
        
    chunk_embeddings = []
    for start, end in boundaries:
        s_tok = inputs.char_to_token(start)
        e_tok = inputs.char_to_token(end - 1)
        if s_tok is None or e_tok is None: continue
        
        # Mean pool specific chunk tokens after document-wide contextualization
        mean_pooled = token_embeddings[s_tok : e_tok + 1].mean(dim=0)
        chunk_embeddings.append(F.normalize(mean_pooled, p=2, dim=0))
        
    return chunk_embeddings

# Example usage
doc = documents[0].page_content
# Character boundary markers for sentence 1 and sentence 2
slices = [(0, 31), (32, 74)]
embs = late_chunking("jinaai/jina-embeddings-v3", doc, slices)
print(f"Generated {len(embs)} late-chunked embeddings.")
