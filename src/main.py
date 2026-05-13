import numpy as np, time, random 
from dataclasses import dataclass 
from typing import Optional, List, Dict, Tuple

np.random.seed(47) 
random.seed(47) 
  
LEVEL_BENCANA = {'KRITIS': 1, 'SEDANG': 2, 'RINGAN': 3} 
JENIS_BANTUAN = ['MAKANAN', 'AIR', 'OBAT', 'SELIMUT', 'TENDA'] 
  
@dataclass 
class Lokasi: 
    kode: str 
    nama: str 
    level: int 
    populasi: int 
    status: int = 0 
  
@dataclass 
class Bantuan: 
    bantuan_id: int 
    jenis: str 
    jumlah: int 
    asal: str 
    tujuan: str 
    prioritas: int 
  
class LLNode: 
    def __init__(self, data=None): 
        self.data = data 
        self.next = None 

class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularQueue:
    """
    Circular Queue berbasis array (fixed capacity).
    Mensimulasikan buffer FIFO stok gudang.
    FIFO = produk pertama masuk, pertama keluar (hindari kadaluarsa).
    """
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.buffer = [None] * kapasitas
        self.front = 0
        self.rear = 0
        self._size = 0
    def enqueue(self, produk):
        """Big-O: O(1). Kembalikan False jika penuh."""
        pass # TODO: implementasikan logika circular

    def dequeue(self):
        """Big-O: O(1). Ambil produk terlama (FIFO)."""
        pass # TODO: implementasikan

    def is_full(self):
        return self._size == self.kapasitas
    
    def is_empty(self):
        return self._size == 0

class PriorityQueueBantuan: 
    """Lokasi KRITIS (level=1) selalu dilayani lebih dulu.""" 
    def __init__(self): 
        self.head = None 
        self._size = 0 
    
    def enqueue(self, bantuan): 
        """Big-O: O(n) insertion terurut prioritas.""" 
        pass  # TODO: implementasikan 
    
    def dequeue(self): 
        """Big-O: O(1).""" 
        pass  # TODO: implementasikan 
    
    def __len__(self): 
        return self._size 
    
class Stack: 
    def __init__(self): 
        self.top = None 
        self._size = 0 
    
    def push(self, data): 
        pass  # TODO: Big-O O(1) 
    
    def pop(self): 
        pass  # TODO: Big-O O(1) 
    
    def peek(self): 
        return self.top.data if self.top else None 
    
    def to_list(self): 
        pass  # TODO: kembalikan list dari top ke bottom

class BSTNodeLok: 
    def __init__(self, lokasi): 
        self.lokasi = lokasi 
        self.left = self.right = None 
    
class BSTLokasi: 
    def __init__(self): 
        self.root = None 
    
    def insert(self, lokasi): 
        """Big-O: O(log n). Kunci = lokasi.kode.""" 
        pass  # TODO: implementasikan 
    
    def search(self, kode): 
        """Big-O: O(log n).""" 
        pass  # TODO: implementasikan 
    
    def update_level(self, kode, level): 
        """Big-O: O(log n).""" 
        pass  # TODO: implementasikan 
    
    def inorder(self): 
        """Big-O: O(n).""" 
        pass  # TODO: implementasikan 
  
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
  
def dijkstra_logistik(graph, depot): 
    """Shortest path dari depot. Big-O: O(V^2+E).""" 
    INF = float('inf') 
    dist = {v: INF for v in graph.adj} 
    parent = {v: None for v in graph.adj} 
    dist[depot] = 0 
    visited = set() 
    # TODO: implementasikan
    return dist, parent 

def generate_peta_bencana(n_lokasi=35, n_depot=3, seed=47): 
    rng = np.random.default_rng(seed) 
    lokasi = [] 
    for i in range(n_depot): 
        lokasi.append(Lokasi(f'DEPOT_{i}', f'Gudang Logistik {i}', 3, 0)) 
    for i in range(n_lokasi): 
        kode = f'L{i:03d}' 
        level = int(rng.choice([1,2,3], p=[0.2, 0.4, 0.4])) 
        pop = int(rng.integers(100, 5000)) 
        lokasi.append(Lokasi(kode, f'Desa/Kelurahan-{i}', level, pop)) 
    n_total = len(lokasi) 
    perm = rng.permutation(n_total) 
    edges = [] 
    for i in range(1, n_total): 
        u = lokasi[perm[i-1]].kode 
        v = lokasi[perm[i]].kode 
        edges.append((u, v, int(rng.integers(5, 100)), int(rng.integers(1, 5)))) 
    for _ in range(15): 
        i, j = rng.choice(n_total, 2, replace=False) 
        edges.append((lokasi[i].kode, lokasi[j].kode, int(rng.integers(5,100)), 
        int(rng.integers(1,5)))) 
    return lokasi, edges

def main(): 
    bst_lokasi = BSTLokasi() 
    graph = GraphRute() 
    antrian_bantuan = PriorityQueueBantuan() 
    log_kirim = Stack() 
    bantuan_counter = 0 
    
    lokasi_list, edges = generate_peta_bencana(35, 3, seed=47) 
    for lok in lokasi_list: 
        bst_lokasi.insert(lok) 
        graph.tambah_node(lok.kode) 
    for u, v, j, k in edges: 
        graph.tambah_rute(u, v, j, k) 
    
    print('Disaster Response Logistics System  Ketik BANTUAN untuk daftar perintah') 
    # TODO: implementasikan loop CLI 
    # Perintah: KIRIM <depot> <lokasi> <jenis> <jumlah> 
    # PROSES_BANTUAN, RUTE_OPTIMAL <depot> <tujuan> 
    # UPDATE_LEVEL <kode> <level>, TIDAK_TERJANGKAU <depot> 
    # LOG_PENGIRIMAN, LAPORAN_BENCANA, KELUAR 

if __name__ == '__main__': 
    main()