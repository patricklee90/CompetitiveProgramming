'''
Question Link: https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa8e9c 

Solution Explanation: 
1. https://www.youtube.com/watch?v=ZdpSR4L09NI&ab_channel=HappyCoding 
'''
from multiprocessing import pool
import copy
import sys

class Solution:
    def doubleOrOne(self, stringExp):
        res = ""
        last = '\0'
        cnt = 0

        for i in range(len(stringExp)):
            print(f"i:{i}, string[i]:{stringExp[i]}, last:{last}, last<str[i]?:{last < stringExp[i]}, cnt:{cnt}")
            if stringExp[i] != last:
                if(last < stringExp[i]):
                    cnt*=2
                
                print(f"cnt:{cnt}", end=" ")
                while cnt>0:
                    cnt -=1
                    res += last
                print(f", res:{res}")
                last = stringExp[i]
                cnt = 0
            cnt +=1
        while cnt>0:
            cnt -=1
            res += last
        
        print(res)

stringLink = [
            "PEEL",
            "AAAAAAAAAA",
            "CODEJAMDAY",
        ]

solution = Solution()

for id, stringExp in enumerate(stringLink):
    print(f'Case #{id+1}:',end = ' ')
    solution.doubleOrOne(stringExp)