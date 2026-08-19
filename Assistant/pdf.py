from pypdf import PdfReader

def extract_text(file):
    reader = PdfReader(file)
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()

        if text is not None:
            full_text += text + "\n\n"
    return full_text

