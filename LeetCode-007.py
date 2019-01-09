# my code
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num_str = list(str(x))
        num_str = num_str[::-1]
        if num_str[-1] == '-':
            num_str = num_str[:-1]
            num_str = ['-', ] + num_str

        num_str = ''.join(num_str)
        output = int(num_str)
        if output > pow(2, 31) - 1 or output < -pow(2, 31):
            return 0

        return output

# others
class Solution1(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = int(str(x)[::-1]) if x > 0 else -int(str(-x)[::-1])
        return x if x<2147483648 and x>-2147483648 else 0


class Solution2(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = x < 0 and -1 or 1
        x = abs(x)
        ans = 0
        while x:
            ans = ans * 10 + x % 10
            x /= 10
        return sign * ans if ans <= 0x7fffffff else 0

