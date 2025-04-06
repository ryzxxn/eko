from uuid import uuid4
from chroma.client import agent
from chroma.utils import ef, chunker, get_ids, llm_prep  # type: ignore
from llm.ollama import ollamaLLM
from dev.logger import get_logger

log = get_logger(__name__)

# Initialize Chroma client & collection
client, memory = agent("./chroma_db", "agent")

# Read text from file
file_path = "./updated_discord_messages.txt"
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
except FileNotFoundError:
    log.error(f"File not found: {file_path}")
    exit()

user_id = "user123"
agent_id = "agent123"

# Chunk the text
chunks = chunker(text=text, chunk_size=100, overlap=20)

# Debug: Check chunking output
if not chunks:
    log.error("Error: No chunks generated!")
    exit()

# Generate unique IDs for each chunk
ids = get_ids(chunks)

# Process & upsert chunks
for i, chunk in enumerate(chunks):
    log.info(f"\nProcessing chunk {i + 1}: {chunk}")

    try:
        # Upsert into ChromaDB (let collection handle embedding)
        memory.add(
            documents=[chunk],
            metadatas=[{"user_id": user_id, "agent_id": agent_id}],
            ids=[ids[i]]
        )
    except Exception as e:
        log.error(f"Error processing chunk {i}: {e}")
        continue

# Verify insertion
log.info(f"Total documents in collection: {memory.count()}")
log.info("All chunks processed successfully!")

query = "earthquake"

# Query the collection
result = memory.query(
    query_texts=query,
    n_results=20,
    where={"user_id": user_id}
)

# Flatten and log the documents
flattened_documents = [item for sublist in result['documents'] for item in sublist]
documents_text = ' '.join(flattened_documents)
log.info(documents_text)

# Interact with LLM
try:
    response = ollamaLLM.chat.completions.create(
        model="llama3.1:latest",
        messages=[{"role": "user", "content": "hello"}]
    )
    log.info(f"LLM Response: {response.choices[0].message.content}")

    # Store LLM response in ChromaDB
    memory.add(
        documents=[response.choices[0].message.content],
        metadatas=[{"user_id": "system", "agent_id": agent_id}],
        ids=[str(uuid4())]
    )
except Exception as e:
    log.error(f"Error interacting with LLM: {e}")
