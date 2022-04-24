'''
Question Link: https://leetcode.com/problems/two-sum/

Solution Explanation: https://www.code-recipe.com/post/two-sum

HashMap Method: 
'''


class Solution(object):

    # Brute Force Solution
    def twoSumBF(self, nums, target):
        for bottom, bottomVal in enumerate(nums):
            for top, topVal in enumerate(nums[bottom+1:]):
                sum = bottomVal + topVal
                if(sum == target):
                    return [bottom, top + bottom+1]
    
    # HashMap - 1
    def twoSumHM(self, nums, target):
        hashMap = {}

        for id, number in enumerate(nums):
            hashMap[number] = id
        
        keys = hashMap.keys()

        for id,number in enumerate(nums):
            if(target-number in keys):
                if(hashMap[target-number] != id):
                    return [id, hashMap[target-number]]

    # HashMap - Best
    def twoSumHM2(self, nums: list, target:int) -> list:
        prevMap = {}

        for id, number in enumerate(nums):
            diff = target - number
            if diff in prevMap:
                return [prevMap[diff], id]
            prevMap[number] = id
        return



nums = [2,5,5,11]
target = 10

SolutionObj = Solution()

print(SolutionObj.twoSumHM2(nums,target))