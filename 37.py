all_n=[]
n=int(input("整數n:"))
all_n=[]
all_n.append(n)
print(n)
while n!=1:
    if n %2 ==0:
        n=n/2
        all_n.append(n)

    else:
        n=3*n+1
        all_n.append(n)

for k in all_n:
     print("%2d"%(k),end=" ")