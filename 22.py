correct=0
data=[["123","456","9000"],["456","789","5000"],["789","888","6000"],["336","558","10000"],["775","666","12000"],["566","221","7000"]]
use_in =int(input("輸入查詢組數N為:"))
for j in range(use_in):
    use_data =input().split(" ")
    correct=0
    for i in range(6):
        if data[i][0]==use_data[0] and  data[i][1]==use_data[1]:
                correct=1
                money=data[i][2]
    if correct==1:
        print(money)
    else:
        print("error")
         
          
