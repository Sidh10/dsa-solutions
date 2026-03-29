def two_sum(arr, target):
    seen = {}

    for i, num in enumerate(arr):
        complement = target - num

        if complement in seen:
            print(complement, num)
            return
        seen[num] = i
        


arr1 = [2,4,5,3,6,9,7,24,8,32]
two_sum(arr1, 8)