class Grid:
    
    def __init__(self, ox, oy, oz, nx, ny, nz, sx, sy, sz): #Construtor, é o método que é executado automaticamente, quando 
        
        #Definindo os atributos do objeto. O módulo construtor sempre roda quando instanciamos um objeto
        self.ox = ox
        self.oy = oy
        self.oz = oz
        
        self.nx = nx
        self.ny = ny
        self.nz = nz
    
        self.sx = sx
        self.sy = sy
        self.sz = sz    
    
    def auto_grid(self, coords_x, coords_y, coords_z, sx, sy, sz): #O método auto_grid recebe as coordenadas x, y, z de um point set e as dimensões dos blocos. Esse método altera os valores de nx, ny, nz e ox, oy, oz para cobrir todo o point set.
       
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
        
        dist_z = np.max(coords_z) - np.min(coords_z)
        nz = int(dist_z / sz)
        oz = np.min(coords_z)
        
        self.oz = oz
        self.nz = nz
        self.sz = sz 
        
    def number_of_blocks():
        block_count = self.nx*self.ny*self.nz