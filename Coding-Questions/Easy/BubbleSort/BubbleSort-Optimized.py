# Bubble Sort

# General algo is to iterate through the array using while loop and compare the current item to the next item,
# if current item is larger than swap
# continue until the swapped flag is no longer True

# Main difference is if part of the array is already sorted, then no swap will occur and the execution can terminate earlier

# Time - O(n)
# Space - O(n)

def bubbleSort(array):
    swapped = True
    temp = 0

    while swapped:
        swapped = False

        # loop
        for i in range(len(array)-1):
            if (array[i] > array[i+1]):
                # swap
                swapped = True
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp

    return array


# Driver Code

# input array
array = [8, 5, 2, 9, 5, 6, 3]

print("original array: ", array)

# expected output array
expectedArray = [2, 3, 5, 5, 6, 8, 9]
print("expected array: ", expectedArray)

actualArray = bubbleSort(array)
print("actual array: ", actualArray)