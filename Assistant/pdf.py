from pypdf import PdfReader
import tiktoken

class PDFError(Exception):
    pass

def extract_text(file):
    try:    
        reader = PdfReader(file) # reader calls pypdf to read the file

        full_text = ""

    
        # Extract each page to raw text, and if it isn't empty add it to full_text
        for page in reader.pages:
            text = page.extract_text()

            if text is not None:
                full_text += text + "\n\n"

        if not full_text.strip():
            raise PDFError("No readable text found in PDF.")

        full_length  = len(full_text) # Get full characters cout of the final text

        return full_text, full_length 

    except PDFError:
        raise

    except Exception as e:
            raise PDFError("Unable to extract text.") from e

def split_text(full_text, chunk_size=4000):
    encoding = tiktoken.get_encoding("o200k_base")

    paragraphs = [
        paragraph.strip() # cleans whitespace
        for paragraph in full_text.split("\n\n") # splits the full text into paragraph
        if paragraph.strip() # filters out empty paragraphs
    ]

    chunks = []
    current_chunk = []
    current_tokens = 0

    for paragraph in paragraphs:

        paragraph_tokens = len(encoding.encode(paragraph)) # calculates the token count of the paragraph

        # Adds paragraphs until the chunk size is reached
        if current_tokens + paragraph_tokens <= chunk_size:
            current_chunk.append(paragraph)
            current_tokens += paragraph_tokens

         # When the chunk size is exceeded, appends the current chunk to the final list
        else:
            if current_chunk:
                chunks.append("\n\n".join(current_chunk))

            current_chunk = [paragraph] # current_chunk (the next one) now starts with the last paragraph that didn't fit
            current_tokens = paragraph_tokens # And so does the token count

     # When no more paragraphs exist, adds the current chunk to the end of the function
    if current_chunk:
        chunks.append("\n\n".join(current_chunk))

    return chunks
