def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (high + low) // 2 # 11

        if (arr[mid] < target):
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid


array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
target = 18

print("Target ", target, " found at index ", binary_search(array, target))












def selection_sort(list_a):
    indexing_length = range(0, len(list_a) - 1)

    for i in indexing_length:
        min_value = i
        for j in range(i + 1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j

        if min_value != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]

    return list_a




unsorted_list = [4, 5, 7, 2, 6, 3, 1, 10]

print(selection_sort(unsorted_list))