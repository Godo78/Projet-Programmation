# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 

from grid import Grid

class Test_GRID(unittest.TestCase):
    def test_grid(self):
        initial_state = [[1,2,3],[4,5,6],[7,8,9]]
        g = Grid(3,3, initial_state)
        self.assertEqual(g.convert(), ((1,2,3),(4,5,6),(7,8,9)))

if __name__ == '__main__':
    unittest.main()