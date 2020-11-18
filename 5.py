
def union(seg, t_1, t_2):
    a=min(seg[t_1][0],seg[t_2][0])
    b=max(seg[t_1][1],seg[t_2][1])
    seg[t_1]=[a,b]
    return seg


def comparation(seg, t_1, t_2):
    if (seg[t_1][0]<=seg[t_2][0]<=seg[t_1][1]) or (seg[t_1][0]<=seg[t_2][1]<=seg[t_1][1]):
        return True
    else:
        return False
                             
def sort(seg):
    seg=sorted(seg, key=lambda x: x[0], reverse=False)
    seg=sorted(seg, key=lambda x: x[1], reverse=False)
    return seg


def Ismeritel200(seg, num):
    for i in range(num):
        for j in range(num):
            if (comparation(seg,i,j)==True):
                union(seg, i,j)
    return seg


def longest(seg, num):
    seg_len=[]
    for i in range(num):
        seg_len.append(seg[i][1]-seg[i][0])
    x=max(seg_len)
    i=[]
    i_x=indekses(seg_len.copy(), x)
    return i_x

def indekses(seg, elem):
    result=[]
    for i in range(len(seg)):
        if (seg[i]==elem):
            result.append(i)
    return result


def autotest():
    print("Starting autotest...")
    s=True
    seg=[[3,4], [2,3], [1,3], [1,2]]
    seg_1=union(seg.copy(), 1,2)
    t_1=comparation(seg, 2,3)
    seg_2=sort(seg.copy())
    seg_3=Ismeritel200(seg_2.copy(),4)
    t_2=longest(seg_3,4)
    if seg_1!=[[3, 4], [1, 3], [1, 3], [1, 2]] or t_1!=True or seg_2!=[[1,2], [1,3], [2,3], [3,4]] or seg_3!=[[1, 4], [1, 4], [2, 4], [1, 4]] or t_2!=[0, 1, 3]:
        s=False
    if s==True:
        print("Autotest passed!  Respect+")
    else:
        print("Autotest failed!  Wasted...")



num=int(input("Enter amount of segments: "))
if num==0:
    print("Error! Wrong number...")
    exit(-2)
seg=[]
for i in range(num):
    print("Write down", i+1, "segment...")
    a=int(input("Right end: "))
    b=int(input("Left end: "))
    if(a<b):
        seg.append([a,b])
    else:
        print("This is not segment!")
        exit(-1)
        
seg_2=sort(seg)
seg_1=Ismeritel200(seg_2.copy(), num)
m=[]
m=longest(seg_1, num)
for j in m:
    print("Result: ", seg_1[j], "Length: ", seg_1[j][1]-seg_1[j][0])
autotest()
