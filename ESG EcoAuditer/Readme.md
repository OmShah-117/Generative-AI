# 🌿 EcoAudit Intelligence  
**AI-Powered Sustainability Compliance & Verification Engine**

EcoAudit Intelligence is an advanced **AI-driven document auditing and compliance system** designed to analyze corporate sustainability and ESG reports. Built using a **Retrieval-Augmented Generation (RAG)** architecture, the application enables users to ask natural language questions and receive **strictly evidence-backed answers** directly sourced from uploaded documents.

This project demonstrates how **responsible AI** can be applied to improve transparency, reduce manual auditing effort, and combat greenwashing in sustainability reporting.

---

## Short Description
EcoAudit Intelligence allows users to upload sustainability or ESG reports (PDFs) and query them using natural language. The system retrieves relevant document sections using semantic search and generates accurate, source-cited responses using a large language model—ensuring **no hallucinations and full traceability**.

---

## Tech Stack / Tools Used
- **Programming Language:** Python  
- **Frontend / UI:** Streamlit  
- **LLM Framework:** LangChain  
- **Large Language Model:** Llama-3.3-70B (via Groq API)  
- **Vector Database:** FAISS  
- **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`)  
- **Document Processing:** PyPDFLoader  
- **Text Chunking:** RecursiveCharacterTextSplitter  

---

## Key Features
- Upload and analyze multiple sustainability reports (PDFs)
- Semantic search with FAISS vector indexing
- Retrieval-Augmented Generation (RAG) for factual accuracy
- **Strict Accuracy Mode** – answers only from document evidence
- Source citations with document name and page numbers
- Professional Streamlit UI with glassmorphism design
- Adjustable chunk size for granular or high-level analysis

---

## Dataset / Inputs
- **Input Type:** PDF documents  
- **Examples:**  
  - ESG Reports  
  - Sustainability Reports  
  - Annual Reports with environmental or social disclosures  

> ⚠️ No public dataset is bundled. Users are encouraged to upload their own documents.

---

## How It Works (High-Level)
1. User uploads one or more PDF documents.
2. Text is extracted using `PyPDFLoader`.
3. Documents are split into semantic chunks.
4. Each chunk is converted into vector embeddings.
5. FAISS stores embeddings for fast similarity search.
6. On user query:
   - Relevant chunks are retrieved
   - LLM generates answers **only from retrieved context**
7. Results are displayed with verified evidence sources.

---

## Installation & Setup
### Clone the Repository
```bash
git clone https://github.com/your-username/ecoaudit-intelligence.git
cd ecoaudit-intelligence

