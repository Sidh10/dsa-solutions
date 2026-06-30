#Approach 1 : Time COmplexity = O(2^n)

class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        return self.fib(n-1)+self.fib(n-2)
    
#Approach 2 
class Solution:
 def fib(self,n):
    num_dict = {}
    num_dict[0]=0
    num_dict[1]=1
    return self.helper(num_dict,n)
 def helper(self,num_dict,n):
    if n in num_dict:
        return num_dict[n]
    num_dict[n]= self.helper(n-1)+ self.helper(n-2)
    return num_dict[n]