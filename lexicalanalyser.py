with open("lexanly.txt","r") as f:
    data =f.readlines()
    data =list(map(lambda x:x.replace("\n"," "),data))
print(data)

keywords=['include','stdio.h','return','int','void','main']
paranthesis=['{','}','[',']','<','>']
delimiters=[' ',';',',']

for j in data:
    print(j)
    
    for i in j.split(" "):
        #print(j)
        if i in keywords:
            print("Keyword:\t",i)
        elif '#' in i:
            print("Header File:\t",i)
        elif '(' and ')' in i:
            print("Function:\t",i)
        elif i in paranthesis:
            print("Paranthesis:\t",i)
        elif i in delimiters:
            print("Delimiters:\t",i)
        else:
            print("Variable:\t",i)

"""

Input File->

# include < stdio.h >
void main()
{
int a ;
}

Output -->

['# include < stdio.h > ', 'void main() ', '{ ', 'int a ; ', '}']
# include < stdio.h > 
Header File:	 #
Keyword:	 include
Paranthesis:	 <
Keyword:	 stdio.h
Paranthesis:	 >
Variable:	 
void main() 
Keyword:	 void
Function:	 main()
Variable:	 
{ 
Paranthesis:	 {
Variable:	 
int a ; 
Keyword:	 int
Variable:	 a
Delimiters:	 ;
Variable:	 
}
Paranthesis:	 }
"""

