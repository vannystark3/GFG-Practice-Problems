class Solution:
	def matSearch(self, mat, x):
		# Complete this function
		m = len(mat)
		n = len(mat[0])
		for i in range(m):
		    for j in range(n):
		        if(mat[i][j]==x):
		            return True
		return False
