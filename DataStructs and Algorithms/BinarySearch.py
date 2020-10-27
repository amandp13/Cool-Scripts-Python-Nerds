def binary_search(arr, low, high, x): 
    if high >= low: 
  
        mid = (high + low) // 2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
  
        else: 
            return binary_search(arr, mid + 1, high, x) 
  
    else: 
        return -1
n = int(input("enter number of elements"))
a=[]
print("enter elements in array")
for i in range(n):
   e=int(input())
   a.append(e)
x = int(input("enter element to be searched"))


result = binary_search(a, 0, len(a)-1, x) 
  
if result != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array") 