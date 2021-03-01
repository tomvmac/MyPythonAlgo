# Bubble Sort

# General algo is to iterate through the array and compare the current item to the next item,
# if current item is larger than swap
# continue until both loops are completed

# Time - O(n^2)
# Space - O(n)

def bubbleSort(array):
    temp = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if (array[i] > array[j]):
                # swap
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
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