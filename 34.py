use_in=int(input("輸入一正整數:"))
if use_in % 2==0 and use_in % 11==0 and use_in % 5 !=0 and use_in % 7 !=0:
    print("{}為新公倍數?:YES".format(use_in))
else:
    print("{}為新公倍數?:NO".format(use_in))