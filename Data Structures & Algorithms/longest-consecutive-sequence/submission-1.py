class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums = sorted(nums)
        n = len(nums)
        # print(nums)
        for i in range(n):
            num = nums[i]
            streak = 1
            for j in range(i+1,n):
                # print(nums[j])
                # print(streak)
                if nums[j]==(num+streak):
                    streak += 1
            ans = max(ans,streak)
        return ans
        


        