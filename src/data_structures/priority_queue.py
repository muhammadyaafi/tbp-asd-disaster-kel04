<<<<<<< HEAD:src/data_structures/priority_queue.py
from data_structures.linked_list import LLNode

=======
>>>>>>> 5b276c5 (feat(queue) : implementasi priority queue):src/data_structures/queue_ll.py
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
        if self.is_full():
            return False
        self.buffer[self.rear] = produk
        self.rear = (self.rear + 1) % self.kapasitas
        self._size += 1
        return True

    def dequeue(self):
        """Big-O: O(1). Ambil produk terlama (FIFO)."""
        if self.is_empty():
            return None
        produk = self.buffer[self.front]
        self.buffer[self.front] = None  # Optional: clear reference
        self.front = (self.front + 1) % self.kapasitas
        self._size -= 1
        return produk

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
<<<<<<< HEAD:src/data_structures/priority_queue.py
        """Big-O: O(1).""" 
=======
        """Big-O: O(1)."""  
>>>>>>> 5b276c5 (feat(queue) : implementasi priority queue):src/data_structures/queue_ll.py
        if self.head is None:
            return None
        bantuan = self.head.data
        self.head = self.head.next
        self._size -= 1
        return bantuan
    
    def __len__(self): 
        return self._size 

    def is_empty(self):
<<<<<<< HEAD:src/data_structures/priority_queue.py
        return self._size == 0
=======
        return self._size == 0
>>>>>>> 5b276c5 (feat(queue) : implementasi priority queue):src/data_structures/queue_ll.py
