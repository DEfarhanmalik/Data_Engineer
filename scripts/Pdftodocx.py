#pip install pymupdf python-docx


import fitz  # PyMuPDF
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

def convert_pdf_to_docx(pdf_path, docx_path):
    try:
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)
        # Create a new Word document
        doc = Document()

        # Loop through each page in the PDF
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text = page.get_text()

            # Add text to the Word document
            if text.strip():  # Skip empty pages
                paragraph = doc.add_paragraph(text)
                paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT  # Optional: Align text to the left

            # Add a page break after every page except the last one
            if page_num < len(pdf_document) - 1:
                doc.add_page_break()

        # Save the Word document
        doc.save(docx_path)
        pdf_path = r'"C:\Users\13475\Desktop\pdf_converter\Farhan_Data_Resume.pdf"'
        print(f"PDF converted to DOCX successfully: {pdf_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
pdf_path = r"C:\Users\13475\Desktop\pdf_converter\Farhan_Data_Resume.pdf"
docx_path = r"C:\Users\13475\Desktop\pdf_converter\Farhan_Data_Resume..docx"

  # Path to save the output DOCX file
convert_pdf_to_docx(pdf_path, docx_path)
