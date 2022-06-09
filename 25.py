

grade=0
count=input("請輸入考試次數及學生數:").split(" ")
subject=int(count[0])
student=int(count[1])
p=input("每次考試所占的比率:").split(" ")
p_int=map(float,p)#將STR轉為INT
p_list=list(p_int)

for i in range(student):
    use_in=input("").split(" ")
    use_int=map(float,use_in)#將STR轉為INT
    use_list=list(use_int)
    for j in range(subject):
       
        grade=grade+p_list[j]*use_list[j]
print(round(grade/3,2))