import streamlit as st
import os
import tempfile

from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_classic.chains import RetrievalQA
from langchain_text_splitters import RecursiveCharacterTextSplitter

#Styling and Layout 
st.set_page_config(page_title="EcoAudit Intelligence", layout="wide", page_icon="🌿")

st.markdown("""
    <style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

    * { font-family: 'Inter', sans-serif; }

    /* Background Gradient */
    .stApp {
        background: radial-gradient(circle at top right, #0a192f, #020c1b);
        color: #e6f1ff;
    }

    /* Professional Glassmorphism Card */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }

    /* Gradient Title */
    .gradient-text {
        background: linear-gradient(90deg, #00d4ff, #00ff7f);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 3.5rem;
        letter-spacing: -1px;
    }

    /* Custom Sidebar */
    [data-testid="stSidebar"] {
        background-color: #020c1b !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Premium Button */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #00d4ff, #00ff7f);
        color: #020c1b;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        height: 3em;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 212, 255, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)


#More Stuff
st.logo("https://cdn-icons-png.flaticon.com/512/892/892926.png", size="large")

#Header
st.markdown('<h1 class="gradient-text">EcoAudit Intelligence</h1>', unsafe_allow_html=True)
st.markdown("<p style='color: #8892b0; font-size: 1.2rem;'>Advanced AI Document Verification & Compliance Engine</p>", unsafe_allow_html=True)

#"What & Why" Glass Cards
st.markdown("<br>", unsafe_allow_html=True)
col_a, col_b = st.columns(2)
with col_a:
    st.markdown("""<div class="glass-card">
    <h3 style="color: #00d4ff; margin-top:0;">🔍 Digital Detective</h3>
    <p style="color: #8892b0;">This service automatically scans your PDFs to verify sustainability claims. 
    Instead of manually reading 200 pages, our AI finds the facts in seconds.</p>
    </div>""", unsafe_allow_html=True)

with col_b:
    st.markdown("""<div class="glass-card">
    <h3 style="color: #00ff7f; margin-top:0;">🛡️ Verified Honesty</h3>
    <p style="color: #8892b0;">We use a 'Strict Accuracy' mode. The AI is forbidden from guessing; 
    it only provides answers backed by the evidence in your uploaded files.</p>
    </div>""", unsafe_allow_html=True)


#Sidebar
with st.sidebar:
    st.markdown("### 📁 Data Repository")
    uploaded_files = st.file_uploader("Upload Reports (PDF)", type="pdf", accept_multiple_files=True)
    
    st.divider()
    st.markdown("### ⚙️ Engine Settings")
    chunk_val = st.select_slider("Reading Granularity", options=[500, 1000, 1500], value=1000)
    process_btn = st.button("EXECUTE AUDIT", use_container_width=True)
    
    #API Checking
    if "GROQ_API_KEY" in st.secrets:
        os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
    else:
        os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY", "")


#Audit(RAG Logic)
if process_btn:
    if not uploaded_files:
        st.toast("Please upload files first!", icon="⚠️")
    else:
        with st.status("🧠 Initializing Neural Audit...", expanded=True) as status:
            all_docs = []
            for uploaded_file in uploaded_files:
                with tempfile.NamedTemporaryFile(delete=False) as tf:
                    tf.write(uploaded_file.getbuffer())
                    file_path = tf.name
                loader = PyPDFLoader(file_path)
                file_docs = loader.load()
                for d in file_docs: d.metadata["source_name"] = uploaded_file.name
                all_docs.extend(file_docs)
                os.remove(file_path)
            
            st.write("Reading pages...")
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_val, chunk_overlap=150)
            chunks = text_splitter.split_documents(all_docs)
            
            st.write("Mapping intelligence...")
            embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
            vectorstore = FAISS.from_documents(chunks, embeddings)
            
            #Strictness
            template = """
            Use ONLY the following context to answer. If the answer isn't there, say you can't find it.
            Context: {context}
            Question: {question}
            Helpful Answer:"""
            
            llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0)
            st.session_state.auditor = RetrievalQA.from_chain_type(
                llm=llm, 
                retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
                return_source_documents=True,
                chain_type_kwargs={"prompt": PromptTemplate(template=template, input_variables=["context", "question"])}
            )
            status.update(label="✅ Audit Engine Ready", state="complete", expanded=False)

#Analysis Interface
if "auditor" in st.session_state:
    st.markdown("<br><h2 style='color: #ccd6f6;'>🔍 Audit Inquiry</h2>", unsafe_allow_html=True)
    
    #Preset Buttons
    c1, c2, c3 = st.columns(3)
    preset_query = ""
    if c1.button("🌍 Environmental Data", use_container_width=True): preset_query = "What are the carbon and energy goals?"
    if c2.button("🤝 Social Standards", use_container_width=True): preset_query = "What is mentioned about diversity and fair labor?"
    if c3.button("⚖️ Compliance Risks", use_container_width=True): preset_query = "Are there any legal fines or ethical risks noted?"

    user_query = st.text_input("Ask a question about the evidence:", value=preset_query, placeholder="e.g., When is the Net Zero target date?")

    if user_query:
        with st.spinner("Analyzing data points..."):
            response = st.session_state.auditor.invoke(user_query)
            
            #Displaying result in a glass card
            st.markdown(f"""<div class="glass-card">
            <h4 style="color: #00d4ff; margin-top:0;">Auditor's Conclusion:</h4>
            <p style="font-size: 1.1rem; line-height: 1.6;">{response["result"]}</p>
            </div>""", unsafe_allow_html=True)
            
            #Evidence Display
            st.subheader("📍 Verified Evidence")
            cols = st.columns(3)
            for idx, doc in enumerate(response["source_documents"][:3]):
                with cols[idx]:
                    st.markdown(f"""<div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.05);">
                    <p style="color: #00ff7f; font-size: 0.8rem; margin:0;">SOURCE: {doc.metadata.get('source_name')}</p>
                    <p style="color: #8892b0; font-size: 0.85rem;">...{doc.page_content[:200]}...</p>
                    <p style="color: #00d4ff; font-size: 0.8rem; margin:0;">PAGE: {doc.metadata.get('page')}</p>
                    </div>""", unsafe_allow_html=True)
else:
    st.info("System Standby. Please upload and process documents to begin intelligence gathering.")