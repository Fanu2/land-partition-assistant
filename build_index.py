# build_index.py

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

# --- Load PDF ---
pdf_path = "haryana_land_revenue_act.pdf"
loader = PyPDFLoader(pdf_path)
documents = loader.load()

# --- Split into Chunks ---
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

# --- Embed and Save FAISS Index ---
embedding = OpenAIEmbeddings()
db = FAISS.from_documents(chunks, embedding)
db.save_local("faiss_index")

print("✅ FAISS index built and saved to 'faiss_index'")
