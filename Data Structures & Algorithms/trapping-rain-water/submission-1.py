class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n-1
        left_max = height[0]
        right_max = height[j]
        ans = 0
        while i<j:
            if left_max<right_max:
                ans += max(0,left_max-height[i])
                i+=1
                left_max = max(left_max,height[i])
            else:
                ans += max(0,right_max-height[j])
                j-=1
                right_max =max(right_max,height[j])
        return ans
                
            
        