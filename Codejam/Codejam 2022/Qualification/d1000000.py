'''
Question Link: https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a46471 

Solution Explanation: 
'''
from multiprocessing import pool
import copy

class Solution(object):

    # Performance
    # Runtime: 
    # Memory: 
    def diceStraight(self, dice):
        dice.sort()
        anchor = 1#copy.copy(dice[0])
        stack = [dice[0]]
        sum = 1
        result = 0

        for d in dice[1:]:
            # print(d, anchor)
            anchor = anchor + 1

            if(d<anchor):
                anchor = d
                result = max(result,sum)
            else:
                sum += 1    
            # print(d)
        
        print(max(result,sum))
        


dices = [
            [6,10,12,8],
            [5,4,5,4,4,4],
            [10,10,7,6,7,4,4,5,7,4],
            [10],
            [5,4,5,4,4,4,4,4,4,4,4,4],
        ]

solution = Solution()

for id, dice in enumerate(dices):
    # print(printer)
    print(f'Case #{id+1}:',end = ' ')
    solution.diceStraight(dice)