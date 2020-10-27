def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i+1
   return -1
n = int(input("enter number of elements"))
a=[]
print("enter elements in array")
for i in range(n):
   e=int(input())
   a.append(e)
x = int(input("enter element to be searched"))
print("element found at position "+str(linearsearch(a,x)))