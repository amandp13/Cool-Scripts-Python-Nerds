'''
Given an array of distinct integers.The task is to count all triplets
such that the sum of two elements equals the third element. 

Constrains:
1<= T <=100
3<= N <= 10pow(5)
1<= A[i] <= 10pow(6)
'''

def triplet(i,a):
    count = 0
    for x in range(i):
        for y in range(x+1,i):
            if a[x]+a[y] in a:
                count +=1
                #print(a[x],a[y])  # debug

    if count:
        return count
    return "-1"


n = int(input('Enter no of times to run [T] : '))
while n:
    i = int(input('Enter Array Length [N] : '))
    # Array input format '1 3 4 5 ...'
    a = [int(d) for d in input().split()]
    print(triplet(i, a))
    n -= 1
