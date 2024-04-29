def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val < target:
            low = mid + 1
        elif mid_val > target:
            high = mid - 1
        else:
            return mid  # Return the index of the target element

    return -1  # Return -1 if the target is not found


# Example usage:
sorted_array = [1, 2, 4, 5, 6, 8, 9]  # The array must be sorted for binary search
target = 5

result = binary_search(sorted_array, target)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found.")
