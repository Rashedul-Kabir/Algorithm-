def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)




nums = [12, 11, 13, 5, 6]
print("Original:", nums)
sorted_nums = quick_sort(nums)
print("Sorted:", sorted_nums)









