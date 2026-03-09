# Local LLM Inference Lab

A small engineering lab exploring performance characteristics of local
Large Language Model inference.

Focus areas:

-   Time To First Token (TTFT)
-   Decode throughput (tokens/sec)
-   Context length scaling
-   KV cache reuse behavior
-   Model size vs performance

Hardware used:

MacBook Pro M2 Max\
64GB Unified Memory

Runtime:

Ollama local inference server

------------------------------------------------------------------------

## Experiments

1.  TTFT Benchmark\
    Measures latency until the first generated token.

2.  Decode Throughput\
    Measures tokens/sec during generation.

3.  Context Scaling\
    Measures how longer prompts affect performance.

4.  Model Scaling\
    Compares performance across models (4B / 8B / 30B).

------------------------------------------------------------------------

## Repository Structure

benchmarks/ ttft_benchmark.py throughput_test.py context_scaling_test.py

results/ model_scaling.md context_scaling.md ttft_results.md

docs/ llm_inference_architecture.png benchmark_chart.png

------------------------------------------------------------------------

## Key Takeaways

Longer context increases KV cache size which reduces decoding
throughput.

First inference requests include model warm‑up which increases TTFT.

Modern laptops can run surprisingly capable LLMs locally.

------------------------------------------------------------------------

## License

MIT
