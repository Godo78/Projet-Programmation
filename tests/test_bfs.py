# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 

from graph import Graph

class Test_BFS(unittest.TestCase):
    def test_bfs1(self):
        g = Graph.graph_from_file("input/graph1.in")
        self.assertEqual(g.bfs(2,18), [2,15,18])
    def test_bfs2(self):
        g = Graph.graph_from_file("input/graph2.in")
        self.assertEqual(g.bfs(4,12), [4,15,16,12])

if __name__ == '__main__':
    unittest.main()
