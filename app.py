import os
import streamlit as st
from dotenv import load_dotenv
from rag_engine import load_pdf, create_vector_store, create_rag_chain, summarize_text, generate_qa_pairs

load_dotenv()

st.set_page_config(page_title="📄 PDF Chat RAG", layout="wide")
st.title("📄 PDF Chat - RAG Mini App")
st.write("✅ App Loaded Successfully")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    st.write("📥 File uploaded:", uploaded_file.name)
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Processing..."):
        try:
            docs = load_pdf(file_path)
            vectorstore = create_vector_store(docs)
            qa_chain = create_rag_chain(vectorstore)

            st.success("✅ Document processed!")

            # Summary Section
            st.subheader("📌 Summary")
            summary = summarize_text(docs)
            st.info(summary)

            # Question-Answer Section
            st.subheader("🧠 Possible Questions & Answers")
            qa_pairs = generate_qa_pairs(summary)
            for q, a in qa_pairs:
                st.markdown(f"**❓ {q}**")
                st.write(f"✅ {a}")

            # Ask PDF (Testing Mode)
            st.subheader("🧪 Ask your PDF (Testing Mode)")
            query = st.text_input("Ask a custom question:")
            if query:
                try:
                    result = qa_chain.run(query)
                    st.success(result)
                except Exception as e:
                    st.error(f"❌ Failed to generate answer: {e}")
        except Exception as e:
            st.error(f"❌ Error while processing PDF: {e}")
