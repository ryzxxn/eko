
install the project
# Requirements
- Groq api Key
- Poetry
- python 3.10+
- make a .env file in root and save your GROQ_API_KEY

```
poetry install --no-root
```

```
poetry run python app/main.py
```

# prdefined tools
feel free to add your own
## get system info
### usage
- run script 
- 'tell me about my system specifications'

## post message to discord using webhook url
### usage
- modify the webhook url with your own url
- run script 
- 'send me a joke about computers on discord'
you could in theory have it send a specific message to a specific webhook url as well, after modify the function to accept a url in it's argument instead of hard coding it in its function
(you can pass the args in the query and the llm should handle it )

## webscrape using a url
### usage
- run script 
- 'webscrape https://en.wikipedia.org/wiki/Star_Wars'
