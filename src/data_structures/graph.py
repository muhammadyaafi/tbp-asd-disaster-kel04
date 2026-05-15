class EdgeNode: 
    def __init__(self, dest, jarak, kapasitas): 
        self.dest = dest 
        self.jarak = jarak 
        self.kapasitas = kapasitas 
        self.next = None

class GraphRute: 
    def __init__(self): 
        self.adj = {} 
    
    def tambah_node(self, kode): 
        """Big-O: O(1).""" 
        pass  # TODO: implementasikan 
    
    def tambah_rute(self, u, v, jarak, kapasitas): 
        """Big-O: O(1). Graf tidak berarah.""" 
        pass  # TODO: implementasikan 
        
    def tetangga(self, u): 
        """Big-O: O(deg).""" 
        pass  # TODO: implementasikan 
    
    def bfs_akses(self, depot): 
        """BFS dari depot. Big-O: O(V+E).""" 
        pass  # TODO: gunakan Queue Linked List sendiri