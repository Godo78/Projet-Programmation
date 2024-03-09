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
    def tri_naif(self,grid):
        
        grosse_liste = []
        for i in range(1,grid.m*grid.n + 1):
            for k in range(grid.m):
                for j in range(grid.n):
                    if grid.state[k][j] == i:
                        indice_ligne = (i-1)//grid.n
                        indice_colonne = (i-1)%grid.n
                        L=[]
                        if j > indice_colonne : 
                            compteur = j
                            while compteur - indice_colonne > 0:
                                L.append(((k,compteur),(k, compteur - 1)))
                                compteur -= 1
                        elif j < indice_colonne : 
                            compteur = j
                            while indice_colonne - compteur > 0:
                                L.append(((k,compteur),(k, compteur + 1)))
                                compteur += 1
                        if k > indice_ligne: 
                            compteur = k
                            while compteur - indice_ligne > 0:
                                L.append(((compteur, indice_colonne),(compteur - 1, indice_colonne)))
                                compteur -= 1
                        elif k < indice_ligne: 
                            compteur = k
                            while indice_ligne - compteur > 0:
                                L.append(((compteur, indice_colonne),( compteur + 1, indice_colonne)))
                                compteur += 1
                        grid.swap_seq(L)
                        grosse_liste = grosse_liste + L

        return grid.state , grosse_liste , len(grosse_liste)
