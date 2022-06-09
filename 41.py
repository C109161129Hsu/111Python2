times=int(input("搭了幾次電梯:"))
all=0
now=1
for i in range(times):
   n=int(input(" "))
   if n>now:
         all=all+(n-now)*20
   else:
        all=all+(now-n)*10
   now=n
print("{}元".format(all))