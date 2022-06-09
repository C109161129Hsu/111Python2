use_all=""
ans_list=[]
all=input("輸入矩陣的維度:").split(' ')
for i in range(int(all[0])*2):
    use_in=str(input(""))
    if i==0:
        use_all=use_in+use_all
    else:
        use_all=use_all+" "+use_in
use_list=use_all.split(' ')

if all[1]=="2":
    for i in range(4):

        a=int(use_list[i])*int(use_list[i+4])
        ans_list.append(a)
    print(str(ans_list[0])+" "+str(ans_list[1]))
    print(str(ans_list[2])+" "+str(ans_list[3]))
else:
    for i in range(6):
        a=int(use_list[i])*int(use_list[i+6])
        ans_list.append(a)
    print(str(ans_list[0])+" "+str(ans_list[1])+" "+str(ans_list[2]))
    print(str(ans_list[3])+" "+str(ans_list[4])+" "+str(ans_list[5]))
