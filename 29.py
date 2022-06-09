ans=[]
甲=input("甲方的數字:")
乙=input("乙方的數字:")
for i in range(len(甲)):
 
    x=int(甲[i])
    y=int(乙[i])
    if x==y:
        ans.append("和")
    elif  x ==1 and  y==3 or x ==3 and  y==1 or x==4 and y==2 or x==2 and y==4:
        ans.append("和")
    
    elif( x==5 and y==4)or(x==1 and y==5) or (x==2 and y==1) or (x==3 and y==2) or ( x==4 and y==3) :
         ans.append("贏")

    elif(x==4 and y==5)or(x==5 and y==1) or (x==1 and y==2 )or (x==2 and y==3) or( x==3 and y==4 ) :
          ans.append("輸")
print(ans)

