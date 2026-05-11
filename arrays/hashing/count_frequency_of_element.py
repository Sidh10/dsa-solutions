def count_frequency(arr):
    freq = {}

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq


a = [1,2,3,4,5,6,7,8,9,10,1,2,3]
print(count_frequency(a))