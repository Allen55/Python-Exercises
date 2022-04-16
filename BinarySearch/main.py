
def binary_search(arr, target):
    if len(arr) < 1:
        return -1

    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < target:
            low = arr[mid] + 1
        elif arr[mid] > target:
            high = arr[mid] - 1
        else:
            return mid

    return -1






array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

target = 5

print("Target ", target, " found at index: ", binary_search(array, target))
#print(binary_search(array, target))