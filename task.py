def find_pairs_for_target(array, target):
    # Convert the array to a set for quick lookup of the complement
    nums_set = set(array)
    pairs = []
    
    # Iterate over the array to find pairs
    for num in array:
        complement = target - num
        # Check if the complement exists in the set and is not the same element
        if complement in nums_set and complement != num:
            # Add the pair (num, complement) to the list
            pairs.append((num, complement))
            # Remove the pair from the set to avoid duplicate pairs
            nums_set.remove(num)
            nums_set.remove(complement)
    
    return pairs

# Taking user input for array and target
array_input = input("Enter the array of unique integers (comma-separated): ")
array = list(map(int, array_input.split(',')))

target = int(input("Enter the target sum: "))

# Calling the function with user input
pairs = find_pairs_for_target(array, target)

# Output the result
print(f"The pairs that sum to {target} are: {pairs}")
