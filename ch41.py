"""
    q41.py
    ~~~~~~
    Route Between Nodes: Given a directed graph, design an algorithm
    to find out whether there is a route between two nodes.
"""
import unittest


def dfs_visited_iter(node, graph):
    visited = []
    stack = [node]

    while stack:
        current = stack.pop()
        stack.extend(graph[current])
        if current not in visited:
            visited.append(current)
    return visited
    
def dfs_visited_re(node, graph, visited=None):
    if visited is None:
        visited = []
    for child in graph[node]:
        if child not in visited:
            visited.append(child)
        dfs_visited_re(child, graph, visited)
    return visited

def bfs_visited(node, graph):
    visited = []
    queue = [node]

    while queue:
        current = queue.pop()
        queue[0:0] = [neighbor for neighbor in graph[current] if neighbor not in visited]
        if current not in visited:
            visited.append(current)
    return visited


def is_path(node1, node2, graph, method):
    return node2 in method(node1, graph)

class TestIsPath(unittest.TestCase):
    def setUp(self):
        self.graph1 = {
            'A': ['B', 'D'],
            'B': [],
            'C': [],
            'D': ['E'],
            'E': ['C'],
            'F': ['C'],
        }
        self.graph2 = {
            'A': ['B', 'C', 'E'],
            'B': ['D'],
            'C': [],
            'D': ['G'],
            'E': [],
            'F': ['E', 'C'],
            'G': ['C'],
        }

    def test_is_path_dfs_iter(self):
        self.assertFalse(is_path('A', 'F', self.graph1, dfs_visited_iter))
        self.assertTrue(is_path('A', 'C', self.graph2, dfs_visited_iter))

    def test_is_path_dfs_recursive(self):
        self.assertFalse(is_path('A', 'F', self.graph1, dfs_visited_re))
        self.assertTrue(is_path('A', 'C', self.graph2, dfs_visited_re))

    def test_is_path_bfs(self):
        self.assertFalse(is_path('A', 'F', self.graph1, bfs_visited))
        self.assertTrue(is_path('A', 'C', self.graph2, bfs_visited))


if __name__ == '__main__':
    unittest.main()