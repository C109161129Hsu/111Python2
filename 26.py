count=0
use_in =input("檢測的字串(end結束):")
use_limit =input("檢測的單一字元:")
while use_in !="end":
    count=0
    for i in range(len(use_in)):
            if use_in[i]==use_limit:
                count+=1
    print("字元" + use_limit+"出現次數為" +str(count))
    use_in =input("檢測的字串(end結束):")
    if use_in=="end":
        print("測驗結束")
    else:
        use_limit =input("檢測的單一字元:")
 