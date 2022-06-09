sA=input("sA:")
sB=input("sB:").split(" ")
a=0
for i in range(len(sB)):
    if sA==sB[i]:
        a+=1
if a>0:
        print("子字串判斷為:Yes")
else:
        print("子字串判斷為:No")
