# use isalnum() from python
class Solution(object):
    def isPalindrome(self, s):
        isValid = lambda x : x == x [::-1]
        string = ''.join([x for x in s.lower() if x isalnum()])
        return isValid(string)