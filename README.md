# Analog-GPT: Generative AI for Analog IC Design  
*From written specifications to SPICE-ready circuits.*

![ChatGPT Image Jun 18, 2025, 02_26_03 AM](https://github.com/user-attachments/assets/1d21b99b-48c7-435c-a464-e9a2c02ab5b7)


## 🤝 Collaboration
**Analog-GPT** is a joint project between **CelesticLabs** *(founded by Abhay – Lead AI Engineer)* and **NeuroAnalog** *(founded by Abhilash – Lead Analog Engineer)*.  
By uniting frontier generative-model research with battle-hardened silicon know-how, we are building the first *AI-native* analog design copilot capable of turning a paragraph of specs into a verified SPICE netlist.

<!-- Optional: add partner logos once available -->

## Project Overview
Analog-GPT tackles the *holy-grail* problem of **analog automation**: given a set of electrical specifications (gain, bandwidth, noise, power, area, …) the system emits a **SPICE-ready netlist** that already meets—or is very close to—the target metrics.  

The core idea is to blend *first-principles* gm/Id sizing with **generative LLMs** (for topology exploration) and **reinforcement learning** (for final parametric tuning). The result is a closed design loop that can propose, simulate, and iteratively improve circuits with *zero* human intervention.

## Problem
Analog IC design is slow, expert-driven, and iteration-heavy. We aim to shorten that cycle **10×** by combining:

1. gm/Id methodology for first-order sizing  
2. Large-Language-Models (LLMs) to synthesize novel topologies  
3. Reinforcement Learning (RL) for fine-grained transistor sizing  
4. Automated SPICE simulation & verification loops  

## Modular Pipeline
```text
          ┌──────────┐   spec  ┌──────────┐
          │  User /  │ ───────▶│ gm/Id    │
          │  Specs   │         │ Solver   │
          └──────────┘         └────┬─────┘
                                     │ coarse sizes
                        ┌────────────▼────────────┐
                        │  Topology LLM (∆)       │
                        └────┬────────────────────┘
                             │ netlist skeleton
                    ┌────────▼─────────┐
                    │ RL-Sizing Agent  │
                    └────┬─────────────┘
                         │ sized netlist
                ┌────────▼─────────┐
                │  SPICE Exporter  │
                └────────┬─────────┘
                         │ .cir file
            ┌────────────▼────────────┐
            │  PySpice Simulator (µ)  │
            └────────────┬────────────┘
                         │ metrics / waveforms
```

*∆ = custom LLM architecture described in `models/analog_llm_architecture.md`  
*µ = optional on-prem or cloud NGSpice service

## Key Features
- 📈 **gm/Id Solver** – fast lookup of transistor operating points across technology nodes  
- 🧠 **Topology LLM** – domain-specific language model that drafts new schematic fragments  
- 🎯 **RL Sizing Agent** – policy network that tweaks device widths/lengths to close spec gaps  
- 🛠 **SPICE Exporter** – clean NGSpice netlist generation with simulation hooks  
- 📊 **Experiments Suite** – notebooks + CSVs to track progress across reference designs  

## What's Working Now
* **gm/Id Solver** loads sweep data and interpolates transistor operating points  
* **Topology Generator** returns mocked netlist fragments for rapid UI demo  
* **RL Sizing Agent** skeleton compiles & logs to TensorBoard  
* **SPICE Exporter** emits valid NGSpice netlists and unit tests pass  

## Dataset: gm/Id Reference Library
Our **gm/Id lookup tables** now ship *inside the repo* under `data/gmid_genai_dataset/`—no extra copying required. Each CSV is a short sweep exported from Spectre/NGSpice and begins with a `waveVsWave(...)` header followed by numeric columns (e.g., `gm_id`, `vov`, `id_by_w`).

* **Technology nodes:** 180 nm, 65 nm, 16 nm (scalable – drop new CSVs in the same folder).  
* **Units:** gm/Id in V⁻¹, V
overdrive in V, Id/W in A/µm.  
* **Usage:** `GmIdSolver` automatically discovers the files; call `solver(gm_id_target)` to get `(Vov, Id/W)`.

> Want to support additional corners (SS/FF, -40 °C, 125 °C)? Run your own sweeps and copy the CSVs here—no code changes required.

## Front-End Interface
The full React/Vite application has been vendored into `frontend/Interface/`. A concise README in that folder provides developer commands & architecture notes; think of it as *module-level* documentation rather than fragmentation.

| UI Panel | Purpose |
|----------|---------|
| Prompt Input | Enter plain-English specs and send to backend |
| LLM Config   | Switch between OpenAI, Claude, or local Llama endpoints |
| Circuit Visualisation | Render schematic graph + simulated waveforms |
| Export / Stats | Download netlist, view metric tables, leaderboard |

### Local Dev
```bash
cd frontend/Interface
bun install    # or npm install
bun run dev    # Vite dev server at http://localhost:5173
```

### Why Separate READMEs?
Each major module (`frontend`, `data`, `docs`) owns its own README **so contributors can jump straight into the part they care about** without scrolling through one mega-file. The top-level README (this file) remains the canonical overview; sub-READMEs are deep dives and keep the repo organised, not cluttered.

## Repository Layout
```text
Analog-GPT/
├── data/               # gm/Id CSV sweeps (copy or symlink here)
├── docs/               # Methodology & roadmap
├── experiments/        # Validation CSVs & raw data
├── frontend/           # React + Vite UI (submodule/pointer)
├── models/             # Model configs & architecture notes
├── notebooks/          # Interactive demos & analysis
├── src/                # Core Python packages
│   ├── gm_id_solver/
│   ├── topology_generator/
│   ├── sizing_optimizer/
│   └── netlist_generator/
├── requirements.txt    # Python dependencies
└── README.md           # You are here
```

## Getting Started
1. **Clone & Install**  
   ```bash
   git clone https://github.com/your-org/Analog-GPT.git
   cd Analog-GPT
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Run gm/Id Demo**  
   ```bash
   python -m src.gm_id_solver.solver  # quick CLI test
   ```
3. **Jupyter Notebooks**  
   ```bash
   jupyter lab notebooks/gm_id_solver.ipynb
   ```

## Next Milestones
1. Fine-tune LLM on internal schematic corpus  
2. Integrate RL reward shaping with simulation metrics  
3. Deploy on a GPU-enabled cloud runner with REST + WebSocket streaming  
4. Publish benchmark results versus state-of-the-art analog design flows  

## Tech Stack
| Layer         | Package / Tool |
|---------------|----------------|
| Data & Viz    | NumPy, Pandas, Matplotlib, Jupyter |
| ML / RL       | PyTorch, Transformers, Stable-Baselines3 |
| EDA           | PySpice, NGSpice |
| Backend       | FastAPI (planned), Docker |
| Front-end     | React + Vite UI (see `Interface/` prototype) |

_This repo is **work-in-progress**. We welcome collaborators!_ 
