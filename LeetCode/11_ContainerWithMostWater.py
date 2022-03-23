'''
Question Link: https://leetcode.com/problems/container-with-most-water/

Solution Explanation: https://www.geeksforgeeks.org/container-with-most-water/ 
'''
import sys

class Solution(object):
    def containerWithMostWaterBF(self, height:list[int]) -> int:
        maxArea = 0
        for id1, h1 in enumerate(height):
            for id2 in range(len(height)):
                minValue = min(h1,height[id2])

                if(id2 - id1)*minValue > maxArea:
                    maxArea = (id2 - id1)*minValue
        return maxArea
    
    # Runtime: 893ms(61.35%)
    # Memory: 27.5MB(61.93%)
    def containerWithMostWaterSort(self, height:list[int]) -> int:
        low = 0 
        high = len(height)-1
        area = 0

        while low < high:
            area = max(area, min(height[low], height[high])*(high-low))

            if height[low]< height[high]:
                low += 1
            else:
                high -=1
        return area

heights = [1,8,6,2,5,4,8,3,7]
row = 3
solution = Solution()

print(solution.containerWithMostWaterSort(heights))