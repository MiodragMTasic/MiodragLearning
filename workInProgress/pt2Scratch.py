# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:47:18 2024

@author: Miodrag Tasic
"""

import math

def main():
    question1(table)

table = [
    ['x1','x2','x3','y'],
    
    [1,1,1,'+'],
    [0,0,1,'+'],
    [0,1,1,'+'],
    [0,1,0,'+'],
    [1,0,0,'-']
]

def booleanOfInteger(x):
    if (x==1):
        return True
    else:
        return Talse

def question1(table):
    tempTable = table
    del tempTable[0]
    
    numberOfFeatures = len(tempTable[0])-1
    for feature in range(numberOfFeatures -1):
        for feature2 in range(numberOfFeatures*2):
            print('f1: ', feature)

if __name__ == "__main__":
    main()

all = [0,1,2]
allExpanded = []
for i in range(len(all)):
    for x in range(len(all)*2 +2):
        allExpanded.append(i)

for i in range(int(len(allExpanded)/2)):
    print(allExpanded[i]," ", allExpanded[i+(int(len(allExpanded)/2))])

'''
01
01
01
01
02
02
02
02
12
12
12
12'''