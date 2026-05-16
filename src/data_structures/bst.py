from typing import Optional, List, Dict, Tuple
class Lokasi:
    kode: str          # Kunci BST (misal: 'L01')
    nama: str
    level: int         # 1=KRITIS, 2=SEDANG, 3=RINGAN
    populasi: int
    status: int = 0    # 0=BELUM, 1=TERKIRIM

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
