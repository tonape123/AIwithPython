#python programtocalculate compound interest
p=float(input("enter principle value"))
t=float(input("enter term value"))
r=float(input("enterrate of interest"))
ci=p*(pow((1+r/100),t))
print(ci)
