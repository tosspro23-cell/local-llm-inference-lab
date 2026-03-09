
import requests, time

MODEL = "qwen3:8b"
PROMPT = "Explain transformer attention in detail."

url = "http://localhost:11434/api/generate"

start = time.time()
response = requests.post(url, json={
    "model": MODEL,
    "prompt": PROMPT,
    "stream": False
})

latency = time.time() - start
data = response.json()

tokens = len(data["response"].split())

print("Model:", MODEL)
print("Generated tokens:", tokens)
print("Total latency:", latency)
print("Tokens/sec:", tokens/latency)
