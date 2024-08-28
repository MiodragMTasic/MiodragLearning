"""
Decision Tree Module

This module provides functions for creating and analyzing decision trees.

Author: Miodrag Tasic
Date: 2024-08-28
"""

import pandas as pd
import numpy as np

def calculateEntropyOfConceptColumn(data: list, column: int) -> float:
    """
    Calculate the entropy of a specific column in the data.

    Args:
        data (list): List of data rows.
        column (int): Index of the column to calculate entropy for.

    Returns:
        float: Calculated entropy.
    """
    finalColumn = [row[column] for row in data]
    allValues = []
    valueCounts = []
    
    for value in finalColumn[1:]:
        if value not in allValues:
            allValues.append(value)
            valueCounts.append(1)
        else:
            valueCounts[allValues.index(value)] += 1

    return entropyCalculateWithOccurances(valueCounts)

def entropyCalculateWithOccurances(valueCounts: list) -> float:
    """
    Calculate entropy based on value occurrences.

    Args:
        valueCounts (list): List of value counts.

    Returns:
        float: Calculated entropy.
    """
    entropy = 0
    total = sum(valueCounts)
    
    for i in valueCounts:
        p = i / total
        entropy += -p * np.log2(p)

    return entropy

def id3GreedyAlgorithm(data: list) -> str:
    """
    Implement the ID3 Greedy Algorithm for decision tree creation.

    Args:
        data (list): List of data rows including headers.

    Returns:
        str: String representation of the decision tree.
    """
    # Remove row numbers
    for row in data:
        del row[0]

    treeStructure = []

    while len(data[0]) > 2:
        columnToRemove, maxInfoGain, allBranches = maxColumnInfoGain(data)
        
        removeThisBranchAndItsIndex = findHighestEntropyBranchBetter(allBranches)
        
        onlyEntropyEqualZeroes = returnOnlyEntropyEqualZeroes(allBranches, removeThisBranchAndItsIndex[0], len(data[0]))
        
        if len(data[0]) > 3:
            endString = "----------->"
            for value in onlyEntropyEqualZeroes:
                concept = getConceptForValue(data, columnToRemove, value)
                endString += f"({value}={concept})"
            
            treeStructure.append((data[0][columnToRemove]).upper() + endString)
            treeStructure.append(" |")
            treeStructure.append(" |" + "(" + removeThisBranchAndItsIndex[0] + ")")
            treeStructure.append(" |")
            treeStructure.append(" V")
        else:
            endString = "----------->"
            for value in onlyEntropyEqualZeroes:
                concept = getConceptForValue(data, columnToRemove, value)
                endString += f"({value}={concept})"
            
            treeStructure.append((data[0][columnToRemove]).upper() + endString)

        data = [row for row in data if row[removeThisBranchAndItsIndex[1]] != removeThisBranchAndItsIndex[0]]
        
        for row in data:
            del row[columnToRemove]

    return "\n".join(treeStructure)

# Helper functions (maxColumnInfoGain, findHighestEntropyBranchBetter, etc.) should be implemented here
