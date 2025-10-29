import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate

load_dotenv()

def create_qa_chain(vectorstore):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.3
    )

    prompt = ChatPromptTemplate.from_template("""
    You are an intelligent assistant. Use the following context to answer the question.
    Keep your answer concise and relevant.

    Context:
    {context}

    Question:
    {input}
    """)

    doc_chain = create_stuff_documents_chain(llm, prompt)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    qa_chain = create_retrieval_chain(retriever, doc_chain)

    return qa_chain
