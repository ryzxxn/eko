import chromadb  # type: ignore
from chromadb.utils import embedding_functions  # type: ignore
from chroma.utils import ef, chunker, get_ids  # type: ignore

# Function to initialize Chroma client & collection
def initialize_chroma_client(persistent_path: str, collection_name: str):
    try:
        client = chromadb.PersistentClient(path=persistent_path)
        # Use a proper embedding function
        embedding_fn = ef
        collection = client.get_or_create_collection(
            name=collection_name,
            embedding_function=embedding_fn
        )
        return client, collection
    except Exception as e:
        print(f"Error initializing ChromaDB: {e}")
        raise

# Initialize Chroma client & collection
client, memory = initialize_chroma_client("./chroma_db", "agent")

text = """
If you're looking for random paragraphs, you've come to the right place. When a random word or a random sentence isn't quite enough, the next logical step is to find a random paragraph. We created the Random Paragraph Generator with you in mind. The process is quite simple. Choose the number of random paragraphs you'd like to see and click the button. Your chosen number of paragraphs will instantly appear.

While it may not be obvious to everyone, there are a number of reasons creating random paragraphs can be useful. A few examples of how some people use this generator are listed in the following paragraphs.

Creative Writing
Generating random paragraphs can be an excellent way for writers to get their creative flow going at the beginning of the day. The writer has no idea what topic the random paragraph will be about when it appears. This forces the writer to use creativity to complete one of three common writing challenges. The writer can use the paragraph as the first one of a short story and build upon it. A second option is to use the random paragraph somewhere in a short story they create. The third option is to have the random paragraph be the ending paragraph in a short story. No matter which of these challenges is undertaken, the writer is forced to use creativity to incorporate the paragraph into their writing.

Tackle Writers' Block
A random paragraph can also be an excellent way for a writer to tackle writers' block. Writing block can often happen due to being stuck with a current project that the writer is trying to complete. By inserting a completely random paragraph from which to begin, it can take down some of the issues that may have been causing the writers' block in the first place.

Beginning Writing Routine
Another productive way to use this tool to begin a daily writing routine. One way is to generate a random paragraph with the intention to try to rewrite it while still keeping the original meaning. The purpose here is to just get the writing started so that when the writer goes onto their day's writing projects, words are already flowing from their fingers.

Writing Challenge
Another writing challenge can be to take the individual sentences in the random paragraph and incorporate a single sentence from that into a new paragraph to create a short story. Unlike the random sentence generator, the sentences from the random paragraph will have some connection to one another so it will be a bit different. You also won't know exactly how many sentences will appear in the random paragraph.

Programmers
It's not only writers who can benefit from this free online tool. If you're a programmer who's working on a project where blocks of text are needed, this tool can be a great way to get that. It's a good way to test your programming and that the tool being created is working well.

Above are a few examples of how the random paragraph generator can be beneficial. The best way to see if this random paragraph picker will be useful for your intended purposes is to give it a try. Generate a number of paragraphs to see if they are beneficial to your current project.

If you do find this paragraph tool useful, please do us a favor and let us know how you're using it. It's greatly beneficial for us to know the different ways this tool is being used so we can improve it with updates. This is especially true since there are times when the generators we create get used in completely unanticipated ways from when we initially created them. If you have the time, please send us a quick note on what you'd like to see changed or added to make it better in the future.
"""

user_id = "user123"
agent_id = "agent123"

# Chunk the text
chunks = chunker(text=text, chunk_size=100, overlap=20)

# Debug: Check chunking output
if not chunks:
    print("Error: No chunks generated!")
    exit()

# Generate unique IDs for each chunk
ids = get_ids(chunks)

# Process & upsert chunks
for i, chunk in enumerate(chunks):
    print(f"\nProcessing chunk {i + 1}: {chunk}")
    
    try:
        # Upsert into ChromaDB (let collection handle embedding)
        memory.add(
            documents=[chunk],
            metadatas=[{"user_id": user_id, "agent_id": agent_id}],
            ids=[ids[i]]
        )
    except Exception as e:
        print(f"Error processing chunk {i}: {e}")
        continue

# Verify insertion
print(f"Total documents in collection: {memory.count()}")
print("All chunks processed successfully!")


query = "Generating random paragraphs can be an excellent way for writers"

embeded_text = ef(query)

results = memory.query(
    query_embeddings=[embeded_text],
    n_results=10,
    where_document={"$contains":query}
)

print("Results Structure:", results["documents"])

