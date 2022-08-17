# 
def odd_numbers(numlist):
    for j in range(number):
        if(numlist[j]%2!=0):
            print(numlist[j],end='')   
numlist=[]
number=int(input("please enter the total number of list elements:"))
for i in range(1,number+1):
    value=int(input("please enter the value of %delement:"%i))
    numlist.append(value)

print("odd numbers in this list are:") 
odd_numbers(numlist)   