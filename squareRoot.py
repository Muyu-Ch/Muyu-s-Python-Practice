def squareRoot (y):
    g=y/2
    count=0
    while(g*g/y-1>0.000005 or g*g/y-1<-0.000005):
        f=y/g
        g=(g+f)/2
        count+=1
    return [g,count]

def squareRoot1(y,g):
    if(g*g/y-1<0.000005 and g*g/y-1>-0.000005):
        return g
    else:
        return squareRoot1(y,(g+y/g)/2)
def squareRoot2(y):
    return squareRoot1(y,y/2)

y=float(input("give me a number:"))
x=squareRoot(y)
print("the Square root is:",x[0],"  counts:",x[1])
print("def2:",squareRoot2(y))

