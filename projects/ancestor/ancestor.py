from collections import deque


class Stack():
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()

    def size(self):
        return len(self.stack)


def earliest_ancestor(ancestors, starting_node):
    graph = dict()
    for tpl in ancestors:
        if tpl[1] not in graph:
            graph[tpl[1]] = set()
        graph[tpl[1]].add(tpl[0])

    def solve(starting_vertex):
        nonlocal graph
        if starting_vertex not in graph:
            return -1

        distances = dict()

        def dfs(starting_vertex, callback):
            visited = set()
            stack = Stack()
            stack.push([starting_vertex])
            while stack.size() > 0:
                path = stack.pop()
                vertex = path[-1]  # last element in the array storing the path
                if vertex not in visited and vertex in graph:
                    for neighbor in graph[vertex]:
                        path_new = path[:]  # path.copy()
                        path_new.append(neighbor)
                        stack.push(path_new)
                        if neighbor not in graph:
                            callback(neighbor, path_new)
                            continue
                    visited.add(vertex)

        def callback(neighbor, path_new):
            distances[neighbor] = len(path_new)

        dfs(starting_vertex, callback)
        return min([k for k, v in distances.items() if v == max([v for k, v in distances.items()])])
    return solve(starting_node)


lca_index = 9
lca_arr = [
    (1, 3),
    (2, 3),
    (3, 6),
    (5, 6),
    (5, 7),
    (4, 5),
    (4, 8),
    (8, 9),
    (11, 8),
    (10, 1)
]

print(earliest_ancestor(lca_arr, lca_index))

# ```
#  10
#  /
# 1   2   4  11
#  \ /   / \ /
#   3   5   8
#    \ / \   \
#     6   7   9
# ```


# ```
# Example input
#   6

#   1 3
#   2 3
#   3 6
#   5 6
#   5 7
#   4 5
#   4 8
#   8 9
#   11 8
#   10 1
# Example output
#   10
# ```
