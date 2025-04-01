# DFS of Graph

### Python
```py
class Solution:
    def dfs(self, adj):
        visited = [False]*len(adj)
        result=[]
        
        def dfshelp(node):
            visited[node] = True
            result.append(node)
            
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    dfshelp(neighbour)
        
        dfshelp(0)
        
        return result
```
