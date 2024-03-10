
from grid import Grid
from solver import Solver
'''
initial_state = [[4,1,6],[5,3,2]]
g = Grid(2, 3, initial_state)

print(g.state)

print(g.graph_grilles_amélioré())

Solu = Solver()
print(Solu.tri_bfs_amélioré(g))
'''
'''
print(g.graphique_grille())
print("effectuer")

data_path = "../input/"
file_name = data_path + "grid0.in"



g2 = Grid.grid_from_file(file_name)
print(g2)

initial_state = [[1,2,3]]
d = Grid(1,3,initial_state)

'''
