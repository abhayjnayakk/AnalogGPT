"""
gm/Id Solver
============

Loads gm/Id sweep CSV files and provides interpolation utilities
to obtain transistor operating points for a given technology node.

Author: Your Name
"""

from pathlib import Path
from typing import Tuple
import pandas as pd
import numpy as np

# Directory containing gm/Id CSV sweeps (copied or symlinked).
# Priority: project-local data/ folder → workspace-level folder.
PROJECT_DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "gmid_genai_dataset"
FALLBACK_DATA_DIR = Path(__file__).resolve().parents[2] / "gmid_genai_dataset"

DATA_DIR = PROJECT_DATA_DIR if PROJECT_DATA_DIR.exists() else FALLBACK_DATA_DIR


class GmIdSolver:
    """Lightweight gm/Id lookup based on pre-simulated sweeps."""

    def __init__(self, tech_node: str = "65nm"):
        self.tech_node = tech_node
        self._db = self._load_all()

    def _load_all(self) -> dict:
        db = {}
        for csv in DATA_DIR.glob("*.csv"):
            # Example filename: "gm_id vs vov.csv"
            key = csv.stem.lower().replace(" ", "_")
            df = pd.read_csv(csv, comment="w")  # Skip long 'waveVsWave...' header lines
            df.columns = [c.lower().replace("/", "_") for c in df.columns]
            db[key] = df
        return db

    def query(self, gm_over_id: float) -> Tuple[float, float]:
        """Return (V_ov, Id/W) for the nearest gm/Id value."""
        table = self._db.get("gm_id_vs_vov")
        if table is None:
            raise ValueError("gm_id_vs_vov sweep not loaded.")

        idx = (table["gm_id"] - gm_over_id).abs().idxmin()
        row = table.iloc[idx]
        return float(row["vov"]), float(row["id_by_w"])

    # Convenience alias
    __call__ = query


if __name__ == "__main__":
    solver = GmIdSolver()
    vov, id_w = solver(15)
    print(f"gm/Id=15 → Vov={vov:.3f} V, Id/W={id_w:.3e} A/µm") 