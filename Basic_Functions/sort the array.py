"""
Given an array A of size N containing 0s, 1s, and 2s;
you need to sort the array in ascending order.
"""

from time import time
from random import randint as ri


def printArray(a):
    for k in a:
        print(k, end=',')
    print('\n')


arr = [ri(0, 2) for x in range(16000)]
t1 = time()

def method1(a):
    arr_size = len(a)
    lo = 0
    hi = arr_size - 1
    mid = 0
    while mid <= hi:
        if a[mid] == 0:
            a[lo], a[mid] = a[mid], a[lo]
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        else:
            a[mid], a[hi] = a[hi], a[mid]
            hi = hi - 1
    return a

def method2(arr):
    arr.sort()
    return arr

def method3(arr):
    c0 = arr.count(0)
    c1 = arr.count(1)
    c2 = arr.count(2)
    sorarr = [0 for x in range(c0)]+[1 for x in range(c1)]+[2 for x in range(c2)]
    return sorarr

t1 = time()

m1 = method1(arr)
printArray(m1)

t2 = time()

m2 = method2(arr)
printArray(m2)

t3 = time()

m3 = method3(arr)
printArray(m3)

t4 = time()

print(f'\n---- Time Taken ----\n[method 1]: {t2-t1}\n[method 2]: {t3-t2}\n[method 3]: {t4-t3}\n--------------------')
