'''
Question Link: https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4672b 

Solution Explanation: 
'''
from multiprocessing import pool
import sys

class Solution(object):

    # Performance
    # Runtime: 
    # Memory: 
    def printing(self, printer1:list[int], printer2:list[int], printer3:list[int]):
        inkMatrix = []
        total = 0
        for ink in range(len(printer1)):
            colorMatrix = [(printer1[ink], ink),(printer2[ink],ink),(printer3[ink],ink)]

            colorMatrix.sort()

            total += colorMatrix[0][0]

            inkMatrix.append(colorMatrix[0])
        
        # print(f'total ink: {total}')

        if(total >= 1000000):
            inkMatrix.sort()

            sumCheck = 0
            result = ['0','0','0','0']

            for ink in inkMatrix:   
                if (sumCheck + ink[0])<=1000000:
                    sumCheck += ink[0]
                    result[ink[1]] = str(ink[0])
                else:
                    remain = 1000000 - sumCheck
                    sumCheck += remain
                    result[ink[1]] = str(remain)      
                    break       
            
            print(' '.join(result))
        else:
            print('IMPOSSIBLE')


printers = [
            [
                [300000,200000,300000,500000],
                [300000,200000,500000,300000],
                [300000,500000,300000,200000]
            ],
            [
                [1000000,1000000,0,0],
                [0,1000000,1000000,1000000],
                [999999,999999,999999,999999]
            ],
            [
                [768763,148041,178147,984173],
                [699508,515362,534729,714381],
                [949704,625054,946212,951187]
            ]
        ]
row = 3
solution = Solution()

for id, printer in enumerate(printers):
    # print(printer)
    print(f'Case #{id+1}:',end = ' ')
    solution.printing(printer[0],printer[1], printer[2])