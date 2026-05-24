class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt = 0
        product = 1
        for i in nums:
            if i==0:
                cnt+=1
            else:
                product*=i
        if cnt>1:
            return [0]*len(nums)
        ans=[]
        if cnt ==1 :
            for i in range(len(nums)):
                if nums[i]==0:
                    ans.append(product)
                else:
                    ans.append(0)
        else:
            for i in range(len(nums)):
                ans.append(product//nums[i])
        return ans
        