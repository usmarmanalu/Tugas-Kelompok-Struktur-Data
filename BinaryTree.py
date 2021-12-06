class Node:
    def __init__(data,key):
        data.left = None
        data.right = None
        data.val = key
        
        
    #Operasi pada Pohon Biner (Biner Tree Traversal) dibagi menjadi 3 bentuk     
    
    
    #PreOrder
    def trafersePreOrder(data):
        print(data.val,end='   ')               #cetak isi simpul yang dikunjungi (Simpul Akar)
        if data.left:
            data.left.trafersePreOrder()        #Kunjungi cabang kiri
        if data.right:
            data.right.trafersePreOrder()       #kunjungi cabang kanan
            
    #InOrder
    def traverseInOrder(data):
        if data.left:
            data.left.traverseInOrder()         #kunjungi cabang kiri
        print(data.val,end='   ')               #cetak isi simpul yang dikunjungi (Simpul Akar)
        if data.right:
            data.right.traverseInOrder()        #kunjungi cabang kanan
            
    #PostOrder
    def traversePostOrder(data):
        if data.left:
            data.left.traversePostOrder()       #kunjungi cabang kiri
        if data.right:
            data.right.traversePostOrder()      #kunjungi cabang kanan
        print(data.val,end='   ')               #cetak isi simpul yang dikunjungi (Simpul Akar)
            
            
root = Node("A")                                #LEVEL 1

root.left = Node("B")                           #LEVEL 2
root.right = Node("C")

root.left.left = Node("D")                      #LEVEL 3
root.right.left = Node("E")
root.right.right = Node("F")

root.left.left.right = Node("G")                #LEVEL 4
root.right.left.left = Node("H")
root.right.left.right = Node("I")


print("\nPre Order Traversal  : ",end="")
root.trafersePreOrder()
print("\n\nIn order Traversal   : ",end="")
root.traverseInOrder()
print("\n\nPost Order Traversal : ",end="")
root.traversePostOrder()