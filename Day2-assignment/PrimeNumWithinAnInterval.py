import math
n = eval(input('Enter a val: '))
li = [2,3]
for i in range(4,n+1):
    for j in range(2, int(math.sqrt(i) + 1)):
        if i % j == 0:
            flag = 1
            break
        flag = 0
    if flag == 0:
        li.append(i)
print(li)
