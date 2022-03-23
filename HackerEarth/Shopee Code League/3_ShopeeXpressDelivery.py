'''
Question Link: 

Solution Explanation: 

HashMap Method: 

Similar Question: https://leetcode.com/problems/snakes-and-ladders/
'''
import math

class Solution(object):


    def shopeeXpressDelivery(self, grid:list[list[int]], m, n) -> int:
        
        visited = set()
        q = []
        dirs = [(0,1),(0,-1),(1,),(-1,0),(-1,-1),(1,1),(-1,1),(1,-1)]

        if grid[0][0] == 0:
            q.append((1,(0,0)))
            grid[0][0] = 1

        while q:
            steps, tmp = q.pop[-1]
            r,c = tmp[0], tmp[1]
            if(r,c) == (m-1, n-1):
                return steps
            for i,j in dirs:
                newR, newC = r+i, c+j
                if 0 <= newR < m and 0<= newC < n and grid[newR][newC] == 0 and (newR,newC) not in visited:
                    q.append((steps+2), (newR,newC))
                    # visited.add((newR, newC))
                    grid[newR][newC] = 1

        return -1

    def shopeeXpressDeliveryDfs(self, grid:list[list[int]], m, n) -> int:

        jumpMap = {}
        blackHoldMap = {}
        overallMap = []
        currentX, currentY = 0, 0
        stepX, stepY = 0, 0
        totalStep = 0

        for y, row in enumerate(grid):
            for x,elem in enumerate(row):

                if elem > 0:
                    if elem not in jumpMap:
                        jumpMap[elem] = []
                    jumpMap[elem].append([y,x])
                    overallMap.append([y,x])
                    blackHoldMap[y,x] = elem

        overallMap = sorted(overallMap)
        print(jumpMap)
        print(blackHoldMap)
        print(f'overallMap:{sorted(overallMap)}')
        def retrieve(y,x):
            return jumpMap[blackHoldMap[y,x]]

        def closesPoint():
            gap = []
            gap.append([m-currentX,n-currentY,m,n,m-currentX-1,n-currentY-1])
            
            for [y,x] in overallMap:
                print(y,x)
                if (currentY <= y and currentX <= x):
                    point2Cur = [y-currentY, x-currentX]
                    if(point2Cur[0] <=0 and point2Cur[1] <=0):
                        continue
                    print(f'y,x {y,x},currentY,currentX:{currentY,currentX}, point2Cur:{point2Cur}')
                    print(jumpMap[blackHoldMap[point2Cur[0],point2Cur[1]]])

                    sortedJump = sorted(retrieve(point2Cur[0],point2Cur[1]))
                    dest2Cur = [m-sortedJump[-1][0]+point2Cur[0], n-sortedJump[-1][1]+point2Cur[1]]
                    gap.append([dest2Cur[0],dest2Cur[1], sortedJump[-1][0],sortedJump[-1][1],point2Cur[0],point2Cur[1]])
            gap=sorted(gap)
            print(f"gap:{gap}")
            return (gap[0])

        def nextPoint(cord):
            return jumpMap[blackHoldMap[cord[0],cord[1]]][-1]

        while currentX < m and currentY < n:
            # stepY += overallMap[0][0] - currentY
            # stepX += overallMap[0][1] - currentX

            _, _, currentY, currentX, stepY, stepX = closesPoint()
            # currentY, currentX = nextPoint(overallMap[0])
            totalStep += stepY + stepX
            print(f"currentY, currentX:{stepY, stepX, currentY, currentX}")
        
        print(f"totalStep:{totalStep}")
            # break 
        # if grid[0][0] == 0:
        #     q.append((1,(0,0)))
        #     grid[0][0] = 1

        # while q:
        #     steps, tmp = q.pop[-1]
        #     r,c = tmp[0], tmp[1]
        #     if(r,c) == (m-1, n-1):
        #         return steps
        #     for i,j in dirs:
        #         newR, newC = r+i, c+j
        #         if 0 <= newR < m and 0<= newC < n and grid[newR][newC] == 0 and (newR,newC) not in visited:
        #             q.append((steps+1), (newR,newC))
        #             # visited.add((newR, newC))
        #             grid[newR][newC] = 1

        return -1

m = 8
n = 8
input = [[0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0]]

SolutionObj = Solution()

print(SolutionObj.shopeeXpressDeliveryDfs(input, m, n))