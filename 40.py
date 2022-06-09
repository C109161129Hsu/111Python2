
big=[]
all=[]
little=[]
use_in=int(input(""))
for i in range(1,use_in,2):
    big.append(i)
    all.append(i)
all.append(use_in)
    

for i in range(use_in-2,-1,-2):
    little.append(i)
    all.append(i)

for k in big:
        print("        "+str(k))
for k in all:
        print(str(k),end=" ")
print()
for k in little:
        print("        "+str(k))

