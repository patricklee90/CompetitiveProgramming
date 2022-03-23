'''
Question Link: https://leetcode.com/problems/zigzag-conversion/

Solution Explanation: https://www.youtube.com/watch?v=Q2Tw6gcVEwc&ab_channel=NeetCode 
'''

class Solution(object):
    def convertBF(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s

        res = ""
        for r in range(numRows):
            increment = 2 * (numRows - 1)

            for i in range(r, len(s), increment):
                res += s[i]
                
                if(r > 0 and r < numRows - 1 and 
                    i + increment - 2 * r < len(s)):
                    res += s[i + increment - 2 * r]
        return res

s = "PAYPALISHIRING"
row = 3
solution = Solution()
solution.convertBF(s,row)