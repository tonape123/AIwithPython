#python program to print all numbers between 1 to 100
for n in range(1,100):
    count = 0
    for i in range(2,(n//2+1)):
        if(n%i==0):
            count = count+1
            break
    if(count==0 and n!=1):
        print("%d " %n , end="")