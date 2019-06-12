ch = 'y'
while (ch == 'y'):
    num_s = input("Enter a number : ")
    num = int(num_s)
    flag = 0
    i=2
    while (i < num**(0.5)):
        if (num % i == 0):
            flag = 1
            break
        i=i+1
    if (flag == 1):
        print( "The entered number ", num, " is Composite")
    else:
        print ("The entered number ", num, " is Prime")
    ch = input("Do you want to continue(y/n) : ")
