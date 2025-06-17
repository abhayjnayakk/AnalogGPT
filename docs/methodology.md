# Methodology

## 1. gm/Id–Driven Initialization
We pre-compute gm/Id vs. V\_OV lookup tables for common technology nodes (65 nm ➜ 7 nm). The solver provides **first-pass transistor widths** ensuring:

* Design-space pruning  
* Faster convergence for downstream RL

## 2. Topology Generation with Domain-Aware LLM
Instead of tokenizing plain text, we embed **circuit graphs** using:

* SPICE-specific tokens (`M`, `R`, `C`, `V`, …)  
* Edge-conditioned positional encodings (node connections)

Sequence-to-sequence objective: **spec → ordered SPICE statements**

## 3. RL-Based Sizing
* Environment: PySpice wrapper providing DC/AC metrics  
* Agent: PPO with action mask (legal width/length bins)  
* Reward: weighted geometric mean of closed-loop specs (GBW, PSRR, …)

## 4. Verification Loop
1. Export NGSpice netlist  
2. Run transient / AC / noise analyses  
3. Compare to spec; iterate if unmet 