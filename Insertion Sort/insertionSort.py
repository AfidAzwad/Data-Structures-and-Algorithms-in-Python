def insertion_sort(arr):
    for i in range(1, len(arr)):  # O(n)
        current_value = arr[i]
        prev_index = i - 1

        # Shift elements of arr[0..i-1] that are greater than current_value
        while prev_index >= 0 and arr[prev_index] > current_value:  # O(i) in the worst case
            arr[prev_index + 1] = arr[prev_index]
            prev_index -= 1

        # Insert the current_value into its correct position
        arr[prev_index + 1] = current_value
    return arr

arr = [7,2,9,8,6,1,5,4,3]
print("Sorted List : ", insertion_sort(arr))

# Time Complexity:
# Outer loop runs (n - 1) times, where n = len(arr)
# Inner while loop runs in the worst case for all previous elements
# Best Case: O(n) (when the array is already sorted)
# Worst Case: O(n^2) (when the array is sorted in reverse order)
# Average Case: O(n^2)

# Space Complexity:
# Since sorting is done in-place, the space complexity is O(1)