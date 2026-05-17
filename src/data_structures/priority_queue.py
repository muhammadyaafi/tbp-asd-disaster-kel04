from data_structures.linked_list import LLNode
from modules.disaster_system import LEVEL_BENCANA

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
    
    def tampilkan_antrian(self):
        if self.head is None:
            print("Antrian kosong!")
            return
        level_nama = {v: k for k, v in LEVEL_BENCANA.items()}
        curr = self.head
        nomor = 1

        while curr:
            bantuan = curr.data
            print(
                f"Antrian {nomor}: "
                f"{bantuan.jumlah} {bantuan.jenis} "
                f"dari {bantuan.asal} ke {bantuan.tujuan}. "
                f"Level {level_nama[bantuan.prioritas]}"
            )
            curr = curr.next
            nomor += 1