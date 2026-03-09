# Local LLM Inference Lab

Experiments exploring performance characteristics of large language
model inference on local hardware.

This repository investigates key aspects of LLM runtime behavior,
including latency, throughput, context scaling, and KV cache reuse. The
goal is to better understand practical trade-offs in deploying large
language models locally.

------------------------------------------------------------------------

## Motivation

Running LLMs locally is increasingly viable due to efficient model
architectures and optimized inference runtimes.

Key questions explored:

-   Time to First Token (TTFT)
-   Token generation throughput
-   Context length impact
-   KV cache reuse behavior
-   Model size vs inference performance

------------------------------------------------------------------------

## Hardware

MacBook Pro M2 Max\
64GB Unified Memory

------------------------------------------------------------------------

## Software

Python 3\
Ollama local inference server

Models tested:

-   qwen3:4b
-   qwen3:8b
-   qwen3:30b
-   llama3
-   llama2:13b
-   mistral

------------------------------------------------------------------------

## Repository Structure

local-llm-inference-lab

benchmarks/ throughput_test.py ttft_benchmark.py context_scaling_test.py

results/ model_scaling.md context_scaling.md ttft_results.md

docs/ inference_notes.md

README.md

------------------------------------------------------------------------

## Experiment 1 -- Decode Throughput

Measures token generation speed during decoding.

  Model       Parameters   Decode Speed
  ----------- ------------ --------------
  qwen3:4b    4B           \~70 tok/s
  qwen3:8b    8B           \~45 tok/s
  qwen3:30b   30B          \~55 tok/s

Observation:

Smaller models typically generate tokens faster, but optimized
architectures and inference runtimes can narrow the gap.

------------------------------------------------------------------------

## Experiment 2 -- Time to First Token (TTFT)

TTFT measures the delay between request submission and the first
generated token.

Includes:

-   prompt tokenization
-   prefill computation
-   KV cache initialization

Example observations:

  Model       TTFT
  ----------- -------------
  qwen3:4b    \~0.6s
  qwen3:8b    \~0.2--1.9s
  qwen3:30b   \~0.1--7s

First request often includes model warm-up and cache initialization.

------------------------------------------------------------------------

## Experiment 3 -- Context Length Scaling

Investigates how prompt length affects inference performance.

  Context Length   Decode Speed
  ---------------- --------------
  \~50 tokens      \~69 tok/s
  \~2000 tokens    \~26 tok/s

Observation:

Longer context increases KV cache size and memory bandwidth pressure,
reducing decoding throughput.

------------------------------------------------------------------------

## Experiment 4 -- Prompt Cache Reuse

Repeated prompts demonstrate significant TTFT reduction.

Example:

First request:

TTFT ≈ 140 seconds

Subsequent requests:

TTFT \< 1 second

Explanation:

The runtime reuses previously computed KV cache for identical prompt
prefixes.

------------------------------------------------------------------------

## Key Takeaways

1.  Context length strongly impacts decoding throughput.
2.  TTFT is dominated by the prefill stage for long prompts.
3.  KV cache reuse dramatically reduces latency.
4.  Local inference on consumer hardware is increasingly practical.

------------------------------------------------------------------------

## Future Work

Possible extensions:

-   quantization comparison
-   batch inference experiments
-   GPU utilization analysis
-   concurrent request benchmarking
-   vLLM comparison
-   TensorRT‑LLM benchmarking


