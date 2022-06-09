A=0
B=0
ans=input(" ")
use_in=str(input(" "))
while use_in !="0000":
    A=0
    B=0
    for i in range(len(ans)):
        if ans[i]==use_in[i]:
            A+=1
        else:
            for j in range(len(ans)):
                if ans[i]==use_in[j]:
                    B+=1
         
    print(str(A)+"A"+str(B)+"B")
    use_in=str(input(" "))
   
    