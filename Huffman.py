#Python 3.7.15
from Node import Node

#Made by Settawat Boriruklert
#
#Class Huffman is the Huffman Encoder / Decoder
    #HuffmanTree is build the HuffmanTree by 1st argv is input the objectlist but node must sorted and  before use it example 
    #dna = DNACompute("s1.fasta")
    #nodeA = Node("A",dna.dna_prob[0][0])
    #nodeT = Node("T",dna.dna_prob[0][1])
    #nodeC = Node("C",dna.dna_prob[0][2])
    #nodeG = Node("G",dna.dna_prob[0][3])
    #node = sorted([nodeG,nodeC,nodeT,nodeA],key=attrgetter("freq"))
    #n = Node.HuffmanTree(node)
    #by the 2nd argv is how much diffrent to allow to NodeConnect by default is less than (0.074 or 7.4%)
    
    #HuffmanCode and HaveThis
    #HaveThis is find str in list if haveit "return True" but haven't it "return False"
    #HuffmanCode is find Code from HuffmanTree by input the root's HuffmanTree in 1st argv and that alphabet you want to know from HuffmanTree in 2nd argv but 3rd argv must not input anything in that argv
    #Decoding is Decode from binary's HuffmanCode into text 
    #Encoding is Encode from Text into HuffmanCode but must have HuffmanTable First by in array 2D input
    
#Class Testing Tools 
    #CR --> Compression Ratio input by 1st is encoded string , 2nd original string return in float
    

class Huffman:
    def HuffmanTree(node,diff = 0.074):
        node0 = []
        node0.append(Node.NodeConnect(node[0],node[1]))
        for i in range(2,len(node)):
            node0.append(node[i])

        i = 0
        while(i < len(node0)-1):
            if abs(node0[i].freq - node0[i+1].freq) < diff:
                nn = Node.NodeConnect(node0[i],node0[i+1])
                node0.remove(node0[i+1])
                node0[i] = nn
            else : 
                i = i + 1

        if node0[0].freq + node0[1].freq >= 0.97:
                nn = Node.NodeConnect(node0[0],node0[1])
                node0.remove(node0[1])
                node0[0] = nn
        return node0[0]
    
    def HaveThis(st,find):
        for s in st:
            if find == s:
                return True
        return False

    global str_
    str_ = [] 
    def HuffmanCode(node,find,i = 0):
        if str_ != None and i == 0:
            str_.clear()
        st_data = node.data.split( )
        st_data_left = node.left.data.split( )
        st_data_right = node.right.data.split( )

        if Huffman.HaveThis(st_data_left,find):
            str_.append("1")
            if len(st_data_left) != 1:
                Huffman.HuffmanCode(node.left,find,1)

        elif Huffman.HaveThis(st_data_right,find):
            str_.append("0")
            if len(st_data_right) != 1:
                Huffman.HuffmanCode(node.right,find,1)

        str_ans = "".join(str_)
        return str_ans
    
    def Decoding(code,encoding):    
        str_d = []
        alphabet = []
        i = 1
        alphabet.append(" > gi|12345678| DNA Sequence \n")
        for s in encoding:
            str_d.append(s)
            #print("str : " + "".join(str_))
            for c in code:
                #print("code : " + str(c) + "\tstr : " + str("".join(str_)) )
                if str("".join(str_d)) == str(c[1]):
                    #print("I'm In")
                    alphabet.append(str(c[0]))
                    str_d.clear()
                    i = i + 1
                    break
            if i == 70 :
                alphabet.append("\n")
                i = 1
            
        return "".join(alphabet)        

    def Encoding(code,dna):
        encoding = []
        for s in dna:
            for c in code:
                if s == c[0]:
                    encoding.append(c[1])
        
        encoding = "".join(encoding)
        return encoding
    

