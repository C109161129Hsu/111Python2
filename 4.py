x=int(input("X軸座標:"))
y=int(input("Y軸座標:"))
if x>0 and y>0:
    ans="第一象限"
elif x>0 and y<0:
       ans="第四象限"
elif x<0 and y<0:
       ans="第三象限"
elif  x<0 and y>0:
    ans="第二象限"
elif x==0 and y==0:
    ans="該點位於原點"
elif x==0 and y<0:
    ans="上半平面Y軸上"
elif x==0 and y>0:
    ans="下半平面Y軸上"  
elif x<0 and y==0:
    ans="左半平面X軸上"  
elif x>0 and y==0:
    ans="右半平面X軸上"

if ans!="該點位於原點":
    print("該點位於"+ ans +"，離原點距離為根號"+str(x**2+y**2))     
else:
    print(ans)