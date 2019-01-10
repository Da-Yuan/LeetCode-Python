# my code
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        y=x[::-1]
        if y==x:
            return True
        else:
            return False
