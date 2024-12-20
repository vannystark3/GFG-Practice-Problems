class Solution:
	def common_digits(self, nums):
        x = ""
		for num in nums:
		    x += str(num)
		return sorted(list(map(int,set(x))))
