import math

num = int(input("Insira um nnúmero: "))
flag = True

if num == 1 or num == 0:
    flag = False
if num == 2:
    flag = True

for i in range(2,int(math.sqrt(num) + 1)):
    print(i)
    if num%i == 0:
        flag = False
        break

if flag:
    print(f"O número : {num} é primo")
else:
    print(f"O número {num} não é primo")