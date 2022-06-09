ad=0
d=0
a=int(input(""))
b=int(input(""))
c=int(input(""))
if b**2-4*a*c<0:
    print("無解")
else:
    ad=(-b+(b**2-4*a*c)**(1/2))/2*a
    a=(-b-(b**2-4*a*c)**(1/2))/2*a
    print("%2d"%(ad))
    print("%2d"%(a))