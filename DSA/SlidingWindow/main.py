# Given an array, find the average of all subarrays of ‘K’ contiguous elements in it.
# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# https://www.educative.io/courses/grokking-the-coding-interview/7D5NNZWQ8Wr

def find_averages_of_subarrays(K, arr):
    result = []
    window_sum, window_start = 0.0, 0
    for window_end in range(len(arr)):  # add next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'K'
        window_sum += arr[window_end]
        if window_end >= K - 1:
            result.append(window_sum / K)  # calculate the average
            window_sum -= arr[window_start]  # subtract the element going out
            window_start += 1  # slide the window ahead

    return result


result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
print("Average of subarrays of size k: " + str(result))


#list_a = [1, 3, 5, 7, 9, 10]

#for i in list_a:
 #   print(i)

#for i in range(len(list_a)):
  #  print(list_a[i])
