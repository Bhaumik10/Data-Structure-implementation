print "Implement a function to perform DFS on given graph problem"
def dfs(graph, start):
    visited= set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)   # here we are removing the node from graph which is visited earlier
    return visited


graph = []

print dfs(graph, 'A')
