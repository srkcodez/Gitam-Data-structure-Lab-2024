def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Example usage:
array = [5, 3, 8, 6, 7]
target = 8

result = linear_search(array, target)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found.")
