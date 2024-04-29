def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Pivot selection
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        # Recursively apply quick sort to left, middle, and right
        return quick_sort(left) + middle + quick_sort(right)

# Example usage:
array = [3, 6, 8, 10, 1, 2, 1]

print("Original array:")
print(array)

sorted_array = quick_sort(array)

print("Sorted array:")
print(sorted_array)
