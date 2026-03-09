
import requests, time

MODEL = "qwen3:8b"
BASE_PROMPT = "Explain transformer attention. "
PROMPT = BASE_PROMPT * 50

url = "http://localhost:11434/api/generate"

start = time.time()
response = requests.post(url, json={
    "model": MODEL,
    "prompt": PROMPT,
    "stream": False
})

latency = time.time() - start
text = response.json()["response"]
tokens = len(text.split())

print("Context length test")
print("Generated tokens:", tokens)
print("Latency:", latency)
print("Tokens/sec:", tokens/latency)
