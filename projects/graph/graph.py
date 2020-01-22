# """
# Simple graph implementation
# """
# from util import Stack, Queue  # These may come in handy


# class Graph:

#     """Represent a graph as a dictionary of vertices mapping labels to edges."""

#     def __init__(self):
#         self.vertices = {}

#     def add_vertex(self, vertex_id):
#         """
#         Add a vertex to the graph.
#         """
#         self.vertices[vertex_id] = set()

#     def add_edge(self, v1, v2):
#         """
#         Add a directed edge to the graph.

#         If both exist, add a connection from v1 to v2
#         """
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#         else:
#             raise IndexError("That vertex does not exist.")

#     def get_neighbors(self, vertex_id):
#         """
#         Get all neighbors (edges) of a vertex.
#         """
#         if self.vertices[vertex_id] == set():
#             return None
#         return self.vertices[vertex_id]

#     def bft(self, starting_vertex):
#         """
#         Print each vertex in breadth-first order
#         beginning from starting_vertex.
#         """
#         # Create an empty Queue and enqueue the starting vertex ID
#         q = Queue()
#         q.enqueue(starting_vertex)
#         # Create an empty Set to store visited vertices
#         visited = set()
#         # While the Queue is not empty...
#         while q.size() > 0:
#             # Dequeue the first vertex
#             v = q.dequeue()
#             # If that vertex has not been visited...
#             if v not in visited:
#                 # Mark it as visited
#                 print(v)
#                 visited.add(v)
#                 # Then add all of its neighbors to the back of the Queue
#                 for neighbor in self.get_neighbors(v):
#                     q.enqueue(neighbor)

#     def dft(self, starting_vertex):
#         """
#         Print each vertex in depth-first order
#         beginning from starting_vertex.
#         """
#         # Create an empty Stack and push the starting vertex ID
#         s = Stack()
#         s.push(starting_vertex)
#         # Create an empty Set to store visited vertices
#         visited = set()
#         # While the Stack is not empty...
#         while s.size() > 0:
#             # Pop the last vertex
#             v = s.pop()
#             # If that vertex has not been visited...
#             if v not in visited:
#                 # Mark it as visited
#                 print(v)
#                 visited.add(v)
#                 # Then add all of its neighbors to the top of the Stack
#                 for neighbor in self.get_neighbors(v):
#                     s.push(neighbor)

#     def dft_recursive(self, starting_vertex, visited=set()):
#         """
#         Print each vertex in depth-first order
#         beginning from starting_vertex.

#         This should be done using recursion.
#         """
#         # Check to see if the vertex is in the visited Set
#         # If not, mark the vertex as visited and print
#         if starting_vertex not in visited:
#             visited.add(starting_vertex)
#             print(starting_vertex)
#             # Call on the vertex's neighbors
#             for neighbor in self.get_neighbors(starting_vertex):
#                 self.dft_recursive(neighbor, visited)
#         # Otherwise, return
#         else:
#             return

#         self.dft_recursive(starting_vertex, visited)

#     def bfs(self, starting_vertex, destination_vertex):
#         """
#         Return a list containing the shortest path from
#         starting_vertex to destination_vertex in
#         breath-first order.
#         """
#         # Create an empty Queue and enqueue A PATH TO the starting vertex ID
#         q = Queue()
#         q.enqueue([starting_vertex])
#         # Create a Set to store visited vertices
#         visited = set()
#         # While the queue is not empty...
#         while q.size() > 0:
#             # Dequeue the first PATH
#             vertex_path = q.dequeue()
#             # Grab the last vertex from the PATH
#             last_vertex = vertex_path[-1]
#             # If that vertex has not been visited...
#             if last_vertex not in visited:
#                 # CHECK IF IT'S THE TARGET
#                 if last_vertex == destination_vertex:
#                     # IF SO, RETURN PATH
#                     return vertex_path
#                 # Mark it as visited...
#                 visited.add(last_vertex)
#                 # Then add A PATH TO its neighbors to the back of the Queue
#                 for neighbor in self.get_neighbors(last_vertex):
#                     # COPY THE PATH
#                     neighbor_path = vertex_path + [neighbor]
#                     # APPEND THE NEIGHBOR TO THE BACK
#                     q.enqueue(neighbor_path)
#         return f"No path exists between {starting_vertex} and {destination_vertex}."

#     def dfs(self, starting_vertex, destination_vertex):
#         """
#         Return a list containing a path from
#         starting_vertex to destination_vertex in
#         depth-first order.
#         """
#         # Create an empty Queue and push A PATH TO the starting vertex ID
#         s = Stack()
#         s.push([starting_vertex])
#         # Create a Set to store visited vertices
#         visited = set()
#         # While the Stack is not empty...
#         while s.size() > 0:
#             # Pop the last PATH
#             vertex_path = s.pop()
#             # Grab the last vertex from the PATH
#             last_vertex = vertex_path[-1]
#             # If that vertex has not been visited...
#             if last_vertex not in visited:
#                 # CHECK IF IT'S THE TARGET
#                 if last_vertex == destination_vertex:
#                     # IF SO, RETURN PATH
#                     return vertex_path
#                 # Mark it as visited...
#                 visited.add(last_vertex)
#                 # Then add A PATH TO its neighbors to the back of the Stack
#                 for neighbor in self.get_neighbors(last_vertex):
#                     # COPY THE PATH
#                     neighbor_path = vertex_path + [neighbor]
#                     # APPEND THE NEIGHBOR TO THE BACK
#                     s.push(neighbor_path)
#         return f"No path exists between {starting_vertex} and {destination_vertex}."

