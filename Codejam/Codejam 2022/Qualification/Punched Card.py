'''
Question Link: https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4621b 

Solution Explanation: 
'''
from multiprocessing import pool
import sys

class Solution(object):

    # Performance
    # Runtime: 
    # Memory: 
    def punchCard(self, row:int, col:int):
        # set row
        plusLine = []
        poolLine = []
        for c in range(col):
            # append char
            plusLine += ['+','-']
            poolLine += ['|','.']
        plusLine += ['+']
        poolLine += ['|']

        for r in range(row):
            if r == 0:
                line1 = plusLine.copy()
                line2 = poolLine.copy()
                line2[0] = line2[1] = line1[0] = line1[1] = '.'
                # line2[0:2] = '.'
                print("".join(line1))
                print("".join(line2))
                plusLine = "".join(plusLine)
                poolLine = "".join(poolLine)
            else:
                print(plusLine)
                print(poolLine)

        print(plusLine)
        # print("".join(plusLine))
        # print("".join(poolLine))
        


cards = [[3, 4],[2,2],[2,3],[10,10]]
row = 3
solution = Solution()

for card in cards:
    print(card[0],card[1])
    solution.punchCard(card[0],card[1])