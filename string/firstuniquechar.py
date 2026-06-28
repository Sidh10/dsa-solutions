#Q387 Finding first unique character in a string  (Leetcode)



def firstuniquechar(str1):
    dict1 = {}
    for i in str1:
      if i in dict1:
         dict1[i] +=1
      else:
         dict1[i] =1
    for index,ch in enumerate(str1):
       if dict1[ch]==1:
          return index 
          break
    return -1
s = "loveleetcode"
print(firstuniquechar(s))

    

