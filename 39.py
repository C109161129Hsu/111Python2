for i in range(4):
    for k in range(4-i):
          print(" ",end="")
    if i ==0:
        for k in range(4-i):
          print(" ",end="")
        for j in range(i+1):
            print("+ ",end="")
    else:
        for k in range(4-i):
          print(" ",end="")
        for j in range(i+(i+1)):
            print("+ ",end="")
        
    print( )

for i in range(5):
  

    if i !=5:
           for j in range(5-(i+(i+1))):
            print("+ ",end="")
    
    else:
        for j in range(1):
            print("+ ",end="")

          
    print( )