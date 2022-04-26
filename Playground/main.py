

def binary_search(array, target):

    left = 0
    right = len(array) - 1

    while left < right:

        mid = (left + right) // 2

        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            return mid

    return -1



print(binary_search([5,6,7,8,9,10,11,12,13,14,15,16], 13))