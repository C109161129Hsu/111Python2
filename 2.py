x=""
ans=0

x=0
y=0
ans=int(input("輸入一個度數(正整數)"))
one=120*2.10
two_x=210*3.02;three_x=170*4.39;four_x=200*4.97
two_y=210*2.68;three_y=170*3.61;four_y=200*4.01
if ans<=120:
   x=ans*2.10
elif ans>=121 and ans<=330:
    ans=ans-120
    x=one+ans*3.02
    y=one+ans*2.68
elif ans>=331 and ans<=500:
    ans=ans-120-210
    x=one+two_x+ans*4.39
    y=one+two_y+ans*3.61
elif ans>=501 and ans<=700:
    ans=ans-120-210-170
    x=one+two_x+three_x+ans*4.97
    y=one+two_y+three_y+ans*4.01
else:
    ans=ans-120-210-170-200
    x=one+two_x+three_x+four_x+ans*5.63
    y=one+two_y+three_y+four_y+ans*4.50
print("summer months" +str(x))
print("Non summer months" +str(y))

