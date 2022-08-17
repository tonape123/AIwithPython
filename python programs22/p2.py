#python program to find the power of a numbers in a list using recursion
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("enter the base value"))
exp=int(input("enter exponential value: "))
print("Result:",power(base,exp))        