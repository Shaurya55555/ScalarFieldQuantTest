# =========================
#  Module: Vector DB Build
# =========================

from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_huggingface import HuggingFaceEmbeddings

# Build vector database
def run_db_build():
    loader = DirectoryLoader(
        'src\data',
        glob='*.pdf',
        loader_cls=PyPDFLoader
    )

    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=5000,
        chunk_overlap=500
    )

    texts = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-MiniLM-L6-v2',
        model_kwargs={'device': 'cpu'}
    )

    vectorstore = FAISS.from_documents(texts, embeddings)

    vectorstore.save_local(
        'vectorstore\db_faiss'
    )

if __name__ == "__main__":
    run_db_build()