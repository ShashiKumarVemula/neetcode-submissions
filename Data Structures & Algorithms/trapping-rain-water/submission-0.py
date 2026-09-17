class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [height[0]]
        right_max = [height[n-1]]
        for i in range(1,n):
            left_max.append(max(height[i],left_max[-1]))
        for i in range(1,n):
            right_max.append(max(height[n-i-1],right_max[-1]))

        right_max = right_max[::-1]

        ans = 0
        for i in range(n):
            ans+=max(0,min(left_max[i],right_max[i])-height[i])
        return ans
            
        