def palindrome(s):
    s = s.replace(" ","").replace(",","").replace(":","").replace(";","")
    s = s.lower()
    left = 0
    right = len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left +=1
        right -=1
    return True
s = "A man, a plan, a canal: Panama"
print(palindrome(s))




    

