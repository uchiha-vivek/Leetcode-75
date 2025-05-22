# https://leetcode.com/problems/house-robber/description/
def rob(nums):
    if not nums:
        return 0
    
    if len(nums)==1:
        return nums[0]
    
    dp = [0]*len(nums)
    dp[0]=nums[0]
    dp[1]=max(nums[0],nums[1])


    for i in range(2,len(nums)):
        dp[i]=max(dp[i-1],dp[i-2]+nums[i])
    
    return dp[-1]

# method 2
def rob2(nums):
    prev1,prev2 = 0,0
    for num in nums:
        temp=prev1
        prev1=max(prev1,num+prev2)
        prev2=temp
    return prev1


if __name__=="__main__":
    nums:list[int] = [2,7,9,3,1]
    ans = rob(nums)
    ans1=rob(nums)
    print(ans1)