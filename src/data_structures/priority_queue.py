from data_structures.linked_list import LLNode

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
