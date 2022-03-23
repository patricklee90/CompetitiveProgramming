'''
Question Link: https://leetcode.com/problems/car-fleet/

Solution Explanation: https://www.youtube.com/watch?v=Pr6T-3yB9RM&ab_channel=NeetCode 
'''
from runtime import Runtime;

class Solution:
    def carFleet(self, target, position, speed) -> int:
        pair = [[p,s] for p,s in zip(position,speed)]

        stack = []
        for p, s in sorted(pair)[::-1]: #Reverse Sorted Order
            stack.append((target - p) / s)
            print(stack)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

runtime = Runtime()

'''
Program Here
'''
target = 10
position = [6,8]
speed = [3,2]

solution = Solution()
answer = solution.carFleet(target, position, speed)

runtime.stop()

print(f'answer: {answer}')