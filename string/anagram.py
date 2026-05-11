


#Approach 1
def find_anagram(s,t):
   dict1 = {}
   dict2 = {}
   
   if len(s) != len(t):
      return False
   
   for i in s:
     if i in dict1:
        dict1[i] +=1
     else:
        dict1[i] = 1
   for i in t:
      if i in dict2:
        dict2[i] +=1
      else:
        dict2[i] =1
      
   return dict1 == dict2
   


#Approach 2

def find_anagram1(s,t):
   dict1 = {}
   
   if len(s) != len(t):
      return False
   for i in s:
      if i in dict1:
        dict1[i] +=1
      else:
         dict1[i] =1
   for i in t:
      if i not in dict1:
         return False
      else:
         dict1[i] -=1 
      
      
   for value in dict1.values(): 
      if value != 0:
         return False
      
   return True


#Approach 3

def find_anagram2(s,t):
   dict1 = {}

   if len(s) != len(t):
      return False
   for i in s:
      if i in dict1:
         dict1[i] +=1
      else:   
        dict1[i] =1
   for i in t:
      if i not in dict1:
         return False
      dict1[i] -=1
      if dict1[i]<0:
         return False
         
   return True

s = "aab"
t = "aac"
print(find_anagram2(s,t))
         
   


    
      



                

      