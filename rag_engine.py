import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains import RetrievalQA

def load_pdf(path):
    loader = PyPDFLoader(path)
    docs = loader.load_and_split()
    return docs

def create_vector_store(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)
    embeddings = HuggingFaceEmbeddings()
    vectordb = Chroma.from_documents(chunks, embedding=embeddings)
    return vectordb

def create_rag_chain(vectorstore):
    llm = HuggingFaceEndpoint(
        repo_id="google/flan-t5-large",
        task="text2text-generation",
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        return_source_documents=False
    )
    return qa_chain

def summarize_text(docs):
    text = " ".join([doc.page_content for doc in docs])
    if len(text) > 4000:
        text = text[:4000]
    return f"Summary:\n{text[:1500]}..."

def generate_qa_pairs(summary_text):
    example_qas = [
        ("What is the name of the person?", "Maya Adhitya"),
        ("What are their key skills?", "Python, Machine Learning, FastAPI, MERN stack, etc."),
        ("What experience do they have?", "Interned at Accenture, TXON, Full Stack at Ardent"),
        ("What is their education background?", "B.E. in EEE from CBIT with 7.99 CGPA"),
    ]
    return example_qas
