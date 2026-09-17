class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxWater = 0
        left = 0
        right = len(height) - 1

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            currentWater = h * w
            maxWater = max(maxWater, currentWater)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxWater
        