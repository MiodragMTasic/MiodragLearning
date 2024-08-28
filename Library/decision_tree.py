"""
Decision Tree Module

This module provides functions for creating and analyzing decision trees.

Author: Miodrag Tasic
Date: 2024-08-28
"""

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

def maxColumnInfoGain(data: list) -> tuple:
    """
    Calculate the maximum information gain for all columns in the data.

    Args:
        data (list): List of data rows including headers.

    Returns:
        tuple: (column to remove, max info gain, all branches for that column)
    """
    initialEntropy = calculateEntropyOfConceptColumn(data, len(data[0])-1)
    allBranchesInfoGains = []
    allColumnsBranchesGROUPED = []
    
    for z in range(len(data[0])-1):
        allBranches = []
        for i in data[1:]:
            sublist = [i[z]]
            if sublist not in allBranches:
                allBranches.append(sublist)
                
        for row in data[1:]:
            branchValue = row[z]
            conceptValue = row[-1]
            
            for branch in allBranches:
                if branch[0] == branchValue:
                    branch.append(conceptValue)
                    break
        
        allColumnsBranchesGROUPED.append(allBranches)
        
        totalColumnEntropy = 0
        
        for i in range(len(allBranches)):
            allValues = []
            valueCounts = []
            for value in allBranches[i][1:]:
                if value not in allValues:
                    allValues.append(value)
                    valueCounts.append(1)
                else:
                    valueCounts[allValues.index(value)] += 1
            
            totalColumnEntropy += entropyCalculateWithOccurances(valueCounts) * sum(valueCounts)*0.1
            
        allBranchesInfoGains.append((initialEntropy-totalColumnEntropy))
        
    maxInfoGain = max(allBranchesInfoGains)
    columnToRemove = allBranchesInfoGains.index(maxInfoGain)
    return columnToRemove, maxInfoGain, allColumnsBranchesGROUPED[columnToRemove]

def findHighestEntropyBranchBetter(allBranches: list) -> list:
    """
    Find the branch with the highest entropy.

    Args:
        allBranches (list): List of all branches.

    Returns:
        list: Information about the branch with highest entropy.
    """
    returnList = [0,0,0,0]
    totalColumnEntropy = 0
    oneToRemove = 0
    oneToContinueFrom = 0
    
    for i in range(len(allBranches)):
        minValue = 1.01
        maxValue = 0
        
        allValues = []
        valueCounts = []
        for value in allBranches[i][1:]:
            if value not in allValues:
                allValues.append(value)
                valueCounts.append(1)
            else:
                valueCounts[allValues.index(value)] += 1
        
        branchEntropy = entropyCalculateWithOccurances(valueCounts) * sum(valueCounts)*0.1
        totalColumnEntropy += branchEntropy
        
        if maxValue < branchEntropy:
            oneToRemove = i
            maxValue = branchEntropy
        if minValue > branchEntropy:
            oneToContinueFrom = i
            minValue = branchEntropy
            
    returnList[0] = allBranches[oneToRemove][0]
    returnList[1] = oneToRemove
    returnList[2] = allBranches[oneToContinueFrom]
    returnList[3] = oneToContinueFrom
    
    return returnList

def returnOnlyEntropyEqualZeroes(list: list, x: str, z: int) -> list:
    """
    Return a list of values with zero entropy, excluding a specific value.

    Args:
        list (list): List of branches.
        x (str): Value to exclude.
        z (int): Length of data row.

    Returns:
        list: List of values with zero entropy.
    """
    returnList = []
    for i in range(len(list)):
        returnList.append(list[i][0])
    if (z > 3):
        returnList.remove(x)
    return returnList

def getConceptForValue(data: list, column: int, value: str) -> str:
    """
    Get the concept class for a specific value in a column.

    Args:
        data (list): List of data rows.
        column (int): Index of the column.
        value (str): Value to find the concept for.

    Returns:
        str: Concept class for the given value.
    """
    for row in data[1:]:
        if row[column] == value:
            return row[-1].lower()
    return " "