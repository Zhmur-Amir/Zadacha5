import math

def distance(dot_1, dot_2, dot_3):
    p=(dot_1-dot_3[0])**2
    q=(dot_2-dot_3[1])**2
    res=math.sqrt(q+p)
    return res
    
    
def triagy(dot):
    x1=dot[0][0]
    x2=dot[1][0]
    x3=dot[2][0]
    y1=dot[0][1]
    y2=dot[1][1]
    y3=dot[2][1]    
    p=2*(x1-x3)*(y2-y1)+2*(y3-y1)*(x2-x1)
    q=(x1-x3)*(x2**2-x1**2+y2**2-y1**2)+(x2-x1)*(x3**2-x1**2+y3**2-y1**2)
    res=q/p
    return res

def triagx(dot):
    x1=dot[0][0]
    x2=dot[1][0]
    x3=dot[2][0]
    y1=dot[0][1]
    y2=dot[1][1]
    y3=dot[2][1]    
    p=2*(y1-y3)*(x2-x1)+2*(x3-x1)*(y2-y1)
    q=(y1-y3)*(x2**2-x1**2+y2**2-y1**2)+(y2-y1)*(x3**2-x1**2+y3**2-y1**2)
    res=q/p
    return res    


def GreatGeometinator3000(dot, num):
    if num==1:
        return [dot[0][0],dot[0][1], 0]
    if num==2:
        r=distance(dot[0][0], dot[0][1], dot[1])
        return [(dot[0][0]+dot[1][0])*1/2, (dot[0][1]+dot[1][1])*1/2, r*1/2]      
    if num==3:
        x=triagx(dot)
        y=triagy(dot)
        R=distance(x, y, dot[0])
        return [x, y, R]

    dot_b=[dot[0],dot[1],dot[2]]
    x=triagx(dot_b)
    y=triagy(dot_b)
    R=distance(x, y, dot_b[0])    
    for k in range(3, num):
        i=dot[k]
        d=distance(x, y, i)
        if d==R:
            dot_b.append(i)
        if d>R:
            
            dot_g=[]
            dot_t=[]
            for j in range(len(dot_b)):
                dist=distance(i[0],i[1],dot_b[j])
                dot_t.append(dist)
            i_x=dot_t.index(max(dot_t))
            for p in range(len(dot_b)):
                dist=distance(i[0],i[1],dot_b[p])+distance(dot[i_x][0],dot[i_x][1],dot_b[p])
                dot_g.append(dist)
            i_z=dot_g.index(max(dot_g))
            dot_b.clear()
            dot_b.append(dot[i_x])
            dot_b.append(i)
            dot_b.append(dot[i_z])
            x=triagx(dot_b)
            y=triagy(dot_b)
            R=distance(x, y, dot_b[0])
            for h in range(len(dot)):
                if h!=i_x and h!=i_z and h!=k:
                    temp=dot[h]
                    if distance(x, y, temp)==R:
                        dot_b.append(temp)
                    
    res=[]
    res.append(x)
    res.append(y)
    res.append(R)
    return res


def autotest():
    print("Starting autotest...")
    s=True
    dot1=[[1,4]]
    dot2=[[0,0],[1,0]]
    dot3=[[0,0],[1,0],[0,1]]
    dot4=[[0,1],[1,0],[2,1],[1,2],[3,1]]
    res1=GreatGeometinator3000(dot1, 1)
    res2=GreatGeometinator3000(dot2, 2)
    res3=GreatGeometinator3000(dot3, 3)
    res4=GreatGeometinator3000(dot4, 4)
    if res1[0]!=1 and res1[1]!=4 and res2[0]!=0.5 and res2[1]!=0 and res3[0]!=0.5 and res3[1]!=0.5 and res4[0]!=1.5 and res4[1]!=1.5  :
        s=False
    if s==True:
        print("Autotest passed!  Respect+")
    else:
        print("Autotest failed!  Wasted...")




num=int(input("Enter amount of dots: "))
if num==0:
    print("Error! Wrong number...")
    exit(-1)
dot=[]
for i in range(num):
    print("Write down", i+1, "dot...")
    a=float(input("First coordinate: "))
    b=float(input("Second coordinate: "))
    dot.append([a,b])
res=[]
res=GreatGeometinator3000(dot, num)
print("Coordinates of center: (",res[0],",",res[1], ") R=", res[2])
autotest()



