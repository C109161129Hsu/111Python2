



money=0
use_in =int(input("組數為:"))
for i in range(1,use_in+1):
    use_put=(input("第{}組".format(i)).split(" "))
    ans_int=map(int,use_put)#將STR轉為INT
    ans_list=list(ans_int)
    money=ans_list[0]*250+ans_list[1]*175
    print("第{}組應收費用:".format(i) + str(money))
