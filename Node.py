#python3.7.15

#Made by Settawat Boriruklert

# This is the basic tree for Huffman coding
# root = Node(5) mean root has data that is 5 and have empty left and empty right
# NodeConnect is combind nodeLeft and nodeRight and create new data and freq by combind nodeLeft and nodeRight together
#

class Node:
    
    def __init__(self,data,freq):
        self.data = data
        self.freq = freq
        self.parent = None
        self.left = None
        self.right = None
        self.bf = 0
        
    def NodeConnect(nodeLeft,nodeRight):
        newNode = Node(str(str(nodeLeft.data)+" "+str(nodeRight.data)+" "), (nodeLeft.freq + nodeRight.freq))
        newNode.left = nodeLeft
        nodeLeft.parent = newNode
        newNode.right = nodeRight
        nodeRight.parent = newNode
        return newNode

    
        
        
