# BFS of graph

### Python
```py
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        visited = [False]*len(adj)
        queue = []
        res = []
        
        visited[0] = True
        queue.append(0)
        
        while queue:
            node = queue.pop(0)
            res.append(node)
            
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)
        
        return res
```
