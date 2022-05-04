print("RDP")
print("S->aSb/e\n B->b/a\n")
print("Input string:")
global s
s=list(input())
global i
i=0

"""
def match(a):
    global s
    global i
    if(i>=len(s)):
        return False
    elif(s[i]==a):
        i+=1
        return True
    else:
        return False
"""
 
def B():
    global s
    global i
    if(s[i]=='a'):
        i+=1
        B()
    elif(s[i]=='b'):
            i+=1
            if(s[i]!='$'):
                B()
    else:
        print("String is invalid")
        
def S():
    global s
    global i
    if(s[i]=='a'):
        i+=1
        B()
        if(i>0):
            if(s[i]=='$'):
                print("accept")
            else:
                print("invalid")
                quit()
    else:
        print("String is invalid")
        quit()

S()


                


        
        
