"""
Probability Bounds Module

This module provides functions for calculating various probability bounds,
including Markov's inequality, Chebyshev's inequality, and Chernoff bound.

Author: Miodrag Tasic
Date: 2024-08-28
"""

import numpy as np

def calculate_epsilon(X: float, a: float) -> float:
    """
    Calculate epsilon for use in probability bounds.

    Args:
        X (float): Expected value.
        a (float): Threshold value.

    Returns:
        float: Calculated epsilon value.
    """
    return (a - X) / X

def markov_inequality_upperbound(X: float, a: float) -> float:
    """
    Calculate the upper bound using Markov's inequality for P(X >= a).

    Args:
        X (float): Expected value.
        a (float): Threshold value.

    Returns:
        float: Upper bound probability.
    """
    return X / a

def chebyshev_inequality_upperbound(X: float, a: float, n: int) -> float:
    """
    Calculate the upper bound using Chebyshev's inequality for P(X >= a), where a > 2X.

    Args:
        X (float): Expected value.
        a (float): Threshold value.
        n (int): Number of trials.

    Returns:
        float: Upper bound probability.
    """
    return (X * (1 - X)) / (n * np.square(a - X))

def chernoff_inequality_upperbound(X: float, a: float, n: int) -> float:
    """
    Calculate the upper bound using Chernoff bound for P(X >= a), where a > 2X.

    Args:
        X (float): Expected value.
        a (float): Threshold value.
        n (int): Number of trials.

    Returns:
        float: Upper bound probability.
    """
    epsilon = calculate_epsilon(X, a)
    exponent_value = (-1) * (np.square(a - X)) / (2 * (X + epsilon) * X) * n
    return np.exp(exponent_value)
