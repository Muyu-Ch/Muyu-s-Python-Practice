def show(points):#绘画所有的点
    x=0
    y=0
    for point in points:
        x=max(x,point[0])
        y=max(y,point[1])
    width = 3
    for i in range(x+1):
        for j in range(y+1):  # 遍历所有坐标检测（x，y）是否在集合内
            if i == 0:
                print(f'{j:>{width}}', end="")
            elif j == 0:
                print(f'{i:>{width}}', end="")
            elif [i,j] in points:
                print(f'{"*":>{width}}', end='')
            else:
                print(f'{" ":>{width}}', end='')
        print("")

def line(point1,point2):#给定两个点，画出一条线
    points=[]
    if point1[0]==point2[0]:
        max_y=max(point1[1],point2[1])
        min_y=min(point1[1],point2[1])
        for i in range(min_y,max_y+1):
            points.append([point1[0],i])
        return points
    a=(point1[1]-point2[1])/(point1[0]-point2[0])
    min_x=min(point1[0],point2[0])
    max_x=max(point1[0],point2[0])
    for i in range(min_x,max_x+1):
        if min_x==point1[0]:
            points.append([i,int(a*(i-min_x)+point1[1])])
        else:
            points.append([i,int(a*(i-min_x)+point2[1])])
    return points

'''线表结构：ls:
    [l1:[[x11,y11],[x12,y12]]
     l2:[[x21,y21],[x22,y22]]
     l3:[[x31,y31],[x32,y32]]
     ......
     ]'''

def lines(ls):#连续画出好几条线
    points=[]
    for i in range(len(ls)):
        points+=line(ls[i][0],ls[i][1])
    return points

n=int(input("the number of lines: "))

ls=[]

for i in range(n):
    x1,y1=map(int,input(f"the first point of num{i+1} line: ").split())
    x2,y2=map(int,input(f"the second point of num{i+1} line: ").split())
    ls.append([[x1,y1],[x2,y2]])

ps=lines(ls)
show(ps)



