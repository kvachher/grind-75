class Solution(object):
    def isPalindrome(self, s):
        s = s.replace(" ", "").lower()
        for i in s: 
            if i in string.punctuation: 
               s = s.replace(i, "") 
        reverse = s[::-1]
        return (reverse == s)
