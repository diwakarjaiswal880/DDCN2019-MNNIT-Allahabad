n=int(input("Enter no of rows: "))
for i in range(1,n+1):
    print(' '*2*(n-i),end=' ')
#    for j in range(i,n):
#        print(' ',end='')
    for j in range(1,i+1):
        print(j,end=' ')
    print()    