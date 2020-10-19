"""
LCS: Given two string sequences find the longest common subsequence.
A subsequence is a sequence that occurs in both strings in the same
relative order but it need not be continuous.
For example: "xyz" and "wyz" are subsequences of "uvwxyz".
The code is case sensitive.
"""

import numpy as np
print("Enter 1st sequence")
first=input()
print("Enter 2nd sequence")
second=input()

seq=""

def lcs(first,second):
    
    global seq
    m=len(first)
    n=len(second)
    
    """
    In this procedure, table C[m, n] is computed in row major order
    and another table direction[m,n] is computed to construct optimal solution.
    """
    c=[[0 for i in range(n+1)] for j in range(m+1)]
    direction=[[0 for i in range(n+1)] for j in range(m+1)]
    """
    1st row and 1st column of c matrix initialized to 0 above.
    """
    
    for i in range(m):
        for j in range(n):
            """
            Comparing and updating direction and C matrices
            In direction matrix:
            D: Diagonal
            U: Up
            L: Left
            """
            if(first[i]==second[j]):
                c[i+1][j+1]=c[i][j]+1
                direction[i+1][j+1]="D"
                x,y=i+1,j+1
            elif(c[i][j+1]>=c[i+1][j]):
                c[i+1][j+1]=c[i][j+1]
                direction[i+1][j+1]="U"
            else:
                c[i+1][j+1]=c[i+1][j]
                direction[i+1][j+1]="L"

    """
    Calling print_lcs function to generate string from the matrices.
    """
    print_lcs(first,direction,x,y)
    print("longest Common Sequence=",seq)
    print("length=",len(seq))
    del seq

"""
Recursive function to follow the directions in
direction matrix and return the longest common sequence.
"""
def print_lcs(first,direction,i,j):
    global seq
    if(i==0 or j==0):
        return 
    """
    If 0th row or 0th column reached then return.
    """
    if(direction[i][j]=="D"):
        print_lcs(first,direction,i-1,j-1)
        seq=seq+first[i-1]
    elif(direction[i][j]=="U"):
        print_lcs(first,direction,i-1,j)
    else:
        print_lcs(first,direction,i,j-1)
        
lcs(first,second)        
