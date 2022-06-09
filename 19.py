

use_put =int(input("測試的資料量:"))
for i in range(use_put):
    use_in =input().split(" ")
    if use_in[2]=="O":
        if (use_in[0]=="O"  or use_in[0]=="A" or use_in[0]=="B"or use_in[0]=="AB" )and use_in[1]=="AB":
            print("IMPOSSIBLE")
        else:
            print("YES")

    if use_in[2]=="A":
        if   use_in[1]=="O"or use_in[1]=="B" and use_in[0]=="O" or (use_in[1]=="B" and use_in[0]=="B"):
            print("IMPOSSIBLE")
        else:
            print("YES")


    if use_in[2]=="B":
        if use_in[1]=="O"or use_in[1]=="A" and use_in[0]=="O" or use_in[1]=="A" and use_in[0]=="A" :
            print("IMPOSSIBLE")
        else:
            print("YES")

    if use_in[2]=="AB":
        if use_in[0]=="A" or use_in[0]=="B" or use_in[0]=="AB" and use_in[1]=="AB" or use_in[0]=="A" and use_in[1]=="B":
            print("YES")
        else:
            print("IMPOSSIBLE")