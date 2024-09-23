# Listas são coleções de dados mutáveis. E elas podem conter elementos de diferentes tipos 
# e voce pode realizar algumas operções nas listas
#--------  0  1  2  3  
lista1 = [ 1, 2, 3, 4]  

# Adicionar um novo elemento na nossa lista:
lista1.append(78)
lista1.append(0)
lista1.append(3)
lista1.append(1)


print(lista1)

# Remover um elemento específico da minha lista 
lista1.remove(3)
print(lista1)

#ordenar
lista1.sort()
print(lista1)

# Contar elementos 

print(lista1.count(1))
print(lista1.count(78))

# Remover elemento do final
lista1.pop()
print(lista1)

# Fatiamento ou Slicing

# Todos os itens da lista:
todos = lista1[:]
print(f"Todos: {todos}")

# Todos os indices 1 ao 2
# o primeiro parametro é inicio do intervalo que eu desejo iniciar
# o segundo é o parametro de parada
# e o terceiro é de quantas em quantas casas eu quero andar
slice1 = lista1[0:3]
print(f"Slice1 : {slice1}")

#Quero pegar do início:
# eu inicio da posição 0
# e eu vou parar na posição 3
slice0 = lista1[:3]
print(f"Slice0 : {slice0}")


# Quero pular itens de 2 em 1
slice2 = lista1[1:5:2]
print(f"slice2: {slice2}")

# Reverter a minha lista
revert = lista1[::-1]
print(revert)

# Percorrer a lista com passos negativos:
neg_pass = lista1[5:1:-1]
print(neg_pass)



