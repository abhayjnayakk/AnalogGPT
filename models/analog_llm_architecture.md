# “Schmitt-GPT” – A Domain-Specific LLM

* 1.2 B params, decoder-only  
* Tokenizer includes 200 bespoke SPICE tokens  
* Positional Encoding = 3-tuple (device index, pin index, net hash)  
* Adapter layers loadable into Llama-2 checkpoint  

**Status:** tokenizer + config complete; training scheduled on 8 × A100 cluster. 