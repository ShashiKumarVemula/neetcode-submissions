class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = nums[0]
        cnt = 1
        for i in nums[1:]:
            if ele==i:
                cnt+=1
            if cnt==0:
                ele=i
            if ele!=i:
                cnt-=1
        return ele
            