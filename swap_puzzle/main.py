from grid import Grid
from solver import Solver

initial_state = [[4,2,1],[6,3,5]]
g = Grid(2, 3, initial_state)
print(g)

Solu = Solver()
print(Solu.tri_naif(g))
    
'''
data_path = "../input/"
file_name = data_path + "grid0.in"



g2 = Grid.grid_from_file(file_name)
print(g2)
'''