# Dataset: gm/Id Sweeps & Reference Curves

This folder is intended to hold **technology-specific lookup tables** used by the `gm_id_solver` package.  

The original CSVs (≈53 lines each) live in the workspace directory `gmid_genai_dataset/`. For portability we recommend copying or symlinking them here:

```bash
# Inside Analog-GPT/
mkdir -p data/gmid_genai_dataset
cp -r ../../gmid_genai_dataset/*.csv data/gmid_genai_dataset/
```

Once the files are present, the solver will automatically detect them.

| File | Contents |
|------|----------|
| `gm_id vs vov.csv` | gm/Id versus overdrive voltage |
| `ft vs vov.csv`    | Transit frequency versus VOV |
| … | … |

> **Tip:** Use Jupyter notebook `notebooks/gm_id_solver.ipynb` to visualise and sanity-check the curves. 