def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track whether a swap was made during this pass
        swapped = False
        # Last i elements are already sorted, so the inner loop can avoid looking at the last i elements
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break

# Example usage:
array = [64, 34, 25, 12, 22, 11, 90]

print("Original array:")
print(array)

bubble_sort(array)

print("Sorted array:")
print(array)
