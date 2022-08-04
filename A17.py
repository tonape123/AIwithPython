#python program to find numbers divisible by another no
num1 = int(input("Enter First  Number  "))
num2 = int(input("Enter Second Number "))

if num1%num2==0:
  print("\n" +str(num1)+ " is divisible by " +str(num2))
else:
  print("\n" +str(num1)+ " is not divisible by " +str(num2))