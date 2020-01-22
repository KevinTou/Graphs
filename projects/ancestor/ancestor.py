from graph import Graph
from util import Stack, Queue


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    stack = Stack()

    visited = set()

    # Add parent and child pairs to graph as vertices
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)

    # Add the connections between parent and child as vertices
    for parent, child in ancestors:
        graph.add_edge(parent, child)

    # Add starting node to stack
    stack.push(starting_node)
    ancestor = -1

    while stack.size() > 0:
        current = stack.pop()
        for vertex in graph.vertices:
            if current in graph.get_neighbors(vertex) and current not in visited:
                visited.add(current)
                stack.push(vertex)

        if current == starting_node:
            ancestor = -1
        else:
            ancestor = current

    return ancestor

# start: 1
# ancester: 10


'''
If a vertex is NOT a child of any vertex, it is a parent

Loop through the list of vertices and check to see if the starting_node is within
the list of neighbors, add those values into a stack/queue and repeat for those values until
you run through the list without adding to the stack or queue
'''

# vertices {
# parent: {child}
# 1: {3},
# 2: {3},
# 3: {6},
# 4: {8, 5},
# 5: {6, 7},
# 6: set(),
# 7: set(),
# 8: {9},
# 9: set(),
# 10: {1}
# 11: {8},
# }


# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
#                   (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(test_ancestors, 1))  # 10
# print(earliest_ancestor(test_ancestors, 2))  # -1
# print(earliest_ancestor(test_ancestors, 3))  # 10
# print(earliest_ancestor(test_ancestors, 4))  # -1
# print(earliest_ancestor(test_ancestors, 5))  # 4
# print(earliest_ancestor(test_ancestors, 6))  # 10
# print(earliest_ancestor(test_ancestors, 7))  # 4
# print(earliest_ancestor(test_ancestors, 8))  # 4
# print(earliest_ancestor(test_ancestors, 9))  # 4
# print(earliest_ancestor(test_ancestors, 10))  # -1
# print(earliest_ancestor(test_ancestors, 11))  # -1
