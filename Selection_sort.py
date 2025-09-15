def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


nums = [12, 11, 13, 5, 6]
print("Original:", nums)
sorted_nums = selection_sort(nums)
print("Sorted:", sorted_nums)