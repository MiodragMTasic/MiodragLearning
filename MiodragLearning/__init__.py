"""
Probability Theory Library

This library provides various functions for probability theory and information theory calculations.

Modules:
    probability_bounds: Functions for calculating probability bounds
    load_balancing: Functions for random load balancing calculations
    sampling: Functions related to the sampling theorem
    sat_problem: Functions for 3SAT problem calculations
    entropy: Functions for entropy calculations
    decision_tree: Functions for decision tree algorithms

Author: Miodrag Tasic
Date: 2024-08-28
"""

from . import probability_bounds
from . import load_balancing
from . import sampling
from . import sat_problem
from . import entropy
from . import decision_tree

__all__ = ['probability_bounds', 'load_balancing', 'sampling', 'sat_problem', 'entropy', 'decision_tree']

# Version of the probability_theory_lib package
__version__ = "0.1.0"