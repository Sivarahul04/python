import ftplib


row  = 6
for i in range(row):
    for j in range(row-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()
    
print()

rows = 6
for i in range(rows):
    for j in range(i):
        print(" ",end="")
    for j in range(2*(row-i)-1):
        print("*",end="")
    print()