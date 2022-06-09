all_locate=int(input(""))
for i in range(all_locate):
    k=int(input(""))
    if k % 9==0 or k%11==0:
        print("第{}個點 {}".format((i+1),k))
    

