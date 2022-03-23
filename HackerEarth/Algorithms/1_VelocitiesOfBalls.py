'''
Question Link: https://leetcode.com/problems/car-fleet/

Solution Explanation: 

Similar Questions:
    - LeetCode #853 (Car Fleet)
'''
from runtime import Runtime
import math, functools

class Solution():
    def __init__(self):
        self.speed = []
        self.position = []

    def velocitiesOfBalls(self, position, speed):
        sequence = range(len(position))
        pair = [[p,s,seq] for p,s,seq in zip(position,speed,sequence)]

        collide = [0] * len(pair)
        stack = []
        sortedPair = sorted(pair)[::-1]
        for id in range(len(pair)): #Reverse Sorted Order
            p, s, seq = sortedPair[id]
            if(s>0):
                stack.append([(2000 - p) / s, p, s, seq])
            elif(s<0):
                stack.append([(p+2000) / s , p, s, seq])
            else:
                collide.append(0)
                continue
            print(f'ori: {stack}')
            
            distanceFlow = []
            
            if len(stack) >= 2 and stack[-1][2] >= 0:
                stackLen = len(stack)-2
                popEnable = False
                for place, group in enumerate(stack[:-1][::-1]):
                    print(f"group:{group}")
                    if stack[-1][0] >= group[0] :
                        position = ((stack[-1][1] - group[1])/(group[2] - stack[-1][2]))
                        print(f"position:{position}, upper:{(stack[-1][1] - stack[-2][1])}, lower: {(stack[-2][2] - stack[-1][2])}")
                        collide[stack[-1][3]] += math.floor(position)
                        collide[stack[stackLen-place][3]] += math.floor(position)

                        print(f"stackLen-place:{stackLen-place}, stackLen:{stackLen}")
                        stack[-1][3], stack[stackLen-place][3] = stack[stackLen-place][3], stack[-1][3]
                        # sortedPair[stack[-1][4]][1],  sortedPair[stack[-2][4]] = stack[-2][3], stack[-1][3] 
                        
                        print(f'stack: {stack}') 
                        # print(sortedPair[stack[-1][4]],  sortedPair[stack[-2][4]])
                        print(f'collide: {collide}')    
                        popEnable = True            
                        x = input()
                
                if popEnable:
                    stack.pop()

        return collide

    def velocitiesOfBalls2(self, position, speed):
        sequence = range(len(position))
        pair = [[p,s,seq] for p,s,seq in zip(position,speed,sequence)]       

        collide = [0] * len(pair)
        stack = []
        
        for p, s, seq in sorted(pair)[::-1]:
            if(s>0):
                stack.append([(2000 - p) / s, p, s, seq])
            elif(s<0):
                stack.append([(p+2000) / s , p, s, seq])
            else:
                collide.append(0)
                continue

            if len(stack) >= 2 and stack[-1][2] >= 0:
                stackLen = len(stack)-2
                popEnable = False

                for place, group in enumerate(stack[:-1][::-1]):
                    if stack[-1][0] >= group[0]:
                        position = ((stack[-1][1] - group[1])/(group[2] - stack[-1][2]))
                        collide[stack[-1][3]] += math.floor(position)
                        collide[stack[stackLen-place][3]] += math.floor(position)
                        stack[-1][3], stack[stackLen-place][3] = stack[stackLen-place][3], stack[-1][3]
                        popEnable = True          

                if popEnable:
                    stack.pop() 

        return collide


    def velocitiesOfBalls3(self, position, speed):
        def compare(elem1, elem2):
            decision = ((speed[elem2[0]] - speed[elem2[1]])*(position[elem1[1]] - position[elem1[0]])) - ((speed[elem1[0]] - speed[elem1[1]])*(position[elem2[1]]- position[elem2[0]]))
            return decision
        
        sequence = list(range(len(position)))
        pair = [[p,s,seq] for p,s,seq in zip(position,speed,sequence)]   
        collide = [0] * len(pair)
        stack = hit = []

        for i in sequence:
            for j in sequence:
                if(position[i] < position[j] and speed[i] > 0 and speed[j] < 0):
                    stack.append([i,j])

        stack = sorted(stack, key=functools.cmp_to_key(compare))

        for x,y in stack:
            time = (position[y] - position[x])/(speed[x] - speed[y])
            collide[sequence[x]] += math.floor(time)
            collide[sequence[y]] += math.floor(time)
            sequence[y], sequence[x] = sequence[x], sequence[y]

        print(collide)

runtime = Runtime()

'''
Program Here

'''


position = [8,4,0,-3,2]#[-5,1,5]
speed = [-3,2,1,1,-4]#[1,1,-2]
solution = Solution()
collision = solution.velocitiesOfBalls3(position,speed)

runtime.stop()

print(collision)