# 📚 RAG-Powered PDF Q&A Engine 🚀

> Upload any PDF. Ask any question. Get AI-powered answers with Retrieval-Augmented Generation (RAG).  
> Built with ❤️ to blend Large Language Models and powerful vector search.

---

## 🧠 What is This?

A **lightweight RAG (Retrieval-Augmented Generation)** pipeline that lets you:

- 📄 Upload your PDF
- 🔍 Extract context using vector embeddings
- 💬 Ask *any* question based on that content
- 🤖 Get smart answers via OpenAI / HuggingFace models

Perfect for **researchers**, **students**, **developers**, and **AI hobbyists** who want to interact with documents like never before.

---

## 🔥 Demo Snapshot

<img src="static/screenshot.png" alt="Demo Screenshot" width="100%" />

---

## 💡 Why This Project?

- ✨ Combines **document parsing + semantic search + LLM reasoning**
- ⚡ Superfast retrieval using **ChromaDB**
- 🧱 Modular pipeline (easy to extend)
- 🎯 Designed for practical real-world use

---

## 🛠️ Tech Stack

| Layer         | Tool/Library                      |
|--------------|-----------------------------------|
| Backend       | Python, FastAPI / CLI             |
| Retrieval     | LangChain, ChromaDB, FAISS        |
| Generation    | OpenAI API / HuggingFace Transformers |
| Parsing       | PyPDF2, pdfminer.six              |
| Environment   | dotenv                            |

---

## 🗂️ Project Structure
| Path                 | Description                                 |
| -------------------- | ------------------------------------------- |
| `app.py`             | 🟦 Main entry point                         |
| `rag_engine.py`      | 🧠 Core RAG logic (retrieval + generation)  |
| `requirements.txt`   | 📦 Project dependencies                     |
| `.env`               | 🔐 API keys (do not commit this!)           |
| `.gitignore`         | 🚫 Files to exclude from Git                |
| `chroma_db/`         | 🧬 Vector database (auto-generated)         |
| `data/`              | 📄 Input PDF files or extracted text chunks |
| `static/`            | 🖼️  UI images or frontend assets           |
| └── `screenshot.png` | 🖼️ UI snapshot                             |
| `README.md`          | 📘 Project documentation                    |



---

## ⚙️ Installation & Setup

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/rag-mini.git
cd rag-mini

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your OpenAI key
echo "OPENAI_API_KEY=sk-..." > .env

# 4. Run the app
python app.py

✨ Features
✅ Clean PDF parsing and chunking

🔍 Fast vector-based document retrieval (ChromaDB)

💬 Seamless Q&A with your own PDFs

🔄 Fully modular & extendable

📎 Sample Use Cases
📘 Academic Paper Q&A

💼 Contract / Legal Document Insights

📊 Business Reports / Financial PDFs

🧪 Research Summaries and Notes

🧑‍💻 About Me
Hi! I'm Maya Adhitya, an AI & ML enthusiast from Hyderabad, India 🇮🇳

🧠 Passionate about ML, NLP, and AI tutoring

💼 Interned at Accenture & worked on real-world AI pipelines

🌍 Fluent in English + beginner in German 🇩🇪

🔗 LinkedIn | ✉️ Email Me

📄 License
Licensed under the MIT License.
Feel free to use, fork, and improve it — just give credit! 🙏
