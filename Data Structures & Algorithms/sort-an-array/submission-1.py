class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(l,mid,h):
            i=l
            j=mid+1
            a=[]
            while i<=mid and j<=h:
                if nums[i]<=nums[j]:
                    a.append(nums[i])
                    i+=1
                else :
                    a.append(nums[j])
                    j+=1
            while i<=mid:
                a.append(nums[i])
                i+=1
            while j<=h:
                a.append(nums[j])
                j+=1
            i=0
            for k in range(l,h+1):
                nums[k]=a[i]
                i+=1
        
        def mergesort(l,h):
            if l<h:
                mid = (l+h)//2
                mergesort(l,mid)
                mergesort(mid+1,h)
                merge(l,mid,h)

        mergesort(0,len(nums)-1)
        return nums

