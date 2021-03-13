# Move Element To End
# You're given an array of integers and an integer.  Write a function that moves all instances of that integer in the array to the end of the
# array and returns the array.

# The function should perform this in place (ie. it should mutate the input array_ and doesn't need to maintain the order of the other integers.


# General Strategy
# 1. Iterate through array
# 2. Compare each item with number to move
# 3. If equals, assign last element of array to current item


# Time: O(n)
# Space: O(1)

def moveElementToEnd(array, toMove):
    for index in range(len(array)):
        if array[index] == toMove:
            # shift
            for num in range(index, len(array)-1):
                if array[num] != toMove and array[num+1] != toMove:
                    array[num] = array[num+1]
            # assign last
            array[len(array)-1] = toMove
    return array



# Driver Code

array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

print(moveElementToEnd(array, toMove))

