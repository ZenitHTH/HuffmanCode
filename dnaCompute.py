#python3.7.15
import math
import sys

# Made by Settawat Boriruklert

#This Class is the festa reader , counting and entropy computing
#dnaReader(file.festa) is input the file.festa in to class 
#
#Spliting is connecting DNA line and support multi Sequence and return into 1D Arrays--> [DNA0,DNA1,DNA2, ...]
#Counting is counting the dna in data , how many of A,T,C,G and lenght of DNA data , return in to 2D arrays 
#Probability is computing the Prob of DNA , return in [ 1st DNA [prop A,propT,prop C,prop G],2nd DNA [prop A,propT,prop C,prop G],...]
#Entropy is computing the Entropy of DNA , return in [entropy from dna1,entropy from dna2,...] 

class DNACompute: 
    
    
    def __init__(self,file):
        self.file_dna = open(str(file),"r+")
        self.dna = self.Spliting()                #Spliting     dna = [[>DNA sequence1<],[>DNA sequence2<],...]  
        self.dna_data = self.Counting()           #Counting     dna_data = [data1,data2,...]
        self.dna_prob = self.Probability()        #Probability  prop_data = [prop_data1,prop_data2,...]
        self.dna_ent = self.Entropy()             #Entropy      ent = [entropy from dna1,entropy from dna2,...] 
        
    
    def Spliting(self):
        s_split = ""
        dna = []
        #Warning if forget input the file.festa to processing
        if self.file_dna == None:
            print("Please input the file by dnaReader(file.festa)")
            return None
        else :
            for s in self.file_dna.readlines():
                if s[0] != ">":
                    s_split = s_split + str(s)
                    #print(s_split)
                else :
                    dna.append(s_split)
                    #print("DNA" + str(dna))
                    s_split = ""
            dna.append(s_split)        
            dna.remove("")
            return dna
        
    def Counting(self):
        dna_data = []
        #Auto Computing to find
        if self.dna == None:
            self.dna = self.Spliting()

        for i in self.dna:
            data = [0,0,0,0,0] # data = [A,T,C,G , len]
            for j in i:
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
            dna_data.append(data)                   
        return dna_data
            
    def Probability(self):
        prob_dna = []
        #Auto Computing to find
        if self.dna_data == None:
            self.dna_data = self.Counting()
                
        for d in self.dna_data:
            prob_dna.append ([d[0]/d[4] ,d[1]/d[4] ,d[2]/d[4] ,d[3]/d[4]]) # prop_data = [prop A,propT,prop C,prop G]
        return prob_dna
    
    def Entropy (self):
        ent = []
        #Auto Computing to find
        if self.dna_prob == None:
            self.dna_prob = self.Probability()
        
        for entropy in self.dna_prob:
            en = 0
            for i in entropy:
                en = en + (i*math.log2(i))
            ent.append(float(en*(-1)))
                
        return ent
      
            
        
