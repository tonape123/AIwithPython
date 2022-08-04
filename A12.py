# python program to find largest among three numbers
a = int(input("enter a value"))
b = int(input("enter b value"))
c = int(input("enter c value"))

if(a>b) and (a>c):
    print ("a is big",a)
if(b>a) and (b>c):
    print("b is big",b) 
if(c>a) and (c>b):
    print("c is big",c)       