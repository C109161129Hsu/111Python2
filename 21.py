

data=[["123","Tom","DTGD"],["456","Cat","CSIE"],["789","Nana","ASIE"],["321","Lim","DBA"],["654","Won","FDD"]]
use_in =str(input("輸入查詢學號為:"))
for i in range(5):
        if data[i][0]==use_in:
            print("學生資料為:" + data[i][0] + " " +data[i][1] +" "+data[i][2])