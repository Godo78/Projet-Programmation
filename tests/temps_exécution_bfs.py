import time

t= "test"
def time_bfs_amélioré():
    initial_state = [[4,1,6],[5,3,2]]
    g = Grid(2, 3, initial_state)
    Solu = Solver()
    début = time.time()
    Solu.tri_bfs_amélioré(g)
    fin = time.time()
    str = f"Le temps d'exécution de la fonction est de {fin - début} secondes"
    return str


print(time_bfs_amélioré())

def time_bfs_naif():
    initial_state = [[4,1,6],[5,3,2]]
    g = Grid(2, 3, initial_state)
    Solu = Solver()
    début = time.time()
    Solu.tri_bfs_naif(g)
    fin = time.time()
    str = f"Le temps d'exécution de la fonction est de {fin - début} secondes"
    return str


print(time_bfs_naif())