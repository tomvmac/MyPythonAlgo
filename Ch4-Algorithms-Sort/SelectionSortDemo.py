# Selection Sort


# General Strategy:
#
# Compare and swap the smaller number to the beginning.
#

# 1. First set a Spot Marker or index
# 2. Loop
# 3. Compare the current value at current position to the spot marker to check for less
# 4. If number is less than marker, then swap

# Implementation
# 2 Loops - O(n^2)

def selection_sort(arr):
    print(arr)
    spot_marker = 0
    print(spot_marker)
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
        print(arr)

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
selection_sort(l)