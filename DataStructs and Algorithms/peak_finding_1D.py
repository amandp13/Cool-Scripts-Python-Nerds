#!/usr/bin/env
# Problem: Finding a 1D peak in given array if it exists. (Using Divide & Conquer)
# Complexity when "Divide & Conquer" method is used: O(log(n))

import math


def find_peak(given_array, starting_index, ending_index):
    # Using binary search (divide & conquer) to reduce complexity of the algorithm.
    mid = (starting_index + ending_index)//2
    if given_array[mid - 1] <= given_array[mid] >= given_array[mid + 1]:
        return given_array[mid]
    elif given_array[mid-1] > given_array[mid]:
        return find_peak(given_array, starting_index, mid - 1)
    elif given_array[mid + 1] > given_array[mid]:
        return find_peak(given_array, mid + 1, ending_index)


def main():
    given_array = [8, 2, 4, 6, 9, 3]
    array_length = len(given_array)  # Size of the given array.
    # Use of a sentinel value to avoid index error in case of strictly increasing or decreasing order.
    given_array.insert(0, -math.inf)
    given_array.append(-math.inf)

    # Call the function and show the result.
    result = find_peak(given_array, 1, array_length - 1)
    if result:
        print("A 1D peak is: ", result)
    else:   # This 'else' condition will never run as there exists a peak always in an 1D array.
        print("There is no 1D peak in the array.")


if __name__ == "__main__":
    main()