#     def dfs_recursive(self, starting_vertex, destination_vertex, path=[], visited=set()):
#         """
#         Return a list containing a path from
#         starting_vertex to destination_vertex in
#         depth-first order.

#         This should be done using recursion.
#         """

#         path = path + [starting_vertex]
#         visited.add(starting_vertex)

#         if starting_vertex == destination_vertex:
#             return path
#         for neighbor in self.get_neighbors(starting_vertex):
#             if neighbor not in visited:
#                 new_path = self.dfs_recursive(
#                     neighbor, destination_vertex, path, visited)
#                 if new_path is not None:
#                     return new_path
#         return None


# if __name__ == '__main__':
#     graph = Graph()  # Instantiate your graph
#     # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
#     graph.add_vertex(1)
#     graph.add_vertex(2)
#     graph.add_vertex(3)
#     graph.add_vertex(4)
#     graph.add_vertex(5)
#     graph.add_vertex(6)
#     graph.add_vertex(7)
#     graph.add_edge(5, 3)
#     graph.add_edge(6, 3)
#     graph.add_edge(7, 1)
#     graph.add_edge(4, 7)
#     graph.add_edge(1, 2)
#     graph.add_edge(7, 6)
#     graph.add_edge(2, 4)
#     graph.add_edge(3, 5)
#     graph.add_edge(2, 3)
#     graph.add_edge(4, 6)

#     '''
#     Should print:
#         {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
#     '''
#     # print(graph.vertices)

#     '''
#     Valid BFT paths:
#         1, 2, 3, 4, 5, 6, 7
#         1, 2, 3, 4, 5, 7, 6
#         1, 2, 3, 4, 6, 7, 5
#         1, 2, 3, 4, 6, 5, 7
#         1, 2, 3, 4, 7, 6, 5
#         1, 2, 3, 4, 7, 5, 6
#         1, 2, 4, 3, 5, 6, 7
#         1, 2, 4, 3, 5, 7, 6
#         1, 2, 4, 3, 6, 7, 5
#         1, 2, 4, 3, 6, 5, 7
#         1, 2, 4, 3, 7, 6, 5
#         1, 2, 4, 3, 7, 5, 6
#     '''
#     # graph.bft(1)

#     '''
#     Valid DFT paths:
#         1, 2, 3, 5, 4, 6, 7
#         1, 2, 3, 5, 4, 7, 6
#         1, 2, 4, 7, 6, 3, 5
#         1, 2, 4, 6, 3, 5, 7
#     '''
#     # graph.dft(1)
#     # graph.dft_recursive(1)

#     '''
#     Valid BFS path:
#         [1, 2, 4, 6]
#     '''
#     # print(graph.bfs(1, 6))

#     '''
#     Valid DFS paths:
#         [1, 2, 4, 6]
#         [1, 2, 4, 7, 6]
#     '''
#     # print(graph.dfs(1, 6))
#     print(graph.dfs_recursive(1, 6))

"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        If both exist, and a connection from v1 to v2
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue/stack as appropriate
        queue = Queue()
        # Put the starting point in that
        queue.enqueue(starting_vertex)
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while queue.size() > 0:
            #    Pop the first item
            vertex = queue.dequeue()
        #    If not visited
            if vertex not in visited:
                #       DO THE THING!
                print(vertex)
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    #           Add that edge to the queue/stack
                    queue.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a queue/stack as appropriate
        stack = Stack()
        # Put the starting point in that
        stack.push(starting_vertex)
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while stack.size() > 0:
            #    Pop the first item
            vertex = stack.pop()
        #    If not visited
            if vertex not in visited:
                #       DO THE THING!
                print(vertex)
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    #           Add that edge to the queue/stack
                    stack.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue/stack as appropriate
        queue = Queue()
        # Put the starting point in that
        # Enstack a list to use as our path
        queue.enqueue([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while queue.size() > 0:
            #    Pop the first item
            path = queue.dequeue()
            vertex = path[-1]
        #    If not visited
            if vertex not in visited:
                if vertex == destination_vertex:
                    # Do the thing!
                    return path
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    # Copy path to avoid pass by reference bug
                    # Make a copy of path rather than reference
                    new_path = list(path)
                    new_path.append(next_vert)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a queue/stack as appropriate
        stack = Stack()
        # Put the starting point in that
        # Enstack a list to use as our path
        stack.push([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while stack.size() > 0:
            #    Pop the first item
            path = stack.pop()
            vertex = path[-1]
        #    If not visited
            if vertex not in visited:
                if vertex == destination_vertex:
                    # Do the thing!
                    return path
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    # Copy path to avoid pass by reference bug
                    # Make a copy of path rather than reference
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, target_value, path=None, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == target_value:
            return path
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                new_path = self.dfs_recursive(
                    child_vert, target_value, path, visited)
                if new_path:
                    return new_path
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print("Printing graph.vertices")
    print(graph.vertices)
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("Running bft")
    graph.bft(1)
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("Running dft")
    graph.dft(1)
    print("Running dft_recursive")
    graph.dft_recursive(1)
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("Running BFS")
    print(graph.bfs(1, 6))
    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("Running DFS")
    print(graph.dfs(1, 6))
    print("Running dfs_recursive")
    print(graph.dfs_recursive(1, 6))
