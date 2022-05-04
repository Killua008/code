import os


mnemonics={'STOP':('00','IS',0),'ADD':('01','IS',2),'SUB':('02','IS',2),'MUL':('03','IS',2),'MOVER':('04','IS',2),'MOVEM':('05','IS',2),'COMP':('06','IS',2),'BC':('07','IS',2),'DIV':('08','IS',2),'READ':('09','IS',1),'PRINT':('10','IS',1),'LTORG':('05','AD',0),'ORIGIN':('03','AD',1),'START':('01','AD',1),'EQU':('04','AD',2),'DS':('01','DL',1),'DC':('02','DL',1),'END':('AD',0)}
LC=0

file=open("input.txt")

symtab={}

def symbol():
    global symtab
    print("Symbol Table:")
    print(symtab)
def OTHERS(mnemonic,k):
    global words
    global mnemonics 
    global symtab
    global LC,symindex
    z=mnemonics[mnemonic]
    
    i=0
    y=z[-1]
    for i in range(1,y+1):
        if(words[k+i] not in symtab.keys()):
            symtab[words[k+i]]=("**",symindex)
            
            symindex+=1
        else:
            w=symtab[words[k+i]]
            
    LC+=1


def detect_mn(k):
    OTHERS(words[k],k)
    symbol()


symindex=0
for line in file:
   
    words=line.split()
    
    print("LC=",LC)
    print(line)
    print(words)
    k=0
        
    if words[0] in mnemonics.keys():
        print("Mnemonic:",words[0])
        val=mnemonics[words[0]]
        k=0
        detect_mn(k)
    else:
        print("Label:",words[0],"Mnemonic:",words[1])
        if words[k] not in symtab.keys():
            symtab[words[k]]=(LC,symindex)
            symindex+=1
            symbol()
        else:
            x=symtab[words[k]]
            if x[0]=="**":
                print("yes")
                symtab[words[k]]=(LC,x[1])
            symbol()
        k=1
        detect_mn(k)


"""

input.txt-->

   START 100
A  DC 10
   MOVER AREG, B
   MOVEM BREG, ='1'
   ADD AREG, ='2'
   SUB BREG, ='1'
B  DC 20 
   ORIGIN 300
   LTORG 
   MOVER AREG, NUM
   MOVER CREG, LOOP
   ADD BREG, ='1'
NUM DS 5 
LOOP	DC 10 
END 
"""
