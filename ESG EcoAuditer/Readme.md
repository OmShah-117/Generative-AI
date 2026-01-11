# 🌿 EcoAudit Intelligence  ...
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
```
---

## Results / Output

- Evidence-based answers to sustainability questions
- Source documents and page references for every response
- Faster and more reliable ESG verification compared to manual review

---

## Model Performance & Evaluation
### Evaluation Approach
- Accuracy: Ensured by restricting responses to retrieved document context
- Hallucination Control: Temperature set to zero
- Relevance: Top-K document retrieval via FAISS

### Metrics (Qualitative)
- Precision of retrieved document chunks
- Consistency of answers across repeated queries
- Traceability of responses to source documents

---

## Limitations
- Dependent on document quality and structure
- No numerical scoring or benchmarking included
- Not suitable for real-time regulatory compliance decisions
- LLM responses are only as good as the uploaded data

---

## Future Improvements

- Automated ESG scoring and benchmarking
- Multilingual document support
- Visual dashboards for trend analysis
- Integration with regulatory databases
- Support for additional SDGs (e.g., Climate Action – SDG 13)
  
---

## Disclaimer
- This project is intended for educational and demonstration purposes only.
- It is not a certified auditing or compliance tool. Users are encouraged to:
1. Experiment with different datasets
2. Improve document quality
3. Extend functionality or evaluation metrics

---
⭐ If you find this project useful, feel free to star the repository and explore further enhancements!
