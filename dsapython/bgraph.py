from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            for neighbour in graph[vertex]:
                if neighbour not in vertex:
                    queue.append(neighbour)


graph = {"A": ["B", "C", "D"], "B": ["A"], "C": ["D", "A"], "D": ["A", "C"]}

bfs(graph, 
'A')