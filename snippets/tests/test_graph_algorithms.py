import unittest
from snippets.graph_algorithms import dijkstra, get_path
from snippets.simple_graph import Graph

class DijkstraTest(unittest.TestCase):

    def test_simple(self):
        G = Graph(3)
        G.add_edge(1,2,3)
        G.add_edge(1,3,4)

        d, p = dijkstra(G.adj_list, G.w, 1)
        self.assertTrue(d[2],3)
        self.assertTrue(d[3],4)

    def test_two_path(self):
        G = Graph(4)
        G.add_edge(1,2,3)
        G.add_edge(1,3,2)
        G.add_edge(2,4,2)
        G.add_edge(3,4,1)

        d, p = dijkstra(G.adj_list, G.w, 1)
        self.assertTrue(d[4],3)

if __name__ == '__main__':
    unittest.main()



