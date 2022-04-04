'''
Question Link: https://leetcode.com/problems/regular-expression-matching/ 

Solution Explanation: https://www.youtube.com/watch?v=HAA8mgxlov8&ab_channel=NeetCode 
'''
import sys

class Solution(object):

    # String approach
    # Runtime: 86ms (57.22%)
    # Memory: 13.8MB (97.59%)
    def isPalindrome(self, x:int) -> bool:
        s = str(x)
        return s == s[::-1]

    # Int approach
    # Runtime: 110ms (28.39%)
    # Memory: 13.8MB (70.64%)
    def isPalindromeInt(self, x:int) -> bool:
        if x<0:
            return False
        
        # Store the number in a variable
        number = x

        #store reverse number
        reverse = 0 
        while number:
            reverse = reverse *10 + number%10
            number //= 10

        return x == reverse

integer = [121, -121, -1234, -1234321, 1234321]
row = 3
solution = Solution()

for i in integer:
    print(solution.isPalindromeInt(i))