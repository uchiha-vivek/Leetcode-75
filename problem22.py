# https://leetcode.com/problems/house-robber-ii/description/
# House Robber 2
class Solution :
    def  rob_linear(self,nums:list[int]):
        prev1,prev2 = 0,0
        for num in nums:
            temp=prev1
            prev1=max(prev1,prev2+num)
            prev2=temp
        return prev1
    
    def circular_robbery(self,nums:list[int]):
        if not nums:
            return 0
        
        if len(nums)==1:
            return nums[0]
        
        rob1 = self.rob_linear(nums[:-1])
        rob2 = self.rob_linear(nums[1:])
        return max(rob1,rob2)
    

if __name__=="__main__":
    sol=Solution()
    nums = [2,3,2,4]
    ans=sol.circular_robbery(nums)
    print(ans)
