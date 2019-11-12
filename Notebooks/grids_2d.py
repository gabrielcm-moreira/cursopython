import numpy as np
import itertools
class Grid:
            
    def __init__(self, ox, oy, nx, ny, sx, sy): #Construtor, é o método que é executado automaticamente, quando 

        #Definindo os atributos do objeto. O módulo construtor sempre roda quando instanciamos um objeto
        self.ox = ox
        self.oy = oy

        self.nx = nx
        self.ny = ny

        self.sx = sx
        self.sy = sy   

    def auto_grid(self, coords_x, coords_y, sx, sy):

        """
        O método auto_grid recebe as coordenadas x, y, z de um point set e as dimensões dos blocos. 
        Esse método altera os valores de nx, ny, nz e ox, oy, oz para cobrir todo o point set.
        """

        dist_x = np.max(coords_x) - np.min(coords_x)
        nx = int(dist_x / sx)
        ox = np.min(coords_x)

        self.ox = ox
        self.nx = nx
        self.sx = sx

        dist_y = np.max(coords_y) - np.min(coords_y)
        ny = int(dist_y / sy)
        oy = np.min(coords_y)

        self.oy = oy
        self.ny = ny
        self.sy = sy
        
        x_coords = np.arange(ox, ox+nx*sx, sx)
        y_coords = np.arange(oy, oy+ny*sy, sy)
    
        coords_array = []
        
        for x, y in itertools.product(x_coords, y_coords):
            coords_array.append([x,y])
            
        return np.array(coords_array)

    def number_of_blocks():
        block_count = self.nx*self.ny*self.nz