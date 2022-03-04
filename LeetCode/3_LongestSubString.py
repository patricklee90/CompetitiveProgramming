'''
Question Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/ 

Solution Explanation: https://www.youtube.com/watch?v=4RACzI5-du8&t=2s&ab_channel=NeetCode 
'''


class Solution(object):

    # Brute Force Solution
    def longestSubString(self, longString):
        subString = ""
        longestNum = 0

        for char in longString:
            print(char)
            if char not in subString:
                print(f"not in, longestNum {longestNum}.")
                subString += char
                print(f"substring new : {subString}")
                if len(subString) > longestNum:
                    print(f'substring, {subString} len: {len(subString)}')
                    longestNum = len(subString)
            else:
                subString = subString.split(char)[-1] + char
                # subString = char
        return longestNum
    
    # Sliding Window
    def longestSubStringSW(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res

longString = "dvdf"

SolutionObj = Solution()

print(SolutionObj.longestSubString(longString))