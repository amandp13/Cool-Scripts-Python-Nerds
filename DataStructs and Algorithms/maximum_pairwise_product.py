def maxPairwiseProduct(n,numbers):
    nums=numbers.split()
    lst=[]
    for num in range(n):
        lst.append(int(nums[num]))
    lst.sort(reverse=True)
    return lst[0]*lst[1]
while True:
    n=int(input())
    numbers=input()
    if numbers=='done':
        break
    print(maxPairwiseProduct(n,numbers))
