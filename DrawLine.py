def show_points(point,x,y):
    width=3
    for i in range(x):
        for j in range(y):
            if i==0:
                print(f'{j:>{width}}',end="")
            elif j==0:
                print(f'{i:>{width}}',end="")
            elif [i,j] in point:
                print(f'{"*":>{width}}',end='')
            else:
                print(f'{" ":>{width}}',end='')
        print("")

def show(points):
    x=0
    y=0
    for point in points:
        x=max(x,point[0])
        y=max(y,point[1])
    show_points(points,x+1,y+1)

def line(point1,point2):
    points=[]
    if point1[0]==point2[0]:
        for i in range(point1[1],point2[1]+1):
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

p1=[int(input("X of the first point: ")),int(input("Y of the first point: "))]
p2=[int(input("X of the second point: ")),int(input("Y of the second point: "))]
ps=line(p1,p2)
show(ps)





