import math
from pickletools import long1
x=""
y=""
use_in =str(input("請輸入連續字元:"))


if use_in[::-1]== use_in[:]:
    print("Yes")
else:
    print("NO")
