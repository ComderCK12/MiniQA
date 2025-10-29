import streamlit as st
from backend.vector_store import create_vectorstore_from_file
from backend.qa_chain import create_qa_chain

st.set_page_config(page_title="MiniQA - Gemini Powered", page_icon="🤖")

st.title("🤖 MiniQA (Gemini-Powered)")
st.write("Upload a document and ask questions about it!")

uploaded_file = st.file_uploader("📄 Upload a document (PDF, TXT, DOCX)", type=["pdf", "txt", "docx"])

if uploaded_file:
    with st.spinner("Processing document..."):
        vectorstore = create_vectorstore_from_file(uploaded_file)
        qa_chain = create_qa_chain(vectorstore)
        st.session_state.qa = qa_chain
    st.success("✅ Document processed successfully!")

if "qa" in st.session_state:
    query = st.text_input("💬 Ask a question about your document:")
    if query:
        with st.spinner("Thinking..."):
            response = st.session_state.qa.invoke({"input": query})
        st.markdown(f"**Answer:** {response['answer']}")
else:
    st.info("Please upload a document to start asking questions.")