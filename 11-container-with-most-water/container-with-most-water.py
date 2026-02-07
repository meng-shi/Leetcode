class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        size = 0
        while left < right:
            size = max(min(height[left],height[right])*(right-left),size)
            if height[right] < height[left]:
                right -= 1
            else:
                left +=1
        return size

