print("Algorithms files loaded")

# Includes all the functions for all sorting algorthims

# Quick Sort
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

# Merge Sort
def merged_sorted(arr1, arr2):
    # print("Merge function called with lists below:")
    # print(f"left: {arr1} and right: {arr2}")
    sorted_arr = []
    i, j = 0,0

    while i < len(arr1) and j < len(arr2):
        # print(f"Left list index i is {i} and has value: {arr1[i]}")
        # print(f"Right list index j is {j} and has value: {arr2[j]}")

        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i +=1
        else:
            sorted_arr.append(arr2[j])
            j +=1
        # print(sorted_arr)

    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1

    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1

    return sorted_arr



def mergesort(arr):
    if len(arr) < 2:
        # print(f"Base condition reached with {arr[:]}")
        return arr[:]
    else:
        middle = len(arr) // 2
        # print("Current list to work with:", arr)
        # print("Left split:", arr[:middle])
        # print("Right split:", arr[middle:])
        l1 = mergesort(arr[:middle])
        l2 = mergesort(arr[middle:])
        # merge
        return merged_sorted(l1, l2)


# Bubble Sort

def bubblesort(arr):
    # Potential solutions
    # 1. Nested for loops, but this is not most efficient because the list could be sorted already and still
    #     iterating  o n^2
    # 2. Optimized solution is to use a flag to sign swap occured,

    swap_happened = True

    while swap_happened:
        # print('bubble sort status: ' + str(arr))
        # init swap_happened to False
        swap_happened = False
        # loop through list
        for num in range(len(arr)-1):
            if (arr[num] > arr [num +1]):
                # swap using python array dynamic assignment
                swap_happened = True
                # print("Swap happend")
                arr[num], arr[num+1] = arr[num+1], arr[num]
                # print(arr)


# Insertion Sort

def insertionsort(arr):
    # print(arr)
    spot_marker = 1
    # print(spot_marker)
    temp_num = 0

    while spot_marker < len(arr):
        # compare current to prior
        if arr[spot_marker] < arr[spot_marker-1]:
            # swap
            # temp variable
            temp_num = arr[spot_marker]
            arr[spot_marker] = arr[spot_marker-1]
            arr[spot_marker-1] = temp_num
            # loop from spot_marker-1 to beginning of arr and compare each one
            # if prior is smaller, then swap
            for num in range(spot_marker-1, 0, -1):
                if arr[num] < arr[num-1]:
                    # swap
                    temp_num1 = arr[num]
                    arr[num] = arr[num-1]
                    arr[num-1] = temp_num1
        spot_marker += 1
        # print(arr)


# Selection Sort
def selectionsort(arr):
    # print(arr)
    spot_marker = 0
    # print(spot_marker)
    temp_num = 0

    while spot_marker < len(arr):
        for num in range(spot_marker, len(arr)):
            if arr[num] < arr[spot_marker]:
                # dynamic array assignment
                #arr[spot_marker], arr[num] = arr[num], arr[spot_marker]

                # temp variable
                temp_num = arr[spot_marker]
                arr[spot_marker] = arr[num]
                arr[num] = temp_num
        spot_marker += 1
        # print(arr)
