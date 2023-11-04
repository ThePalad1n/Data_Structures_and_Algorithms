from collections import deque


graph1 = {
    "a": ["d", "f"],
    "b": ["c"],
    "c": ["b", "c", "d", "e"],
    "d": ["a", "c"],
    "e": ["c"],
    "f": ["a"]
}
graph2 = {
    "a": ["d", "f"],
    "b": ["c", "b"],
    "c": ["b", "c", "d", "e"],
    "d": ["a", "c"],
    "e": ["c"],
    "f": ["a"]
}


def dfs(graph, node, visited):
  if node not in visited:
    print(node)
    visited.add(node)
    for neighbor in graph[node]:
      dfs(graph, neighbor, visited)


visited = set()
dfs(graph1, 'a', visited)
print("\n")
visited = set()
dfs(graph2, 'a', visited)
print("\n")




def bfs(graph, start):
  visited = set()
  queue = deque()

  visited.add(start)
  queue.append(start)

  while queue:
    node = queue.popleft()
    print(node)

    # Explore neighbors of the current node
    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)



bfs(graph1, 'a')
print("\n")
bfs(graph2, 'a')
