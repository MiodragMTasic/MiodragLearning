"""
SAT Problem Module

This module provides functions for calculating probabilities related to 3SAT problems.

Author: Miodrag Tasic
Date: 2024-08-28
"""

import numpy as np

def satisfying3SATProblem(atLeast: int, atMost: int, satisfyingChance: float) -> float:
    """
    Calculate the probability of satisfying a 3SAT problem.

    Args:
        atLeast (int): Minimum number of satisfying assignments.
        atMost (int): Maximum number of satisfying assignments.
        satisfyingChance (float): Probability of a single assignment being satisfying.

    Returns:
        float: Probability of satisfying the 3SAT problem.
    """
    chance = (100 - satisfyingChance) / 100
    return np.power(chance, atLeast) - np.power(chance, atMost)