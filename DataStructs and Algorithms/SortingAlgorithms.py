def selectionSort(input_array):
    # Traverse through all array elements 
    for i in range(len(input_array)):

        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i 
        for j in range(i+1, len(input_array)): 
            if input_array[min_idx] > input_array[j]: 
                min_idx = j 

        # Swap the found minimum element with  
        # the first element  
        temp = input_array[i]
        input_array[i] = input_array[min_idx] 
        input_array[min_idx] = temp
    
    return input_array

def insertionSort(input_array):
    # Traverse through 1 to len(input_array) 
    for i in range(1, len(input_array)): 
  
        key = input_array[i] 
  
        # Move elements of input_array[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < input_array[j] : 
                input_array[j + 1] = input_array[j] 
                j -= 1
        input_array[j + 1] = key
        
    return input_array

def mergeSort(input_array):
    if len(input_array) > 1:
         # Finding the mid of the array
        mid = len(input_array)//2
        # Dividing the array elements
        L = input_array[:mid]
        # into 2 halves
        R = input_array[mid:]
        # Sorting the first half
        mergeSort(L)
        # Sorting the second half
        mergeSort(R)
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                input_array[k] = L[i]
                i += 1
            else:
                input_array[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(L):
            input_array[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            input_array[k] = R[j]
            j += 1
            k += 1

        return input_array

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# input_array[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(input_array,low,high): 
    if low < high: 
  
        # pi is partitioning index, input_array[p] is now 
        # at right place 
        pi = partition(input_array,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(input_array, low, pi-1) 
        quickSort(input_array, pi+1, high)

        return input_array

if __name__ == '__main__':
    test_array = [2, 7, 1, 7, 45, 23, 67, 2, 7, 8]
    print(selectionSort(test_array))
    print(insertionSort(test_array))
    print(mergeSort(test_array))
    n = len(test_array)
    print(quickSort(test_array, 0, n-1))
