from PyPDF2 import PdfReader
from detector import is_me_present

def scan_pdf(file_path: str) -> bool:
    try:
        reader = PdfReader(file_path)

        for page in reader.pages:
            text = page.extract_text()
            if text and is_me_present(text):
                return True

    except Exception as e:
        print("PDF scan error:", e)

    return False
