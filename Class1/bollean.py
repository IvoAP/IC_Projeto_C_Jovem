# Bolleanas em python
# True (1)
# False (0)


# Vou levar um guarda chuva AND um casaco:  
# Tabela Verdade do AND
#  1   1   ->  1
#  1   0   ->  0
#  0   1   ->  0
#  0   0   ->  0

#Tabela verdade do Ou lógico

# Vou levar um guarda chuva OR um casaco
#  1    1  -> 1
#  1    0  -> 1
#  0    1  -> 1
#  0    0 ->  0

# Tabela verdade do nao
# Vou levar um guarda chuva 
#  1  ->  0
#  0  ->  1

#Tabela verdade do OU exclusivo
# 1    1 -> 0
# 1    0 -> 1
# 0    1 -> 1
# 0    0 -> 0

# Operações Booleanas
# E lógico
# OU lógico
# Negação lógica
# Ou Exlusivo

b = True
c = True

print(f"O AND LÓGICO: {b and c}")
print(f"O OU LÓGICO: {b or c}")
print(f"Negação Lógica {not b}")
print(f"Ou exclusivo lógico {b != c}")

