
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1




int_arr = [1,2,3,4,5,6,7,8,9,10]
idx = 8

print(binary_search(int_arr, idx))