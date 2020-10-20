# Longest Common Subsequence

The longest common subsequence problem is finding the longest sequence 
which exists in both the given strings.

Subsequence
Let us consider a sequence S = <s1, s2, s3, s4, …,sn>.

A sequence Z = <z1, z2, z3, z4, …,zm> over S is called a subsequence of S, 
if and only if it can be derived from S deletion of some elements.

Common Subsequence
Suppose, X and Y are two sequences over a finite set of elements. 
We can say that Z is a common subsequence of X and Y, if Z is a subsequence of both X and Y.

Longest Common Subsequence
If a set of sequences are given, the longest common subsequence problem is to 
find a common subsequence of all the sequences that is of maximal length.

The longest common subsequence problem is a classic computer science problem, 
the basis of data comparison programs such as the diff-utility, and has applications 
in bioinformatics. It is also widely used by revision control systems, such as SVN 
and Git, for reconciling multiple changes made to a revision-controlled collection of files.

Naïve Method
Let X be a sequence of length m and Y a sequence of length n. Check for every subsequence 
of X whether it is a subsequence of Y, and return the longest common subsequence found.

There are 2m subsequences of X. Testing sequences whether or not it is a subsequence of Y 
takes O(n) time. Thus, the naïve algorithm would take O(n2m) time.

Dynamic Programming
Let X = < x1, x2, x3,…, xm > and Y = < y1, y2, y3,…, yn > be the sequences. 
To compute the length of an element the following algorithm is used.

In this procedure, table C[m, n] is computed in row major order and 
another table B[m,n] is computed to construct optimal solution.

# Example
In this example, we have two strings X = BACDB and Y = BDCB to find the longest common subsequence.

Following the algorithm LCS-Length-Table-Formulation (as stated above), we have calculated table C 
(shown on the left hand side) and table B (shown on the right hand side).

In table B, we are using ‘D’, ‘L’ and ‘U’ for diagonal, left and up
respectively. After generating table B, the LCS is determined by function LCS-Print. The result is BCB.

As can be seen in the image below on the left, we are recurring from bottom to top to get the desired subsequence

![alt text](https://www.tutorialspoint.com/design_and_analysis_of_algorithms/images/lcs.jpg)
