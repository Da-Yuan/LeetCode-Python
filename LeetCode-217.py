# 给定一个整数数组，判断是否存在重复元素。

# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

def Solution1(nums): # 超出时间限制
	if len(nums)==1:
		return False
	for i in range(len(nums)):
		for j in range(len(nums)-i-1):
			if nums[i]==nums[-j-1]:
				return True
	return False


a1=[1,2,3,1]
a2=[1,2,3,4]
a3=[3,1]
print(Solution(a3))