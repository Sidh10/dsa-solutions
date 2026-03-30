def max_subarray_sum(arr):
    if not arr:
        return 0
    current_sum = arr[0]
    best_sum = arr[0]
    for i in range(1,len(arr)):
        current_sum = max(arr[i],current_sum + arr[i])
        best_sum = max(current_sum,best_sum)
    return  best_sum 
     
    


# Test cases
print(max_subarray_sum([-2, 3, -1, 5, -3, 2]))   # → 7
print(max_subarray_sum([5, 4, -1, 7, 8]))          # → 23
print(max_subarray_sum([-3, -1, -2]))              # → -1  
print(max_subarray_sum([1]))                        # → 1   