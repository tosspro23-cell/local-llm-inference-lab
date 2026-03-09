# Model Scaling Results

Hardware: MacBook Pro M2 Max 64GB unified memory

  Model       Parameters   Decode Speed
  ----------- ------------ --------------
  qwen3:4b    4B           \~70 tok/s
  qwen3:8b    8B           \~45 tok/s
  qwen3:30b   30B          \~55 tok/s

Observation:

Model size influences throughput, but architecture and inference
optimization also play a major role.
