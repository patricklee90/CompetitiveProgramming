'''
Question Link: https://leetcode.com/problems/string-to-integer-atoi/ 

Solution Explanation: https://www.code-recipe.com/post/reverse-integer 
'''

class Solution(object):

    def stringToInteger(self, sentence: str) -> int:
        # signMultiplier = -1 for negative numbers
	    # signMultiplier = 1 for positive numbers
        signMultiplier = 1
        signLock = False
        numLock = False
        result = 0

        for id, s in enumerate(sentence):
            # print(s,signLock)
            if s in ["+", "-"] and signLock == False:
                signMultiplier *= 1 if s == "+" else -1     
                signLock = True           
            
            elif s.isnumeric():
                result = result*10 + int(s)
                signLock = True

            elif signLock == True:
                break
            elif s == " ":
                continue

            elif s != " ":
                break

        min_int_32 = 2 ** 31
        if result * signMultiplier <= -min_int_32:
            return -min_int_32
        elif result * signMultiplier >= min_int_32-1:
            return min_int_32-1

        if signMultiplier == 99: signMultiplier = 1

        return result * signMultiplier

integer = ["12345", " 12340", "-12340","   -12340", "12345 have some word", "1234 word123", "+-12", "00000-42a1234", "   +0 123"]
row = 3
solution = Solution()

for i in integer:
    print(solution.stringToInteger(i))