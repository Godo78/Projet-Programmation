# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from graph import Graph
#on teste si en partant de la matrice [[1,2,3]] on obtient bien un graphe 
#avec toutes les grilles possibles

class Test_Graph_Grilles(unittest.TestCase):
    def test_graph_grilles(self):
        initial_state = [[1,2,3]]
        grid = Grid(1, 3, initial_state)
        D = grid.graph_grilles()
        self.assertEqual(D.graph, {((1, 2, 3),): [((2, 1, 3),), ((1, 3, 2),)], 
        ((2, 1, 3),): [((1, 2, 3),), ((2, 3, 1),)], 
        ((1, 3, 2),): [((1, 2, 3),), ((3, 1, 2),)], 
        ((2, 3, 1),): [((2, 1, 3),), ((3, 2, 1),)], 
        ((3, 1, 2),): [((1, 3, 2),), ((3, 2, 1),)], 
        ((3, 2, 1),): [((2, 3, 1),), ((3, 1, 2),)]})

if __name__ == '__main__':
    unittest.main()
