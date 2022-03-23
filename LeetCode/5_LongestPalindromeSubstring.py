'''
Question Link: https://leetcode.com/problems/longest-palindromic-substring/

Solution Explanation:
'''

class Solution(object):
    def longestPalindromeBF(self, s):
        """
        :type s: str
        :rtype: str
        """
        mask = 1
        window = len(s)
        output = ""


        while mask <= window:
            for pos in range(len(s)):
                if(pos+mask > len(s)):
                    mask += 1
                    break

                subStr = s[pos:pos+mask]
                # print("current: ", subStr, f"pos:pos+mask, {pos,pos+mask}")
                if(subStr == subStr[::-1]):
                    if(len(subStr) > len(output)):
                        output = subStr
                    mask += 1
                    break

        return output

    # Expand in both directions of `low` and `high` to find maximum length palindrome
    def expand(self,s, low, high):
        length = len(s)

        # expand in both directions
        while low >= 0 and high < length and s[low] == s[high]:
            low = low - 1
            high = high + 1

        # return palindromic substring
        return s[low + 1:high]

    def longestPalindromeBFv2(self, s):
        # base case
        if not s or not len(s):
            return ''

        # `max_str` stores the maximum length palindromic substring found so far
        max_str = ''

        # `max_length` stores the maximum length of palindromic
        # substring found so far
        max_length = 0

        # consider every character of the given string as a midpoint and expand
        # in both directions to find maximum length palindrome

        for i in range(len(s)):

            # find the longest odd length palindrome with `s[i]` as a midpoint
            curr_str = self.expand(s, i, i)
            curr_length = len(curr_str)

            # update maximum length palindromic substring if the odd length
            # palindrome has a greater length

            if curr_length > max_length:
                max_length = curr_length
                max_str = curr_str

            # Find the longest even length palindrome with `s[i]` and `s[i+1]` as
            # midpoints. Note that an even length palindrome has two midpoints.

            curr_str = self.expand(s, i, i + 1)
            curr_length = len(curr_str)

            # update maximum length palindromic substring if even length
            # palindrome has a greater length

            if curr_length > max_length:
                max_length = curr_length
                max_str = curr_str

        return max_str

    def longestPalindromeBS(self,s):
        def isPalindrome(s):
            return s == s[::-1]

        # Return true if there is a palindrome of length x
        def good(x, s):
            n = len(s)
            for L in range(n):
                if(L+x) < n:
                    if(isPalindrome(s[L:x])):
                        return L

            return -1

        bestLen = 0
        bestString = ""
        n = len(s)
        low =1
        high = n

        for parity in {0,1}:
            low = 1
            high = n

            if(low%2 != parity): low+=1
            if(high%2 != parity): high -=1

            while(low<=high):
                mid = (low + high)/2
                if(mid%2 != parity):
                    mid+=1
                if(mid>high):
                    break

                tmp = good(int(mid), s)
                if(tmp != -1):
                    if(mid > bestLen):
                        bestLen = mid
                        bestString = s[tmp:int(mid)]
                    bestLen = max(bestLen, mid)
                    low = mid + 2
                else:
                    high = mid - 2

        return bestString

# s = "esbtzjaaijqkgmtaajpsdfiqtvxsgfvijpxrvxgfumsuprzlyvhclgkhccmcnquukivlpnjlfteljvykbddtrpmxzcrdqinsnlsteonhcegtkoszzonkwjevlasgjlcquzuhdmmkhfniozhuphcfkeobturbuoefhmtgcvhlsezvkpgfebbdbhiuwdcftenihseorykdguoqotqyscwymtjejpdzqepjkadtftzwebxwyuqwyeegwxhroaaymusddwnjkvsvrwwsmolmidoybsotaqufhepinkkxicvzrgbgsarmizugbvtzfxghkhthzpuetufqvigmyhmlsgfaaqmmlblxbqxpluhaawqkdluwfirfngbhdkjjyfsxglsnakskcbsyafqpwmwmoxjwlhjduayqyzmpkmrjhbqyhongfdxmuwaqgjkcpatgbrqdllbzodnrifvhcfvgbixbwywanivsdjnbrgskyifgvksadvgzzzuogzcukskjxbohofdimkmyqypyuexypwnjlrfpbtkqyngvxjcwvngmilgwbpcsseoywetatfjijsbcekaixvqreelnlmdonknmxerjjhvmqiztsgjkijjtcyetuygqgsikxctvpxrqtuhxreidhwcklkkjayvqdzqqapgdqaapefzjfngdvjsiiivnkfimqkkucltgavwlakcfyhnpgmqxgfyjziliyqhugphhjtlllgtlcsibfdktzhcfuallqlonbsgyyvvyarvaxmchtyrtkgekkmhejwvsuumhcfcyncgeqtltfmhtlsfswaqpmwpjwgvksvazhwyrzwhyjjdbphhjcmurdcgtbvpkhbkpirhysrpcrntetacyfvgjivhaxgpqhbjahruuejdmaghoaquhiafjqaionbrjbjksxaezosxqmncejjptcksnoq"
s = "babad"
solution = Solution()
print(solution.longestPalindromeBS(s))