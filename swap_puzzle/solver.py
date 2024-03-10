from grid import Grid


class Solver(): 
    """
    A solver class, to be implemented.
    """
    '''
    def get_solution(self):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
    '''  
    def tri_naif(self, grid):
        grosse_liste = [] # On initialise la liste de tous les swaps réalisés pour trier la grille
        for i in range(1,grid.m*grid.n + 1):
            for k in range(grid.m):
                for j in range(grid.n):
                    if grid.state[k][j] == i:
                        indice_ligne = (i-1)//grid.n  # On réalise une division euclidienne pour déterminer la colonne "objectif"
                        indice_colonne = (i-1)%grid.n # et la ligne "objectif" pour chaque entier entre 1 et m*n.
                        L=[]
                        if j > indice_colonne : 
                            compteur = j # On décrémente le compteur pour se déplacer vers la gauche
                            while compteur - indice_colonne > 0:
                                L.append(((k,compteur),(k, compteur - 1)))
                                compteur -= 1
                        elif j < indice_colonne : 
                            compteur = j # On incrémente le compteur pour se déplacer vers la droite
                            while indice_colonne - compteur > 0:
                                L.append(((k,compteur),(k, compteur + 1)))
                                compteur += 1
                        if k > indice_ligne: 
                            compteur = k # On décrémente le compteur pour se déplacer vers le bas
                            while compteur - indice_ligne > 0:
                                L.append(((compteur, indice_colonne),(compteur - 1, indice_colonne)))
                                compteur -= 1
                        elif k < indice_ligne: 
                            compteur = k # On incrémente le compteur pour se déplacer vers le haut
                            while indice_ligne - compteur > 0:
                                L.append(((compteur, indice_colonne),( compteur + 1, indice_colonne)))
                                compteur += 1
                        grid.swap_seq(L)
                        grosse_liste = grosse_liste + L

        return grid.state , grosse_liste , len(grosse_liste) # On renvoie la grille triée, la liste de tous les swaps exécutés
                                                             # et le nombre de swaps exécutés

    def tri_bfs_naif(self, grid):
        m = grid.m
        n = grid.n
        grid = Grid(m, n, grid.state)
        G = grid.graph_grilles()
        dst = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]
        node1 = convert1(grid.state)
        node2 = convert1(dst)
        return G.bfs(node1, node2), len(G.bfs(node1, node2))-1
    
    def tri_bfs_amélioré(self, grid):
        m = grid.m
        n = grid.n
        grid = Grid(m, n, grid.state)
        G = grid.graph_grilles_amélioré()
        dst = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]
        node1 = convert1(grid.state)
        node2 = convert1(dst)
        return G.bfs(node1, node2), len(G.bfs(node1, node2))-1

    def tri_A_star(self, grid):
        m = grid.m
        n = grid.n
        grid = Grid(m, n, grid.state)
        G = grid.graph_grilles_A_star()
        dst = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]
        node1 = convert1(grid.state)
        node2 = convert1(dst)
        return G.bfs(node1, node2), len(G.bfs(node1, node2))-1

#fonction convert1 dont on a 
def convert1(M):
    tupledetuples = ()
    for element in M:
        tupledetuples = tupledetuples + (tuple(element),)
    return tupledetuples


        