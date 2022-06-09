a=0
all=int(input(" "))
for j in range(all):
    globals()["number"+str(j)]=[]
    for i in range(4):
        number=int(input(""))
        globals()["number"+str(j)].append(number)

    if globals()["number"+str(j)][j+1]/globals()["number"+str(j)][j]== globals()["number"+str(j)][i]/globals()["number"+str(j)][i-1] :
        a=round((globals()["number"+str(j)][j+1]/globals()["number"+str(j)][j])*globals()["number"+str(j)][i],0)
        globals()["number"+str(j)].append(a)
        for k in globals()["number"+str(j)]:
            print(k,end=" ")
        print("此為等比數列")
    else:
        a=round((globals()["number"+str(j)][j+1]-globals()["number"+str(j)][j])+globals()["number"+str(j)][i],0)
        globals()["number"+str(j)].append(a)
        for k in globals()["number"+str(j)]:
            print("%2d"%(k),end=" ")
        print("此為等差數列")

  