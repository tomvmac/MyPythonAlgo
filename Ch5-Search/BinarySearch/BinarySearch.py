def binary_search_iter(n, arr):
    start = 0
    stop = len(arr)-1

    while start <= stop:
        mid = (start + stop) // 2
        if n == arr[mid]:
            return f"{n} found at index: {mid}"
        elif n > arr[mid]:
            start = mid + 1
        else:
            stop = mid -1
    return f"{n} not found in list"


def binary_search_recur(n, arr, start, stop):
    if start > stop:
        f"{n} not found in list"
    else:
        mid = (start + stop) // 2
        if n == arr[mid]:
            return f"{n} found at index: {mid}"
        elif n > arr[mid]:
            return binary_search_recur(n, arr, mid+1, stop)
        else:
            return binary_search_recur(n, arr, start, mid-1)

    return arr


def create_list(max_val):
    arr = []
    for num in range(1, max_val+1):
        arr.append(num)
    return arr

l = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_to_search = 2
print("Iterative Binary Search")
print(binary_search_iter(num_to_search, l))

print("-----------------------------------")

print("Recursive Binary Search")
print(binary_search_recur(num_to_search, l, 0, len(l)))