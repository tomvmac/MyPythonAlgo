def merge(arr1, arr2):
    mergedList = []

    arr1Index = 0
    arr2Index = 0

    while arr1Index < len(arr1) and arr2Index < len(arr2):
        if arr1Index < len(arr1):
            if arr1[arr1Index] < arr2[arr2Index]:
                mergedList.append(arr1[arr1Index])
                arr1Index += 1
            else:
                if arr2Index < len(arr2):
                    mergedList.append(arr2[arr2Index])
                    arr2Index += 1

    if len(mergedList) < len(arr1) + len(arr2):
        mergedList.append(arr2[arr2Index-1])


    return mergedList


arr1 = [1, 2, 6, 8]
arr2 = [3, 4, 6, 8]

print(merge(arr1, arr2))