class Solution(object):
    def longestPalindrome(self, s):
        longest = s[0]
        for i in range(0, len(s)) :
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r + 1]) > len(longest):
                    longest = s[l:r + 1]
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r + 1]) > len(longest):
                    longest = s[l:r + 1]
                l -= 1
                r += 1
        return longest
