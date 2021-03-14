# Move Element To End
# You're given an array of integers and an integer.  Write a function that moves all instances of that integer in the array to the end of the
# array and returns the array.

# The function should perform this in place (ie. it should mutate the input array_ and doesn't need to maintain the order of the other integers.


# General Strategy
# 1. Iterate through array using a while loop with two pointers, one at the beginning and one (head) and the end (tail)
# 2. head increments every time
# 3. tail decrements only when it is equal to toMove
# 4. if head == toMove and does not equal to tail, swap head with tail


# Time: O(n)
# Space: O(1)

def moveElementToEnd(array, toMove):
    temp = 0
    head = 0
    tail = len(array)-1

    while head < tail:
        while head < tail and array[tail] == toMove:
            # decrement tail
            tail -= 1
        if array[head] == toMove:
            # swap
            temp = array[tail]
            array[tail] = array[head]
            array[head] = temp
        # increment head
        head += 1

    return array



# Driver Code

# array = [2, 1, 2, 2, 2, 3, 4, 2]
array = [2, 4, 2,5,6,2,2]
toMove = 2

print(moveElementToEnd(array, toMove))

