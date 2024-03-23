def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

# Test the function
arr = [int(x) for x in input("Enter the array elements separated by space: ").split()]
print("Original array:", arr)
selection_sort(arr)
print("Array after selection sort:", arr)
