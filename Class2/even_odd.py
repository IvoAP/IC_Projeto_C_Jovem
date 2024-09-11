num = int(input("insira um número: "))

# Tabela verdade do and 
# v1 e v2 and  answer
# 1    0     0
# 1    1     1
# 0    0     0
# 0    1     0

#2 = 10 and 1 =  0
# 3 = 11 and 1 = 1
# 4 = 100 and 1
# 6 = 1000 and 1

# and  = &
# or = |


if num & 1 == 0:
    print("Numero é par")
else:
    print(" Número é ímpar")