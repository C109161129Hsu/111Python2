
import numpy as np
allnumber=""
all_max=[]
use_list=[]
big=0
for i in range(3):
     use_in=input().split(" ")
     big=big+int(max(use_in))
     all_max.append(max(use_in))
     use_list.append(use_in)
print("最大值為:" + str(big))  
for i in range(3):
  use_list=np.array(use_list)
  number=all_max[i]
  results=np.where(use_list==number)
  print("位置為" +str(results))