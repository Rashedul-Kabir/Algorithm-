def counting_sort(arr):
    """Sorts an array of non-negative integers using counting sort algorithm.

    Args:
        arr (list of int): The list of non-negative integers to be sorted.

    Returns:
        list of int: The sorted list of integers.
    """
    if not arr:
        return []

    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i, cnt in enumerate(count):
        sorted_arr.extend([i] * cnt)

    return sorted_arr


# Example usage
nums = [4, 2, 2, 8, 3, 3, 1]
print("Original:", nums)                
sorted_nums = counting_sort(nums)
print("Sorted:", sorted_nums)       


"""

    Sorts an array using the counting sort algorithm.
    Parameters:
    arr (list): The list of non-negative integers to be sorted.
    Returns:
    list: The sorted list.

    """
