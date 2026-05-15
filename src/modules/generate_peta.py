import numpy as np
from modules.disaster_system import Lokasi

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