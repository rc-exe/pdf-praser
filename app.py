import streamlit as st
import fitz  # PyMuPDF
import pdfplumber
import pandas as pd
import io
# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    """Extract text from a PDF uploaded via Streamlit."""
    with fitz.open("pdf", pdf_file.read()) as doc:
        text = ""
        for page in doc:
            text += page.get_text("text") + "\n"
    return text

    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

# Function to extract tables from PDF
def extract_tables_from_pdf(pdf_file):
    tables = []
    pdf_bytes = io.BytesIO(pdf_file.read())  # Convert file object to bytes
    with pdfplumber.open(pdf_bytes) as pdf:
        for page in pdf.pages:
            extracted_tables = page.extract_tables()
            for table in extracted_tables:
                df = pd.DataFrame(table)
                tables.append(df)
    return tables

# Streamlit UI
st.title("📄 Automated PDF Parser")
st.subheader("Extract text and tables from PDFs")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    st.success("PDF uploaded successfully!")

    # Extract text
    text = extract_text_from_pdf(uploaded_file)
    st.subheader("Extracted Text")
    st.text_area("Text Output", text, height=300)

    # Extract tables
    tables = extract_tables_from_pdf(uploaded_file)
    if tables:
        st.subheader("Extracted Tables")
        for i, table in enumerate(tables):
            st.write(f"Table {i+1}")
            st.dataframe(table)
    else:
        st.warning("No tables found in the PDF.")

