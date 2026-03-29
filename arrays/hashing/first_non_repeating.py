def non_rep(arr):
    dict1 ={}
    for num in arr:
        if num in dict1:
            dict1[num] += 1
        else:
            dict1[num] = 1
    for i in dict1:
        if dict1[i]==1:
         print(i)  
         return

arr1 = [5,4,37,6,2,7,5,2,4,7,0,8,37,6,45,76,23,79.45,75]
non_rep(arr1)