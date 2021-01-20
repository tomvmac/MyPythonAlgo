# Insertion Sort

# General Strategy



# 1. Set the key to second element, Keep track of the key, compare to element prior
# 2. If condition for a swap is reached, keep track of the current item (working index) as it will be compared again to its prior element after the swap


# Big O - O(n^2)

def insertion_sort(arr):
    print(arr)
    spot_marker = 1
    print(spot_marker)
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
        print(arr)

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]

# for num in range(len(l), 0, -1):
#     print (num)

insertion_sort(l)