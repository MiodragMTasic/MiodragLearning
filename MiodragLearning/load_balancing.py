"""
Load Balancing Module

This module provides functions for calculating probabilities related to random load balancing.

Author: Miodrag Tasic
Date: 2024-08-28
"""

import numpy as np

def random_load_balancing(numServers: int, numJobs: int, overloadCap: int) -> float:
    """
    Calculate the probability of overload in a random load balancing scenario.

    Args:
        numServers (int): Number of servers.
        numJobs (int): Number of jobs.
        overloadCap (int): Overload capacity threshold.

    Returns:
        float: Probability of overload.
    """
    epsilon = (overloadCap + 1 - numJobs/numServers) / (numJobs/numServers)
    exponentValue = (-1) * np.square(epsilon) / (2 + epsilon) * (numJobs/numServers)
    unionBound = numServers * np.exp(exponentValue)
    return unionBound