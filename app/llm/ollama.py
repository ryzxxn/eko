import openai # type: ignore

ollamaLLM = openai.OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)