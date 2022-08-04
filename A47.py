#python - extract digits from tuple list
test_list = [(15, 3), (3, 9), (1, 10), (99, 2)]

print("The original list is : " + str(test_list))
x=""

for i in test_list:
    for j in i:
        x+=str(j)
res=list(map(int,set(x)))

print("The extracted digits : " + str(res))
