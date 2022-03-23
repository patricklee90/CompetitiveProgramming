'''
Question Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/special-shop-69904c91/ 

Solution Explanation: https://www.code-recipe.com/post/two-sum

HashMap Method: 

Similar Question: https://leetcode.com/problems/shopping-offers/ 
'''
import math

class Solution(object):


    # HashMap - Best
    def specialShopHM(self, target:int, a:int, b:int):
        minTotal = 10**5 * math.pow(10**5,2) 
        low,high = sorted([a,b])

        for id, number in enumerate(range(target+1)[::-1]):
            print(number)
            total = low*math.pow(number,2) + high*math.pow(target-number,2)
            
            if(total <= minTotal):
                minTotal = total
            else:
                return minTotal

        return int(minTotal)

    def specialShopLM(self, target:int, a:int, b:int):
        minTotal = 10**5 * math.pow(10**5,2) 
        low,high = sorted([a,b])    
        diff = 100
        pin = 0

        while diff > 0:
            lhs = low*math.pow(pin,2) + high*math.pow(target-pin,2)
            rhs = low*math.pow(pin+1,2) + high*math.pow(target-pin-1,2)
            print(pin)
            if((rhs - lhs)>1000):
                pin = int(pin + target*0.01)
            elif((rhs-lhs)<0):
                pin = int(pin - target*0.009)
                # for id, number in enumerate(range(target-pin)[::-1]):
                #     total = low*math.pow(number,2) + high*math.pow(target-number,2)
                    
                #     if(total <= minTotal):
                #         minTotal = total
                #     else:
                #         return minTotal

                # return int(minTotal)
            else:
                for id, number in enumerate(range(target-pin)[::-1]):
                    total = low*math.pow(number,2) + high*math.pow(target-number,2)
                    
                    if(total <= minTotal):
                        minTotal = total
                    else:
                        return minTotal

                return int(minTotal)

    def specialShopFormula(self, n:int, a:int, b:int):
        # Write your code here
        x=(-n*b)//(a-b)

        y=n-x

        if(abs(x*(a+b)-(n*b))>abs((x+1)*(a+b)-(n*b))):

            x=x+1

            y=n-x

        return a*(x**2)+b*(y**2)

target, a, b = [int(x) for x in "18 55 72".split()]

SolutionObj = Solution()

print(SolutionObj.specialShopFormula(target, a, b))