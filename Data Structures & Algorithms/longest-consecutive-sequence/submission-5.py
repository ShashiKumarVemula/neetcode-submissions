class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                streak = 1
                while num+streak in nums:
                    streak+=1
                ans=max(ans,streak)
        return ans
        


        