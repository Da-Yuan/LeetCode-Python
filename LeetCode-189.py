import copy

def rotate(nums,k):
	if len(nums)==1:
		return
	for i in range(k):
		for j in range(len(nums)):
			if j == 0:
				a=nums[j]
				b=nums[j+1]
				nums[j+1]=a
			elif j==len(nums)-1:
				nums[0]=a
			else:
				b=nums[j+1]
				nums[j+1]=a
			a=b
			print(j)
			print(nums)

def rotate1(nums, k):
    size=len(nums)
    k=k%size
    if size==1:
        return
    for i in range(k):
        a=nums[size-1]
        for j in range(len(nums)-1):
            nums[size-j-1] = nums[size-j-2]
        nums[0] = a

def rotate2(nums, k): # 通过验证 但是不是原地算法
	size = len(nums)
	nums_copy = copy.deepcopy(nums)
	if size == 1:
		return
	# index = 0
	for i in range(size):
		location = (i - k) % size
		nums[i] = nums_copy[location]
		print(location)

def rotate3(nums, k):
	l=len(nums)
	while l and k%l:
		k %= l
		for i in range(k):
			nums[i-l], nums[i-k] = nums[i-k], nums[i-l]
			print(nums)
		l -= k
		




a = [1,2,3,4,5,6,7]
k=4
rotate3(a,k)
print(a)
