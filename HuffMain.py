from dnaCompute import DNACompute
from Node import Node
from Huffman import Huffman as Huff
from operator import attrgetter
import sys

#Main Programe
#How to use
#Encoding Huffman : -e <input_file>
#Decoding Huffman : -d <Encode File> <Huffman Table File>

#Example
#python3 a2-590612140.py -d HuffEncode_s1_fasta.dat HuffTable_s1_fasta.tab
#python3 a2-590612140.py -e s1.fasta

#Made by Settawat Boriruklert

def CR(encode,st):
    uncompress = len(''.join('{0:08b}'.format(ord(x), 'b') for x in "".join(st)))
    compress = len("".join(encode))
    cr = uncompress/compress

    return cr

def avgR(beta_p):
    avgR = 0.00000
    for b in beta_p:
        avgR = avgR + len(b[0])*b[1]
    return avgR

def Counting(text):
    data = [0,0,0,0,0]
    for j in text:
        if j == "A":
            data[0] = data[0] + 1
            data[4] = data[4] + 1
        if j == "T":
            data[1] = data[1] + 1
            data[4] = data[4] + 1
        if j == "C":
            data[2] = data[2] + 1
            data[4] = data[4] + 1
        if j == "G":
            data[3] = data[3] + 1
            data[4] = data[4] + 1
    return data


if __name__ == '__main__':
    
    if len(sys.argv) < 2 :
        print("Please input option\nEncoding Huffman : -e <input_file>  \nDecoding Huffman : -d <Encode File> <Huffman Table File>")
    else : 

        if str(sys.argv[1]) == '-e':

            if len(sys.argv) < 3:
                print("Encoding Huffman : -e <input_file>")
            else :
                #sys.argv 1st argv is inputfile 
                file = str(sys.argv[2]) 
                dna = DNACompute(file)

                #Create Node
                nodeA = Node("A",dna.dna_prob[0][0])
                nodeT = Node("T",dna.dna_prob[0][1])
                nodeC = Node("C",dna.dna_prob[0][2])
                nodeG = Node("G",dna.dna_prob[0][3])

                #Create Huffman Tree
                node = sorted([nodeA,nodeT,nodeC,nodeG],key = attrgetter("freq"))
                node = Huff.HuffmanTree(node)

                #Create Huffman Code
                codeA = ['A',"".join(Huff.HuffmanCode(node,"A"))]
                codeT = ['T',"".join(Huff.HuffmanCode(node,"T"))]
                codeC = ['C',"".join(Huff.HuffmanCode(node,"C"))]
                codeG = ['G',"".join(Huff.HuffmanCode(node,"G"))]

                #Prepair to print out
                code = [codeA,codeT,codeC,codeG]
                dnaTest = dna.dna[0].splitlines()
                encode = Huff.Encoding(code,"".join(dnaTest))
                beta_p = [[codeA[1],nodeA.freq],[codeT[1],nodeT.freq],[codeC[1],nodeC.freq],[codeG[1],nodeG.freq]]

                #print out 
                print("Compression Ratio : " + str(CR(encode,dnaTest)))
                print("BitRate : " + str(avgR(beta_p)))
                print("Entropy : " + str(dna.dna_ent[0]))
                print("Number of Occurences [A,T,C,G,All] : "+  str(dna.dna_data[0][0]) + ", " + str(dna.dna_data[0][1]) + ", " + str(dna.dna_data[0][2]) + ", " + str(dna.dna_data[0][3]) + "]")
                print("Probability of occurrence : " + str(dna.dna_prob[0]))

                #Write encode and table
                tableFile = open(str("HuffTable_"+file.split('.')[0] + "_" + file.split('.')[1] +".tab"),"w")
                table = ""
                for c in code:
                    table = table + str(c[0]) + "\t" + str(c[1]) + "\n"
                tableFile.write(table)

                encodeFile = open(str("HuffEncode_"+ file.split('.')[0] + "_" + file.split('.')[1] +".dat"),"wb")
                encodeFile.write(encode.encode('ascii'))

        elif str(sys.argv[1]) == '-d':
            
            if len(sys.argv) < 3:
                print("Decoding Huffman : -d <Encode File> <Huffman Table File>")
            else : 
                
                en_code = str(sys.argv[2])
                table = str(sys.argv[3])
                tab = open(table,"r")
                #print(tab.readlines())
                code = []
                for s in tab.readlines():
                    #print(s)
                    code.append(s.split('\t'))
                #print(code)
                for i in code:
                    i[1] = i[1].replace('\n','')

                encode = open(en_code,"r")
                text = Huff.Decoding(code,str(encode.readline()))
                
                file = open("HuffDecode_"+ en_code.split('_')[1] + "_" + en_code.split('_')[2].split('.')[0] + ".txt","a")
                file.write(text)
                t = Counting(text)
                print("Length of the DNA sequence : " + str(t[4]))
                print("Number of Occurences [A,T,C,G] : "+  str(t[0]) + ", " + str(t[1]) + ", " + str(t[2]) + ", " + str(t[3]) + "]")

        else :
            print("Encoding Huffman : -e <input_file>\nDecoding Huffman : -d <Encode File> <Huffman Table File>")
