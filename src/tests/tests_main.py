import numpy as np
from typing import Optional, List, Dict, Tuple
from dataclasses import dataclass 

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

class BSTNodeLok:
    def __init__(self, lokasi: Lokasi):
        self.lokasi = lokasi
        self.left: Optional['BSTNodeLok'] = None
        self.right: Optional['BSTNodeLok'] = None

class BSTLokasi:
    def __init__(self):
        self.root: Optional[BSTNodeLok] = None

    def insert(self, lokasi: Lokasi) -> None:
        """
        Big-O: O(log n) rata-rata, O(n) worst-case.
        Menyisipkan lokasi baru berdasarkan kode_lokasi (string comparison).ca
        """
        if self.root is None:
            self.root = BSTNodeLok(lokasi)
        else:
            self._insert_recursive(self.root, lokasi)

    def _insert_recursive(self, node: BSTNodeLok, lokasi: Lokasi) -> None:
        if lokasi.kode < node.lokasi.kode:
            if node.left is None:
                node.left = BSTNodeLok(lokasi)
            else:
                self._insert_recursive(node.left, lokasi)
        elif lokasi.kode > node.lokasi.kode:
            if node.right is None:
                node.right = BSTNodeLok(lokasi)
            else:
                self._insert_recursive(node.right, lokasi)

    def search(self, kode: str) -> Optional[Lokasi]:
        """
        Big-O: O(log n) rata-rata, O(n) worst-case.
        Mencari data lokasi berdasarkan kode unik.
        """
        curr = self.root
        while curr:
            if kode == curr.lokasi.kode:
                return curr.lokasi
            curr = curr.left if kode < curr.lokasi.kode else curr.right
        return None

    def update_level(self, kode: str, level_baru: int) -> bool:
        """
        Big-O: O(log n) rata-rata.
        Mencari lokasi lalu memperbarui tingkat keparahan bencana.
        """
        lokasi = self.search(kode)
        if lokasi:
            lokasi.level = level_baru
            return True
        return False

    def inorder(self) -> list[Lokasi]:
        """
        Big-O: O(n).
        Menghasilkan daftar lokasi yang terurut secara alfabetis berdasarkan kode.
        """
        hasil = []
        self._inorder_recursive(self.root, hasil)
        return hasil

    def _inorder_recursive(self, node: Optional[BSTNodeLok], hasil: List[Lokasi]) -> None:
        if node:
            self._inorder_recursive(node.left, hasil)
            hasil.append(node.lokasi)
            self._inorder_recursive(node.right, hasil)

class LLNode: 
    def __init__(self, data=None): 
        self.data = data 
        self.next = None 

class Stack: 
    def __init__(self): 
        # Inisialisasi stack kosong sesuai prinsip Linked List di buku
        self.top = None # 'top' menunjuk ke node teratas (sama dengan '_head' di buku) [2]
        self._size = 0 
    
    def is_empty(self) -> bool:
        """Mengembalikan True jika stack logistik kosong."""
        return self._size == 0

    def push(self, data): 
        """
        Big-O: O(1).
        Menambahkan riwayat pengiriman baru ke posisi teratas stack. [2]
        """
        # Membuat node baru menggunakan LLNode yang sudah didefinisikan temanmu
        new_node = LLNode(data)
        # Menghubungkan node baru ke node yang sebelumnya ada di posisi top
        new_node.next = self.top
        # Memperbarui posisi top ke node yang baru saja dimasukkan
        self.top = new_node
        self._size += 1 
    
    def pop(self): 
        """
        Big-O: O(1).
        Mengambil dan menghapus log terakhir. Digunakan untuk fitur ROLLBACK. [4]
        """
        if self.is_empty():
            return None
        
        # Menyimpan data yang akan diambil
        answer = self.top.data
        # Menggeser penunjuk top ke node di bawahnya (menghapus referensi node teratas) [4]
        self.top = self.top.next
        self._size -= 1
        return answer 
    
    def peek(self): 
        """
        Big-O: O(1).
        Melihat data pengiriman teratas tanpa menghapusnya.
        """
        return self.top.data if self.top else None 
    
    def to_list(self): 
        """
        Big-O: O(n).
        Menelusuri seluruh stack dan mengembalikannya dalam bentuk list.
        Sangat berguna untuk fitur LOG_PENGIRIMAN (menampilkan riwayat). [5]
        """
        result = []
        # Melakukan 'link hopping' atau traversal dari top ke bottom [5]
        curr = self.top
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result

    def __len__(self):
        """Mengembalikan jumlah elemen dalam stack."""
        return self._size

