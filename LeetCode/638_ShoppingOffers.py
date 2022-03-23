'''
Question Link: https://leetcode.com/problems/shopping-offers/ 

Solution Explanation: https://www.youtube.com/watch?v=t6atP4Yv7_4&ab_channel=HappyCoding 

'''
from functools import lru_cache
import math, sys

class Solution(object):


    # Depth First Search
    # Runtime - 224ms
    # Memory - 14.2MB
    def shoppingOffer(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:
        @lru_cache(None)
        
        def shoppingOffersDepthFirstSearch(needs):
            needList = list(needs)

            # use regular price the purchase everything
            ans = sum(needList[i] * price[i] for i in range(n))

            # Try to use a special offer
            for s in special:
                canUse = True

                for i in range(n):
                    needList[i] -= s[i]
                    if needList [i] < 0:
                        canUse = False

                if canUse:
                    ans = min(ans, s[-1] + shoppingOffersDepthFirstSearch(tuple(needList)))

                for i in range(n):
                    needList[i] += s[i]

            return ans

        n = len(price)
        return shoppingOffersDepthFirstSearch(tuple(needs))



price = []
special = []
needs = []

SolutionObj = Solution()

print(SolutionObj.shoppingOffersDepthFirstSearch(price, special, needs))