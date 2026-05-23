class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        ans=[]
        for i in nums:
            if i!=val:
                ans.append(i)
                k+=1
        for i in range(k):
            nums[i]=ans[i]
        return k 

        