class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0
        for num in num_set:
            if num-1 not in num_set:
                temp_ans = 1
                while num+1 in num_set:
                    num+=1
                    temp_ans+=1
                ans = max(ans,temp_ans)
        return ans

        