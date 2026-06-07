class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        for k in range(n):
            d={}
            target = -nums[k]
            for i in range(k+1, n):
                if (target - nums[i]) in d :
                    ans.add(tuple(sorted([nums[k],nums[i],target-nums[i]])))
                d[nums[i]] = i
        return list(ans)

        