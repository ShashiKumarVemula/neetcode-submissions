class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        j=0
        for i in range(len(nums)):
            j=max(j,i)
            while j<len(nums) and nums[j]==val:
                j+=1
            if nums[i]==val and j<len(nums):
                nums[i],nums[j]=nums[j],nums[i]
        for i in nums:
            if i==val:
                k+=1
        return len(nums)-k
            

        