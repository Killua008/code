def readData(f):
    with open(f)as t:
        data=[]
        da=t.read().split("\n")
        for line in da:
            if len(line)!=0:
                data.append(line.split())
    return data

def create_MDT_MNT(data):
    mdt=[]
    mnt=[]
    mdtc,mntc=0,0
    flag=0
    temp=None
    for i,j in enumerate(data):
        print(i,j)
        if flag==1:
            if len(j) == 2 and temp !=1:
                j[1]=j[1].replace('&arg','#')
                #print(j)
            mdt.append([mdtc,j])
            mdtc +=1

        if temp:
            mnt.append([mntc,j[0],mdtc-1])
            mntc +=1
            temp=0

        if j[0].lower()=='marco':
            flag=temp=1

        if j[0].lower() =='mend':
            flag=0
    return mdt,mnt


if __name__ == '__main__':
    data=readData('marco.txt')
    mdt,mnt=create_MDT_MNT(data)
    print("\nMDT")
    for i in mdt:
        print(i)
    print("\nMNT")
    for i in mnt:
        print(i)


"""
Input file->

MARCO
INCR &arg1, &arg2, &arg3
A 1,&arg3
A 2,&arg2
A 3,&arg1
MEND

INCR Data1,Data2,Data3

Output-->

0 ['MARCO']
1 ['INCR', '&arg1,', '&arg2,', '&arg3']
2 ['A', '1,&arg3']
3 ['A', '2,&arg2']
4 ['A', '3,&arg1']
5 ['MEND']
6 ['INCR', 'Data1,Data2,Data3']

MDT
[0, ['INCR', '&arg1,', '&arg2,', '&arg3']]
[1, ['A', '1,#3']]
[2, ['A', '2,#2']]
[3, ['A', '3,#1']]
[4, ['MEND']]

MNT
[0, 'INCR', 0]
"""

