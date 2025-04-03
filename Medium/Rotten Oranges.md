# Rotten Oranges

### Python
```py
from collections import deque

class Solution:
	def orangesRotting(self, mat):
	    n = len(mat)
	    m = len(mat[0])
	    
	    directions = [(-1,0),(1,0),(0,-1),(0,1)]
	    queue = deque()
	    freshCount = 0
	    
	    for i in range(n):
	        for j in range(m):
	            if mat[i][j]==2:
	                queue.append((i,j,0))
	            elif mat[i][j]==1:
	                freshCount += 1
	    
	    if freshCount==0:
	        return 0
	       
	    maxTime = 0
	    while queue:
	        i,j,time = queue.popleft()
	        for di,dj in directions:
	            ni,nj = di+i,dj+j
	            if 0<=ni<n and 0<=nj<m and mat[ni][nj]==1:
	                mat[ni][nj] = 2
	                freshCount -= 1
	                queue.append((ni,nj,time+1))
	                maxTime = max(maxTime,time+1)
	    if freshCount>0:
	        return -1
	    return maxTime
```
