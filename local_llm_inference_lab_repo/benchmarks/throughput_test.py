
import requests, time

MODEL = "qwen3:8b"
PROMPT = "Explain transformer architecture."

url = "http://localhost:11434/api/generate"

for i in range(3):
    start = time.time()
    response = requests.post(url, json={
        "model": MODEL,
        "prompt": PROMPT,
        "stream": False
    })
    latency = time.time() - start
    text = response.json()["response"]
    tokens = len(text.split())
    print("Run", i)
    print("Latency:", latency)
    print("Tokens/sec:", tokens/latency)
