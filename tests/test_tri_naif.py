# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from solver import Solver

class Test_Tri_Naif(unittest.TestCase):
    def test_grid1(self):
        grid = Grid.grid_from_file("input/grid2.in")
        solver = Solver()
        solver.tri_naif(grid)
        
        self.assertEqual(grid.state, [[1,2,3], [4,5,6], [7,8,9]])


if __name__ == '__main__':
    unittest.main()
