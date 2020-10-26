#Algorithm to solve the problem: Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target 
#runtime of algorightm is O(n)  and space complexity is O(n) where n is size of nums array
def twoSum(nums, target):
    map_values = dict()
    #populate the dictionary with the array value as the key and it's index as the value
    for index in range(len(nums)):
        map_values[nums[index]] = index
        #search for the match by using the current value's complement in the dictionary
        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in map_values.keys() and map_values.get(complement) != index:
                results = [index, map_values.get(complement)]
                return results
    raise ValueError("No two sum solution")
    
def main():
    nums = [2,7,11,15]
    target = 9
    print(twoSum(nums, target))


if __name__ == "__main__":
    print("indices of values that add up to the target value ===")
    main()
        
        