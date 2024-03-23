def find_largest(arr):
    if not arr:  # Check if array is empty
        return None

    max_element = arr[0]  # Initialize max_element with the first element of the array

    for num in arr:
        if num > max_element:
            max_element = num

    return max_element

# Test the function
array = [int(x) for x in input("Enter elements of the array separated by space: ").split()]
largest = find_largest(array)
if largest is not None:
    print("The largest element in the array is:", largest)
else:
    print("The array is empty.")
