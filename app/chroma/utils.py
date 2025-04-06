from chromadb.utils import embedding_functions # type: ignore
import re
import uuid

def clean_text(text):
    # Remove newline characters and excessive whitespace
    text = re.sub(r'\n+', ' ', text)  # Replace newlines with a single space
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = text.strip()  # Remove leading and trailing whitespace
    # Remove unwanted characters (e.g., punctuation)
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

def chunker(text, chunk_size, overlap):
    # Clean the text
    text = clean_text(text)

    # Split the text into paragraphs and sentences
    paragraphs = text.split('\n')
    chunks = []

    for paragraph in paragraphs:
        sentences = paragraph.split('. ')
        for sentence in sentences:
            words = sentence.split()
            while words:
                if len(words) <= chunk_size:
                    chunks.append(' '.join(words))
                    break
                else:
                    chunk = words[:chunk_size]
                    chunks.append(' '.join(chunk))
                    words = words[chunk_size - overlap:]

    return chunks


ef = embedding_functions.DefaultEmbeddingFunction()

def get_ids(chunks):
    ids = [str(uuid.uuid4()) for _ in chunks]
    return ids

def llm_prep(chunks):
    # Initialize the cleaned text with the first chunk
    cleaned_text = [chunks[0]]

    # Iterate over the remaining chunks
    for i in range(1, len(chunks)):
        # Split the current chunk into words
        current_words = chunks[i].split()

        # Split the last sentence in cleaned_text into words
        last_sentence_words = cleaned_text[-1].split()

        # Find the overlap by comparing the end of the last sentence with the start of the current chunk
        overlap_index = 0
        for j in range(min(len(last_sentence_words), len(current_words))):
            if last_sentence_words[-j] != current_words[j-1]:
                break
            overlap_index = j

        # Remove the overlap from the current chunk
        if overlap_index > 0:
            current_words = current_words[overlap_index:]

        # Add the cleaned chunk to the result
        cleaned_text.append(' '.join(current_words))

    # Join all cleaned chunks into a single string
    return ' '.join(cleaned_text)