# Context Scaling Results

  Context Length   Decode Speed
  ---------------- --------------
  \~50 tokens      \~69 tok/s
  \~2000 tokens    \~26 tok/s

Insight:

Long prompts increase KV cache memory usage which slows decoding.
