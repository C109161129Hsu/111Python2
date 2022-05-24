use_in=input("輸入月租費型式與通話時間:")
use_string=use_in.split(",")
type=int(use_string[0])
time=int(use_string[1])
a=0.09
b=0.08
c=0.07
d=0.06
if type==186:
    money=round(time*a)
    if money <= 186:
        ans=money
    elif money <= 186*2:
        ans=round(money*0.9)
    else:
        ans=round(money*0.8)
elif type==386:
    money=round(time*b)
    if money <= 386:
        ans=money
    elif money <= 386*2:
        ans=round(money*0.8)
    else:
        ans=round(money*0.7)
elif type==586:
    money=round(time*c)
    if money <= 586:
        ans=money
    elif money <= 586*2:
        ans=round(money*0.7)
    else:
        ans=round(money*0.6)
elif type==986:
    money=round(time*d)
    if money <= 986:
        ans=money
    elif money <= 986*2:
        ans=round(money*0.6)
    else:
        ans=round(money*0.5)
print("通話費為:"+str(ans))