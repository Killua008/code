import re
j=1
y=[]
f=[]

op=['+','-','*','/']
x=input("Enter Expression: ")
m=re.split("([+-/*])",x)

def comp(m,j):
    
    for word in m:
        
        if word in op:
            y.append(''.join(m[0:3]))
            print(y)
            print(m)
            m.pop(0)
            print(m)
            m.pop(0)
            print(m)
            m[0]='t'+str(j)
            print(m)
            j+=1
            
    return m,j

while len(m)>1:
    m,j=comp(m,j)
    #print('c')
k=len(y)

y.reverse()
print(y)
for i in range(0,len(y)):
    print('t' + str(k) + '=' + y[i])
    k-=1

"""
Output-->

Enter Expression: A+B+C+D
['A+B']
['A', '+', 'B', '+', 'C', '+', 'D']
['+', 'B', '+', 'C', '+', 'D']
['B', '+', 'C', '+', 'D']
['t1', '+', 'C', '+', 'D']
['A+B', 't1+C']
['t1', '+', 'C', '+', 'D']
['+', 'C', '+', 'D']
['C', '+', 'D']
['t2', '+', 'D']
['A+B', 't1+C', 't2+D']
['t2', '+', 'D']
['+', 'D']
['D']
['t3']
['t2+D', 't1+C', 'A+B']
t3=t2+D
t2=t1+C
t1=A+B
"""