class PriorityQueueBantuan: 
    """Lokasi KRITIS (level=1) selalu dilayani lebih dulu.""" 
    def __init__(self): 
        self.head = None 
        self._size = 0 
    
    def enqueue(self, bantuan): 
        """Big-O: O(n) insertion terurut prioritas.""" 
        new_node = LLNode(bantuan)

        if self.head is None or self.head.data.prioritas > bantuan.prioritas:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data.prioritas <= bantuan.prioritas:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self._size += 1
    
    def dequeue(self): 
        """Big-O: O(1).""" 
        if self.head is None:
            return None
        bantuan = self.head.data
        self.head = self.head.next
        self._size -= 1
        return bantuan
    
    def __len__(self): 
        return self._size 

    def is_empty(self):
        return self._size == 0
    
class EdgeNode: 
    def __init__(self, dest, jarak, kapasitas): 
        self.dest = dest 
        self.jarak = jarak 
        self.kapasitas = kapasitas 
        self.next = None

class GraphRute: 
    def __init__(self): 
        self._adj = {} 
    
    def tambah_node(self, kode): 
        """Big-O: O(1).""" 
        # pass  # TODO: implementasikan 
        if kode not in self._adj:
            self._adj[kode] = set()
    
    def tambah_rute(self, u, v, jarak, kapasitas): 
        """Big-O: O(1). Graf tidak berarah.""" 
        # pass  # TODO: implementasikan 
        node_uv = EdgeNode(v, jarak, kapasitas)
        node_uv.next = self._adj[u]
        self._adj[u] = node_uv

        node_vu = EdgeNode(u, jarak, kapasitas)
        node_vu.next = self._adj[v]
        self._adj[v] = node_vu
        
    def tetangga(self, u): 
        """Big-O: O(deg).""" 
        # pass  # TODO: implementasikan 
        hasil = []
        curr = self.adj[u]
        while curr:
            hasil.append(
                (curr.dest, curr.jarak, curr.kapasitas)
            )
            curr = curr.next
        
        return hasil
    
    def bfs_akses(self, depot): 
        """BFS dari depot. Big-O: O(V+E).""" 
        # pass  # TODO: gunakan Queue Linked List sendiri
        visited = set()
        q = Queue()
        q.enqueue(depot)
        visited.add(depot)
        while not q.is_empty():
            current = q.dequeue()
            edge = self.adj[current]
            while edge:
                tetangga = edge.dest
                if tetangga not in visited:
                    visited.add(tetangga)
                    q.enqueue(tetangga)
                edge = edge.next
        return visited

class Empty(Exception):
    pass

class Queue:
    class _Node:
        """
        Node ringan untuk Linked List (Goodrich §7.1, hal. 256).
        Menggunakan __slots__ untuk menghemat memori.
        """
        __slots__ = '_element', '_next'
        def __init__(self, element, next_node):
            self._element = element
            self._next = next_node

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        newest = self._Node(e, None)        # node baru, next=None (akan jadi tail)
        if self.is_empty():
            self._head = newest             # queue sebelumnya kosong, head = node baru
        else:
            self._tail._next = newest       # hubungkan tail lama ke node baru
        self._tail = newest                 # update tail ke node baru
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next   # majukan head
        self._size -= 1
        if self.is_empty():
            self._tail = None   # queue kosong, tail tidak valid lagi
        return answer

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

def dijkstra_logistik(graph, depot): 
    """Shortest path dari depot. Big-O: O(V^2+E).""" 
    INF = float('inf') 
    dist = {v: INF for v in graph._adj} # Jarak awal semua node = tak hingga
    parent = {v: None for v in graph._adj} # Parent untuk rekonstruksi jalur
    dist[depot] = 0 # Jarak depot ke dirinya sendiri = 0
    visited = set() # Menyimpan node yang sudah diproses
    # TODO: implementasikan

    while len(visited) < len(graph._adj):

        # Cari node belum dikunjungi
        # dengan jarak minimum
        current = None
        current_dist = INF

        for node in graph._adj:

            if node not in visited and dist[node] < current_dist:
                current = node
                current_dist = dist[node]

        # Jika tidak ada node terjangkau lagi
        if current is None:
            break

        # Tandai sudah dikunjungi
        visited.add(current)

        # Traversal tetangga current
        edge = graph._adj[current]

        while edge:

            neighbor = edge.dest
            weight = edge.jarak

            # Relaxation
            new_dist = dist[current] + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = current

            edge = edge.next

    return dist, parent 

