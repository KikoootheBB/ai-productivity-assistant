from pypdf import PdfReader

def extract_text(file):
    reader = PdfReader(file)
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()

        if text is not None:
            full_text += text + "\n\n"

    full_length  = len(full_text)

    return full_text, full_length 

def split_text(full_text):
    chunks = []
    chunk_size = 10000
    total_length = len(full_text)

    for index in range(0, total_length, chunk_size):

        end_index = index + chunk_size
        current_chunk = full_text[index:end_index]

        chunks.append(current_chunk)

    return chunks
