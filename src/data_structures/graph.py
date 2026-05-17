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
        if u not in self._adj:
            self.tambah_node(u)

        if v not in self._adj:
            self.tambah_node(v)

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
        curr = self._adj[u]
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
            edge = self._adj[current]
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
