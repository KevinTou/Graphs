from graph import Graph
from util import Stack, Queue


# def earliest_ancestor(ancestors, starting_node):
#     graph = Graph()
#     stack = Stack()

#     visited = set()

#     # Add parent and child pairs to graph as vertices
#     for parent, child in ancestors:
#         graph.add_vertex(parent)
#         graph.add_vertex(child)

#     # Add the connections between parent and child as vertices
#     for parent, child in ancestors:
#         graph.add_edge(parent, child)

#     # Add starting node to stack
#     stack.push(starting_node)

#     # Initialize ancestor value with -1 (or false)
#     ancestor = -1

#     # Go through the stack
#     while stack.size() > 0:
#         current = stack.pop()
#         # Go through the list of vertices and add all the parents that the current is a child of
#         for vertex in graph.vertices:
#             if current in graph.get_neighbors(vertex) and current not in visited:
#                 visited.add(current)
#                 stack.push(vertex)

#         # Update ancestor based on whether or not current changed (has a parent)
#         if current == starting_node:
#             ancestor = -1
#         else:
#             ancestor = current

#     # Return the earliest ancestor (if there was one)
#     return ancestor

# start: 1
# ancestor: 10


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

def earliest_ancestor(ancestors, starting_node):
    # Build the graph
    graph = Graph()

    for parent, child in ancestors:
        if parent not in graph.vertices:
            graph.add_vertex(parent)
        if child not in graph.vertices:
            graph.add_vertex(child)
        # Build in reverse order
        graph.add_edge(child, parent)

    # Do a BFS (storing the path)
    q = Queue()
    q.enqueue([starting_node])
    max_path_len = 1
    earliest_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        # If the path is longer or equal and the value is smaller, or if the path is longer)
        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            max_path_len = len(path)
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    return earliest_ancestor
