"""
This is the grid module. It contains the Grid class and its associated methods.
"""
import matplotlib.pyplot as plt
import random
import numpy as np

class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The intiail state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state

    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

    def is_sorted(self):
        m=self.m
        n=self.n 
        return self.state == [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]
        

    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        x1,y1 = cell1
        x2,y2 = cell2
        
        if x1 < 0 or y1 < 0  or x2 < 0 or y2 < 0:
            raise Exception("Indices négatifs")
        if x1 >= self.m or y1 >= self.n or x2 >= self.m or y2 >= self.n:
            raise Exception("indices plus grand que m ou n")
        if abs(x1-x2)+abs(y1-y2)>1:
            raise Exception("Impossible swap")
        self.state[x1][y1],self.state[x2][y2]=self.state[x2][y2],self.state[x1][y1]
    

    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        for cell_pair in cell_pair_list:
            self.swap(cell_pair[0] , cell_pair[1])
            
    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid


    def graphique_grille(self):
  
        plt . figure ( figsize =(8 ,8) ) # Cree une nouvelle figure avec une taille de 8x8 pouces .
        ax = plt . gca () # cree les axes
        ax.invert_yaxis ()# inverse l’axe y pour avoir (0 ,0) en haut a gauche
        for i in range ( self . m ) :
            for j in range ( self . n ) :
                plt.text (j , i , str ( self . state [ i ][ j ]) , color = 'black', fontsize =12)
        plt.grid(True,which ='both', color = 'black', linewidth =1) # affiche la grille
        ax.set_xticks( np.arange ( -0.5 , self .n , 1) )# Definit les marqueurs des axes x a

        #intervalles reguliers allant de 0 a self .n - 1
        ax.set_yticks (np.arange( -0.5 , self .m , 1) )
        ax.set_xticklabels ([]) # Efface les etiquettes de l’axe x.
        ax.set_yticklabels ([])
        plt.title (" Affichage graphique de la grille ")
        plt.show ()

        return f"<la matrice est de taille : ({self.m}, {self.n}) >"