import numbers
n=1
x=1

number=int(input("請輸入階層值M:"))
while n <= number:
    n=n*x
    x+=1
print("超過M為"+str(number)+"的最小階層N值為:"+str(x-1))