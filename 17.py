
num_sp=[]
x=2
y=2
for j in range(2):
    use_in =str(input()).split(" ")
    row=int(use_in[0])
    num=int(use_in[1])
    if row==x and num==y:
        for i in range(row):
   
            num_sp.append(str(input()).split(" "))
            use_num=''
    else:
        print("兩個矩陣無法相加")
        exit()
    x=row
    y=num
    row=0
    num=0
one=int(num_sp[0][0])+int(num_sp[2][0])
two=int(num_sp[0][1])+int(num_sp[2][1])
three=int(num_sp[1][0])+int(num_sp[3][0])
four=int(num_sp[1][1])+int(num_sp[3][1])
print(str(one)+" "+str(two)+"\n "+str(three)+" "+str(four))



