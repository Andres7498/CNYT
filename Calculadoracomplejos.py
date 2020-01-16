import math

def sumacom(x,y):
    q=float(x[0])+float(y[0])
    e=float(x[1])+float(y[1])
    return(q,e)
def rescom(x,y):
    q=float(x[0])-float(y[0])
    e=float(x[1])-float(y[1])
    return(q,e)
def multicom(x,y):
    q=float(x[0])*float(y[0])
    e=float(x[0])*float(y[1])+(float(x[1])*float(y[0]))
    i=(float(x[1])*float(y[1])*-1)
    q=q+i
    return(q,e)
def modcom(x,y):
    q=((float(x[0])**2)+(float(x[1])**2))**0.5
    e=((float(y[0])**2)+(float(y[1])**2))**0.5
    return(q,e)
def divcom(x,y):
    a1=float(x[0])
    a2=float(x[1])
    b1=float(y[0])
    b2=float(x[0])
    q=(((a1*a2)+(b1*b2))/(a2**2)+(b2**2))
    e=(((a2*b1)-(a1*b2))/(a2**2)+(b2**2))
    return(q,e)
def concom(x,y):
    q=float(x[0]),(float(x[1])*-1)
    e=float(y[0]),(float(y[1])*-1)
    return(q,e)
def cartcom(x):
    q=((float(x[0])**2)+(float(x[1])**2))**0.5
    ang1=math.atan(float(x[1])/float(x[0]))
    x=q*math.cos(ang1)
    y=q*math.sin(ang1)
    return(x,y)

