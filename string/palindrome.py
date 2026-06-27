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




#Q2 Palindrome number

def isPalindrome( x: int) -> bool:
        x = str(x)
        a = list(x)
        b = list(x)
        print(b)
        left = 0
        right = len(a)-1
        while left<right:
            a[left],a[right] = a[right],a[left]
            left +=1
            right -=1
        if a == b:
              return True
        else :
              return False

#Approach 2

def isPalindrome( x: int) -> bool:
    rev = 0
    if x<0:
        return False
    if x%10 ==0 and x!=0:
        return False
    while x>rev:
        rev = rev*10 + (x%10)
        x = x//10
    return x ==rev or x== rev//10
   


    

