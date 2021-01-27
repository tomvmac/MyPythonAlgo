import random
import string
import time

def binary_search_iter(n, arr):
    start = 0
    stop = len(arr)-1

    while start <= stop:
        mid = (start + stop) // 2
        if n == arr[mid]:
            return mid, f"{n} found at index: {mid}" # return tuple
        elif n > arr[mid]:
            start = mid + 1
        else:
            stop = mid -1
    return None, f"{n} not found in list"


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

def analyze_func(func_name, *args):
    tic = time.time()
    func_name(*args) # accept variable list of arguments
    toc = time.time()
    seconds = toc - tic
    print(f"{func_name.__name__.capitalize()}\t-> Elapsed time: {seconds:.5f}")


####### functions to generate lists of random emails #######
def generate_name(length_of_name):
    return ''.join(random.choice(string.ascii_letters) for i in range(length_of_name))

def get_domain(list_of_domains):
    return random.choice(list_of_domains)


def generate_emails(length_of_name, list_of_domains, total_emails):
    emails = []
    for num in range(total_emails):
        emails.append(generate_name(length_of_name)+"@"+get_domain(list_of_domains))
    return emails

