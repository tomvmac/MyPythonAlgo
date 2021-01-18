# Bubble Sort

# Strategy
# 1. Loop
# 2. Compare number to next number
# 3. Swap if number is greater than next number
# 4. Keep doing until done

# Big O Notation

# - Given n numbers, n ^ 2
# - Big O of N^2

def bubble_sort(arr):
    # Potential solutions
    # 1. Nested for loops, but this is not most efficient because the list could be sorted already and still
    #     iterating  o n^2
    # 2. Optimized solution is to use a flag to sign swap occured,

    swap_happened = True

    while swap_happened:
        print('bubble sort status: ' + str(arr))
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

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
bubble_sort(l)

