class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums = sorted(nums)
        n = len(nums)
        for k in range(n):
            target = -nums[k]
            i = k+1
            j = n-1
            while i<j :
                summ = nums[i]+nums[j]
                if summ == target:
                    ans.add(tuple(sorted([nums[i],nums[j],nums[k]])))
                    i+=1
                    j-=1
                elif summ<target :
                    i+=1
                else:
                    j-=1
        return list(ans)
                 

        