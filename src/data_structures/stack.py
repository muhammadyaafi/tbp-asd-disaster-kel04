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