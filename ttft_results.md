# TTFT Benchmark Results

Time To First Token (TTFT) measures latency before the first token
appears.

  Model       TTFT
  ----------- -------------
  qwen3:4b    \~0.6s
  qwen3:8b    \~0.2--1.9s
  qwen3:30b   \~0.1--7s

Notes:

First runs include model warm-up and cache initialization which
significantly increases TTFT. Subsequent requests benefit from cache
reuse.
