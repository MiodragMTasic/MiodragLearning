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
    
    conceptVariable = tempTable[0].pop(-1)
    
    featureVariables = tempTable[0]
    
    all = featureVariables
    allExpanded = []
    
    #x1,x2
    allSets = []
    #1,2 not x1,x2
    allSetsJustNumber = []
    setsThatWork = []
    
    numbers = []
    
    for i in range(len(all)):
        for x in range(len(all)*2 +2):
            allExpanded.append(all[i])

    for i in range(int(len(allExpanded)/2)):
        allSets.append([allExpanded[i],allExpanded[i+(int(len(allExpanded)/2))]])
        #print(allExpanded[i],"V", allExpanded[i+(int(len(allExpanded)/2))])
        
    #allSets becomes all sets of x but just integer so: ['x1', 'x2'] -> [1,2]
    for x in allSets:

        numbers = [int(z[1:]) for z in x]
        allSetsJustNumber.append(numbers)
    
    #print(allSets)
    for i in range(1,len(table)):
        print('table[i]', table[i])
        conceptVariable = table[i][len(table[i])-1]
        print('conceptVariable', conceptVariable)
        print("i: ", i)
        print(allSetsJustNumber)
        print('allSetsJustNumber[i-1]', allSetsJustNumber[i-1])
        print('allSetsJustNumber[i-1][0]', allSetsJustNumber[i-1][0])
        print('allSetsJustNumber[i-1][1]', allSetsJustNumber[i-1][1])
        print('table[i][allSetsJustNumber[i-1][0]', table[i][allSetsJustNumber[i-1][0]])
        print('table[i][allSetsJustNumber[i-1][1]', table[i][allSetsJustNumber[i-1][1]])
        
        print('conceptVariable: ', conceptVariable)
        
        #nothing
        if (i-1%4 == 0):
            print('allSetsJustNumber[i-1][0] or allSetsJustNumber[i-1][1]) == conceptVariable',(allSetsJustNumber[i-1][0] or allSetsJustNumber[i-1][1]) == conceptVariable)
            
        #left not, right nothing
        elif (i-1%4 == 1):
            print('!, ',(not(allSetsJustNumber[i-1][0]) or allSetsJustNumber[i-1][1]) == conceptVariable)
            
        #right not, left nothing
        elif (i-1%4 == 2):
            print(' ,!', (allSetsJustNumber[i-1][0] or not(allSetsJustNumber[i-1][1])) == conceptVariable)
            
        #both not
        elif (i-1%4 == 3):
            print('!,!',(not(allSetsJustNumber[i-1][0]) or not(allSetsJustNumber[i-1][1])) == conceptVariable)
                
        print('\n')
        #print(allSetsJustNumber)
        
        

if __name__ == "__main__":
    main()

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