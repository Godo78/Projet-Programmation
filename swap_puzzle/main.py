
from grid import Grid
from solver import Solver

initial_state = [[7,6,3],[5,4,1]]
g = Grid(2, 3, initial_state)
Solu = Solver()
print(Solu.tri_A_star(g))


#print(g.graph_grilles_A_star())



'''
data_path = "../input/"
file_name = data_path + "grid0.in"



g2 = Grid.grid_from_file(file_name)
print(g2)

initial_state = [[1,2,3]]
d = Grid(1,3,initial_state)

'''
