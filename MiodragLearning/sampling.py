"""
Sampling Module

This module provides functions for calculating sample sizes based on the sampling theorem.

Author: Miodrag Tasic
Date: 2024-08-28
"""

import numpy as np

def samplingTheorem(epsilon: float, confidence: float) -> float:
    """
    Calculate the required sample size based on the sampling theorem.

    Args:
        epsilon (float): Desired precision.
        confidence (float): Desired confidence level.

    Returns:
        float: Required sample size.
    """
    delta = 1 - confidence
    return ((2 + epsilon) / (np.square(epsilon))) * np.log(2/delta)