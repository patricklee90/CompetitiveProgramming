'''
Question Link: https://leetcode.com/problems/tallest-billboard/discuss/1800692/C%2B%2B-DP-solution

Solution Explanation: 

HashMap Method: 

Similar Question: 
'''
import math
from collections import defaultdict

class Solution(object):


    def tallestBillboard(self, rods):
        dp = defaultdict(int)
        dp[0] = 0
        for x in rods:
            nxt = dp.copy()
            for d, y in dp.items():
                nxt[d + x] = max(nxt.get(x + d, 0), y)
                nxt[abs(d - x)] = max(nxt.get(abs(d - x), 0), y + min(d, x))
            dp = nxt
        return dp[0]

input = [1, 2, 3, 6]

SolutionObj = Solution()

print(SolutionObj.tallestBillboard(input))