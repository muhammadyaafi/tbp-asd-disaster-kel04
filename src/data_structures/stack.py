from data_structures.linked_list import LLNode
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