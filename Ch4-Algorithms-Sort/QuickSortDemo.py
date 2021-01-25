# QuickSort

# Performance
# Best Case: O(nlog(n))
# Avg Case: O(nlog(n))
# Worst Case: O(n^2)

# General Strategy

# 1. Pick a pivot
# 2. Arrange all items smaller than pivot to the left of the pivot
# 3. Arrange all items larger than pivot to the right of the pivot
# 4. If there are equal items to the pivot, arrange them in the middle


def quicksort(arr):
    """
    Input: Unsorted list of integers
    Returns sorted list of integers using QuickSort
    Note: This is not an in-place implementation
    """

    # base case
    if len(arr) < 2:
        return arr
    else:
        # choose last element as the pivot
        pivot = arr[-1]
        smallerList, equalList, largerList = [], [], []

        for num in arr:
            if num < pivot:
                smallerList.append(num)
            elif num == pivot:
                equalList.append(num)
            else:
                largerList.append(num)
        return quicksort(smallerList) + equalList + quicksort(largerList)

    return arr


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
print(quicksort(l))

