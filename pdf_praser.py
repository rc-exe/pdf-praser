import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text("text") + "\n"  # Extract text from each page

    return text

if __name__ == "__main__":
    pdf_path = r"C:\Users\rites\Desktop\Ritesh Chakramani.pdf"  # Change this to your PDF file path
    extracted_text = extract_text_from_pdf(pdf_path)
    
    # Save the extracted text to a file
    with open("extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(extracted_text)
    
    print("Text extraction complete! Check extracted_text.txt")
