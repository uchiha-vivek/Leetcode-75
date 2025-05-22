# https://leetcode.ca/2016-08-12-256-Paint-House/

class Solution :
    def minCost(self,costs:list[list[int]]):
        a=b=c=0
        for ca,cb,cc in costs:
            a,b,c = min(b,c)+ca , min(a,c)+cb,min(b,c)+cc
        return min(a,b,c)

if __name__=="__main__":
    sol=Solution()
    nums:list[list[int]] =[[17,2,17],[16,16,5],[14,3,19]]
    ans= sol.minCost(nums)
    print(ans)