def reconstruct_path(parent, tujuan):

    path = []

    while tujuan:
        path.append(tujuan)
        tujuan = parent[tujuan]

    path.reverse()

    return path

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
    while True:

        cmd = input("\n>> ").strip()

        if not cmd:
            continue

        parts = cmd.split()

        perintah = parts[0].upper()

        # ==================================================
        # KIRIM
        # ==================================================

        if perintah == "KIRIM":

            if len(parts) != 5:
                print("Format salah!")
                continue

            depot = parts[1]
            tujuan = parts[2]
            jenis = parts[3].upper()
            jumlah = int(parts[4])

            lokasi = bst_lokasi.search(tujuan)

            if lokasi is None:
                print("Lokasi tidak ditemukan!")
                continue

            bantuan_counter += 1

            bantuan = Bantuan(
                bantuan_id=bantuan_counter,
                jenis=jenis,
                jumlah=jumlah,
                asal=depot,
                tujuan=tujuan,
                prioritas=lokasi.level
            )

            antrian_bantuan.enqueue(bantuan)

            print(f"Bantuan masuk antrian prioritas.")

        # ==================================================
        # PROSES_BANTUAN
        # ==================================================

        elif perintah == "PROSES_BANTUAN":

            bantuan = antrian_bantuan.dequeue()

            if bantuan is None:
                print("Antrian kosong!")
                continue

            print("\nBantuan diproses:")
            print(
                bantuan.bantuan_id,
                bantuan.jenis,
                bantuan.tujuan
            )

            # simpan ke log stack
            log_kirim.push(bantuan)

        # ==================================================
        # RUTE_OPTIMAL
        # ==================================================

        elif perintah == "RUTE_OPTIMAL":

            if len(parts) != 3:
                print("Format salah!")
                continue

            depot = parts[1]
            tujuan = parts[2]

            dist, parent = dijkstra_logistik(graph, depot)

            if dist[tujuan] == float('inf'):
                print("Lokasi tidak terjangkau!")
                continue

            path = reconstruct_path(parent, tujuan)

            print("\nRute Optimal:")
            print(" -> ".join(path))

            print(f"Total jarak: {dist[tujuan]} km")

        # ==================================================
        # UPDATE_LEVEL
        # ==================================================

        elif perintah == "UPDATE_LEVEL":

            if len(parts) != 3:
                print("Format salah!")
                continue

            kode = parts[1]
            level = int(parts[2])

            bst_lokasi.update_level(kode, level)

            print("Level berhasil diperbarui.")

        # ==================================================
        # TIDAK_TERJANGKAU
        # ==================================================

        elif perintah == "TIDAK_TERJANGKAU":

            if len(parts) != 2:
                print("Format salah!")
                continue

            depot = parts[1]

            visited = graph.bfs_akses(depot)

            semua = set(graph.adj.keys())

            tidak_terjangkau = semua - visited

            print("\nLokasi tidak terjangkau:")

            if not tidak_terjangkau:
                print("Tidak ada")
            else:
                for x in sorted(tidak_terjangkau):
                    print(x)

        # ==================================================
        # LOG_PENGIRIMAN
        # ==================================================

        elif perintah == "LOG_PENGIRIMAN":

            logs = log_kirim.to_list()

            if not logs:
                print("Log kosong!")
                continue

            print("\nRiwayat Pengiriman:")

            for item in logs:

                print(
                    f"ID:{item.bantuan_id} | "
                    f"{item.jenis} | "
                    f"{item.tujuan}"
                )

        # ==================================================
        # LAPORAN_BENCANA
        # ==================================================

        elif perintah == "LAPORAN_BENCANA":

            data = bst_lokasi.inorder()

            print("\nDaftar Lokasi:")

            for lok in data:

                print(
                    f"{lok.kode} | "
                    f"{lok.nama} | "
                    f"Level:{lok.level} | "
                    f"Pop:{lok.populasi}"
                )

        # ==================================================
        # KELUAR
        # ==================================================

        elif perintah == "KELUAR":

            print("Program selesai.")
            break

        # ==================================================
        # BANTUAN
        # ==================================================

        elif perintah == "BANTUAN":
            print("\nPerintah:")
            print("KIRIM <depot> <lokasi> <jenis> <jumlah>")
            print("PROSES_BANTUAN")
            print("RUTE_OPTIMAL <depot> <tujuan>")
            print("UPDATE_LEVEL <kode> <level>")
            print("TIDAK_TERJANGKAU <depot>")
            print("LOG_PENGIRIMAN")
            print("LAPORAN_BENCANA")
            print("KELUAR")

        # ==================================================
        # COMMAND TIDAK DIKENAL
        # ==================================================

        else:
            print("Perintah tidak dikenali!")

if __name__ == '__main__': 
    main()