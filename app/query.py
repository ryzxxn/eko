from chroma.client import agent
from llm.gemini import geminiLLM
from llm.ollama import ollamaLLM

client, memory = agent("./chroma_db", "agent")

query = "vedant"

# Query the collection
result = memory.query(
    query_texts=query,
    n_results=20,
    where={"user_id": "user123"}
)

# Flatten and log the documents
flattened_documents = [item for sublist in result['documents'] for item in sublist]
documents_text = ' '.join(flattened_documents)
print(documents_text)

response = ollamaLLM.chat.completions.create(
    model="llama3.1:latest",
    n=1,
    messages=[
        {"role": "system", "content": "be funny based on the data provided"},
        {"role": "system", "content": documents_text},
    ]
)

print(response.choices[0].message)
