from chromadb.utils import embedding_functions # type: ignore
import re

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

    # Split the text into words
    words = text.split()

    # Recursive function to chunk the text by words
    def recursive_chunk(words, chunk_size, overlap):
        if len(words) <= chunk_size:
            return [' '.join(words)]
        else:
            chunk = words[:chunk_size]
            remaining_words = words[chunk_size - overlap:]
            return [' '.join(chunk)] + recursive_chunk(remaining_words, chunk_size, overlap)

    return recursive_chunk(words, chunk_size, overlap)


ef = embedding_functions.DefaultEmbeddingFunction()