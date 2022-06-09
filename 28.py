
ans=[]
out=0
use_1=input(" ").split(" ")
use_2=input(" ").split(" ")

out=1/(int(use_1[0])*int(use_2[1])-int(use_1[1])*int(use_2[0]))
one=round(out*int(use_2[1]),1)
two=round(out*-int(use_1[1]),1)
three=round(out*-int(use_2[0]),1)
four=round(out*int(use_1[0]),1)
print(str(one)+"  "+str(two))
print(str(three)+"  "+str(four))