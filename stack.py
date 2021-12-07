class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):  # Memeriksa apakah stack kosong 
        return self.items == []
        
    def push(self, item):  # Menambahkan item pada posisi atas
        self.items.append(item)
        
    def pop(self):  # Menghapus item paling atas
        return self.items.pop()
        
    def peek(self): # Menampilkan jumlah elemen pada stack
        return self.items[len(self.items)-1]
        
    def size(self): # Mengembalikan nilai Stack
        return len(self.items)
        
s = Stack()
    
s.push('UBSI')
s.push('Cengkareng')
print(s.size())
print(s.peek())
    
print(s.pop())
print(s.size())
print(s.peek())