"""
Valid Palindrome
https://leetcode.com/problems/valid-palindrome
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def isalnum(c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))

        left = 0
        right = len(s) - 1

        while left < right:
            if not isalnum(s[left]):
                left += 1
                continue

            if not isalnum(s[right]):
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True
