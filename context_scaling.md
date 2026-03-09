# Context Scaling Results

Experiment measuring performance impact of prompt length.

  Context Length   Decode Speed
  ---------------- --------------
  \~50 tokens      \~69 tok/s
  \~2000 tokens    \~26 tok/s

Insight:

Longer context increases KV cache size which creates memory bandwidth
pressure during decoding.
