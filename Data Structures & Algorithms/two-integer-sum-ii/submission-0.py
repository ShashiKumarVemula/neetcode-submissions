class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        n=len(numbers)
        j=n-1
        while i<j:
            summ = numbers[i]+numbers[j]
            if summ == target:
                return [i+1,j+1]
            elif summ<target:
                i+=1
            else:
                j-=1
        