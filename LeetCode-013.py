# my code
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900,
        }
        summation = 0
        while s:
            if s[:2] in d:
                summation += d[s[:2]]
                s = s[2:]
            elif s[0] in d:
                summation += d[s[0]]
                s = s[1:]
        return summation
# others
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans=0
        for i in range(len(s)):
            if i<len(s)-1 and a[s[i]]<a[s[i+1]]:
                ans-=a[s[i]]
            else:
                ans+=a[s[i]]
        return ans