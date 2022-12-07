#예제 1번
a='*'
for i in range(16):
    for j in range(16):
        if(j>i):
            print(a,end='')
    print('\n')

#예제 2번
for i in range(8):
    if(i==3):
        break
    for j in range(8-i):
        print(' ',end='')
        if(i==0 and j==7):print('*',end='')
    for j in range(i):
        print('*',end='')
    for j in range(8):
        if(j<i):
            print("*",end='')    
    print('\n')
for i in range(8):
    if(i==0 or i==1):
        continue
    for j in range(8,0,-1):
        if(j<=i+1):
            print('*',end="")
        else:
            print(" ",end="")
    for j in range(8):
        if(j<i):
            print("*",end='')
    print('\n')          
