all_p=[]
a=0
use_in=int(input("小明身上有幾元:"))
use_class=int(input("販賣機有幾種飲料:"))
for i in range(use_class):
    use_p=int(input(""))
    if use_p<=use_in:
        a+=1
print(a)

