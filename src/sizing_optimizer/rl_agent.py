"""
Reinforcement-Learning Agent for transistor sizing.

Currently a skeleton that logs random actions; to be swapped with
Stable-Baselines3 PPO.
"""

from __future__ import annotations
import logging
import random
from typing import Dict, Any, List

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class SizingRLAgent:
    def __init__(self, action_space: List[float] | None = None):
        self.action_space = action_space or [0.5, 1.0, 2.0, 4.0]

    def act(self, state: Dict[str, Any]) -> float:
        """Pick a width multiplier given the current state."""
        choice = random.choice(self.action_space)
        logger.info("Agent selected scale×=%.2f for node=%s", choice, state.get("node", "?"))
        return choice

    def train(self, episodes: int = 10):
        """Mock training loop."""
        for ep in range(episodes):
            reward = random.random()
            logger.debug("Episode %d → reward %.3f", ep, reward)
        logger.info("Finished mock training.") 