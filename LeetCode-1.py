# my code
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[i]+nums[i+j+1] == target:
                    return i, i+j+1
        # 用两遍for循环是最笨的方法了。。。
            

# best solution
class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)): 
            if nums[i] in d:
                return d[nums[i]], i
            else:
                d[target - nums[i]] = i
                continue