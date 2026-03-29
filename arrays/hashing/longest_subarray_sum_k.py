def longest_subarray(arr, k):
    current_sum = 0
    length = 0
    dict1 = {0: -1}
    for i in range(0, len(arr)):
        current_sum = current_sum + arr[i]
        needed = current_sum - k
        if needed in dict1:
            length = max(length,i - dict1[needed])
        if current_sum not in dict1:
            dict1[current_sum] = i
        
    return length
print(longest_subarray([1, -1, 1, 1, -1], 1))   # → 5
print(longest_subarray([1, 2, 3], 3))             # → 2
print(longest_subarray([1, 1, 1], 2))             # → 2
print(longest_subarray([3], 3))                   # → 1