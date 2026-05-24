class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums = sorted(nums)
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            return 1
        for i in range(1,n):
            num = nums[i-1]
            if nums[i]-num>1 or i==1:
                streak = 1
            if nums[i]-num==1:
                num = nums[i]
                streak+=1
            
            ans = max(streak,ans)
        return ans
        


        