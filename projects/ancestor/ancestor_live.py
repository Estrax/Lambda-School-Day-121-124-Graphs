from collections import deque
import operator


class Stack():
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def earliest_ancestor(ancestors, starting_node):
    graph = dict()  # storing children as keys and parents as values in set (graph edges directions rotated)

    for tpl in ancestors:
        if tpl[1] not in graph:
            graph[tpl[1]] = set()
        graph[tpl[1]].add(tpl[0])

    def dfs(starting_vertex):
        nonlocal graph
        if starting_vertex not in graph:
            return -1
        distances = dict()

        visited = set()
        stack = Stack()
        stack.push([starting_vertex])
        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]
            if vertex not in visited:
                if vertex in graph:
                    for neighbor in graph[vertex]:
                        path_new = path[:]
                        path_new.append(neighbor)
                        stack.push(path_new)
                        if neighbor not in graph:
                            # adding key-value pairs storing the vertex and its distance from the starting vertex
                            distances[neighbor] = len(path_new)
                            continue
                    visited.add(vertex)
        # selecting the smallest one among the furthest ones from starting vertex
        return min([k for k, v in distances.items() if v ==
                    max([v for k, v in distances.items()])])
    return dfs(starting_node)
