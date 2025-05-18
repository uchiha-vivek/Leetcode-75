# https://leetcode.com/problems/climbing-stairs/description/
class Solution:
    
    # bottom up approach
    # person can only climb 1 or 2 tree
    # space complexity : O(n)
    # time complexity : O(N)
    def climbstair1(self,n:int):
        if n<=2:
            return n
        dp = [0]*(n+1)
        dp[1],dp[2]=1,2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]

    # try to solve by memoization
    # space complexity : o(n) 
    # time complexity : o(n)
    def climbstairs2(self,n:int,memo={}):
        # base case
        if n<=2:
            return n
        if n not in memo:
            return self.climbstairs2(n-1,memo) + self.climbstairs2(n-2,memo)
        return memo[n]

    # recursive approach
    # time complexity : o(2^n)
    # space complexity : o(n)
    def climbstairs3(self,n:int):
        # base case
        if n<=2:
            return n
        return self.climbstairs3(n-1) + self.climbstairs3(n-2)

if __name__=="__main__":
    sol=Solution()
    n1:int=3
    n2:int=2
    ans=sol.climbstair1(n2)
    ans1=sol.climbstairs2(n1)
    ans2=sol.climbstairs3(n1)
    print(ans2)