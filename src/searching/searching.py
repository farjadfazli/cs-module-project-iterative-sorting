def linear_search(arr, target):
    # Your code here
    for index in range(len(arr)):
        if arr[index] == target:
            return index

    # for i in arr:
    #     if i == target:
    #         return arr.index[target]
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # divide the arr by 2
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if target == arr[middle]:
            return middle
        elif arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return -1  # not found
