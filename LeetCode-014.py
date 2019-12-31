# others
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, e in enumerate(shortest):
            for other in strs:
                if other[i] != e:
                    return shortest[:i]
        return shortest
