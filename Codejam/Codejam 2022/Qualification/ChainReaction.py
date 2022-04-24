'''
Question Link: https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45ef7 

Solution Explanation: 
'''
from multiprocessing import pool
import copy
import sys

sys.setrecursionlimit(10000)

class Solution(object):

    # Performance
    # Runtime: 
    # Memory: 
    def chainReaction(self, funScore, direction):
        #generate edge

        edges = []
        funGraph = {}
        resultGraph = {}
        for id, neighbour in enumerate(direction):
            print(id, neighbour)

            if neighbour not in funGraph:
                funGraph[neighbour] = set()
            # if(neighbour>0):
            #     neighbour -=1
            
            funGraph[neighbour].add(id+1)
            edges.append({id, neighbour})

        print(funGraph)
        def resursiveSum(i, resultGraph):
            
            if i in funGraph:
                for j in funGraph[i]:
                    print(i, j, resultGraph)
                    resultGraph.append(resursiveSum(j, resultGraph))
            else:
                print(f'{i} not in loop, return {funScore[i-1]}')
                return funScore[i-1]
            

        resursiveSum(0, [])
    
    def chainReaction2(self, funScore, direction):
        maxDirection = max(direction)
        size = len(direction)
        funScore.insert(0,0)
        direction.insert(0,0)

        # print(f'maxDirection: {maxDirection}')
        # print(f'funScore: {funScore}')
        # print(f'direction: {direction}')

        resultList = []
        w = 0 
        finalValue = 0 

        for id in range(maxDirection+1, size+1):
            arr = []
            if direction[id] == 0:
                w += funScore[id]
            else:
                arr.append(id)
                if direction[id] == 1:
                    arr.append(1)
                    resultList.append(arr)
                else:
                    temp = direction[id]

                    while temp != 1:
                        arr.append(temp)
                        temp = direction[temp]
                        if temp == 1:
                            arr.append(temp)
                    
                    resultList.append(arr)

        del direction
        calculation = {}
        
        resultList = [x[::-1] for x in resultList]
        resultList.sort()
        # print(resultList)
        # valGroup = [(funScore[x],x) for x in resultList[0]]
        # valGroup.sort()
        # print(f'valGroup:{valGroup}')
        # print(f'max(valGroup[0]):{max(valGroup)[0]}')
        # filterGroup = [max(valGroup)[0]]
        filterGroup = []
        buffer = [[],0] 
        commonGroup = None
        # print(filterGroup)
        # firstVal = funScore[resultList[0]]
        print(f'resultList:{resultList}')
        for id, value in enumerate(resultList):
            valGroup = [(funScore[x],x) for x in value]
            # print(id, resultList[id-1],resultList[id])
            if id < len(resultList)-1:
                commonGroup = list(set(resultList[id]).intersection(resultList[id+1]))
            valGroup.sort()
            print(f'valGroup:{valGroup}')
            print(f'commonGroup:{commonGroup}')
            maxGroup = max(valGroup)

            if(maxGroup[1] > max(commonGroup)):
                filterGroup.append(maxGroup[0])                
            else:
                for val in valGroup:
                    if val not in buffer[0]:
                        buffer[0].append(val)
                buffer[1]+=1
                print(f'buffer: {buffer[0]}, no: {buffer[1]}')

            # print(maxGroup)
            


            # calculation[value[0]] = valGroup[0]
            
        buffer[0].sort(reverse=True)
        # print(f'filterGroup:{filterGroup}')
        # print(buffer)
        for buff in buffer[0][:buffer[1]]:
            filterGroup.append(buff[0])

        print(calculation)
        print(f'filterGroup:{filterGroup}')
        # for id, value in enumerate(resultList):
        #     for val2 in range(len(resultList)):
        #         calculation[val2] = False
        #     calculation[id] = True
        
        #     totalResult = w
        #     obj = {}

        #     # Initiate object
        #     for falseVal in range(size+1):
        #         obj[falseVal] = False
            
        #     result = 0

        #     for elem in value:
        #         obj[elem] = True
        #         result = max(result,funScore[elem])
            
        #     totalResult += result

        #     for id2, deepVal in enumerate(resultList):
        #         if calculation[id2]:
        #             continue
        #         else:
        #             result = 0
        #             for elem in deepVal:
        #                 if not obj[elem]:
        #                     result = max(result,funScore[elem])
        #                     obj[elem] = True
        #             totalResult += result
            
        #     finalValue = max(finalValue,totalResult)

        print(finalValue)

    def sampleAnswer():
        t = int(input())
        a = ""
        for nnn in range(0, t):
            n = int(input())
            b = [int(a) for a in input().split(" ")]
            c = [int(a) for a in input().split(" ")]
            d = f"Case #{nnn+1}: "
            f = max(c)
            b.insert(0,0)
            c.insert(0,0)
            q = []
            w = 0
            s = 0
            for xc in range(f+1,n+1):
                er = []
                if c[xc] == 0:
                    w += b[xc]
                else:
                    er.append(xc)
                    if c[xc] == 1:
                        er.append(1)
                        q.append(er)
                    else:
                        fg = c[xc]
                        while fg != 1:
                            er.append(fg)
                            fg = c[fg]
                            if fg == 1:
                                er.append(fg)
                                break
                        q.append(er)
                    
            del c
            cal = {}
            
            print(q)

            for yu,pu in enumerate(q):
                for nnn in range(len(q)):
                    cal[nnn] = False
                cal[yu] = True
                dfg = w
                m = {}
                for nnn in range(n+1):
                    m[nnn] = False
                zx = 0
                for xc in pu:
                    m[xc] = True
                    zx = max(zx,b[xc])
                dfg += zx
                for vb,lop in enumerate(q):
                    if cal[vb]:
                        continue
                    else :
                        zx = 0
                        for xc in lop:
                            if not m[xc]:
                                zx = max(zx,b[xc])
                                m[xc] = True
                        dfg += zx
                s = max(s,dfg)
            d += f"{s}"
            print(d)

    def youtubeAnswer(self, funScore, direction):
        '''
            let f(x) be the total amount of fun we can have in the subtree rooted at X
            let C = [f(C) for C in children(X)]
            f(X) = max(C[0],V[x]) + sum(other C)
        '''
        def checking(x, C, F):
            if(len(C[x])== 0):
                return funScore[x]
            else:
                CS = []
                for c in C[x]:
                    CS.append(checking(c,C,F))
                CS.sort()

                ans = max(funScore[x], CS[0])

                for i,value in enumerate(CS):
                    ans += value

                return ans

        n = len(direction)
        funScore.insert(0,0)
        direction.insert(0,0)
        
        print(funScore)
        print(direction)

        
        C = []

        for i in range(n+1):
            C.append([])

        print(C)
        for i in range(n+1):
            # print(i, direction[i])
            C[direction[i]].append(i)
            # print(C[direction[i]])
        print("stuck",C)
        answer = checking(0, C, funScore)
        print("answer",answer)

chains = [
            [
                [60,20,40,50],
                [0,1,1,2]
            ],
            # [
            #     [3,2,1,4,5],
            #     [0,1,1,1,0]
            # ],
            # [
            #     [100,100,100,90,80,100,90,100],
            #     [0,1,2,1,2,3,1,3]
            # ],
        ]

solution = Solution()

for id, chain in enumerate(chains):
    print(f'Case #{id+1}:',end = ' ')
    solution.youtubeAnswer(chain[0],chain[1])