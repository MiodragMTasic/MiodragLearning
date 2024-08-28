"""
Entropy Module

This module provides functions for calculating entropy in various scenarios.

Author: Miodrag Tasic
Date: 2024-08-28
"""

import numpy as np
import sympy as sp

def entropyDice(tuplesOfChanceAsFractions: list) -> float:
    """
    Calculate the entropy of a die with given probabilities.

    Args:
        tuplesOfChanceAsFractions (list): List of probabilities for each face of the die.

    Returns:
        float: Calculated entropy.
    """
    totalValue = 0
    for x in tuplesOfChanceAsFractions:
        totalValue += x * np.log2(1/x)
    return totalValue

def compareEntropies(a: float, b: float, precision: int) -> str:
    """
    Compare two entropy values and return a formatted string.

    Args:
        a (float): First entropy value.
        b (float): Second entropy value.
        precision (int): Number of decimal places for the result.

    Returns:
        str: Formatted comparison string.
    """
    difference = abs(a - b)
    if a > b:
        return f"A's entropy is {difference:.{precision}f} more than B's entropy."
    elif b > a:
        return f"B's entropy is {difference:.{precision}f} more than A's entropy."
    else:
        return "A and B have the same entropy."

def entropyOfSpecificValueForFairDice(numSides: int) -> float:
    """
    Calculate the entropy of a specific value for a fair die.

    Args:
        numSides (int): Number of sides on the die.

    Returns:
        float: Calculated entropy.
    """
    varToNotLand = numSides - 1
    varToLand = numSides - varToNotLand
    
    i = sp.symbols('i', integer=True)
    a = sp.Rational(varToNotLand, numSides)
    b = sp.Rational(varToLand, numSides)
    
    term = (a**(i-1) * b) * sp.log((1/(a**(i-1) * b)), 2)

    return sp.summation(term, (i, 1, sp.oo)).evalf()