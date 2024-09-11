#são coleções não ordenadas de itens únicos. Não permitem duplicatas e suportam operações matemáticas como união e interseção.

conjunto = {1,2,3,4,5,6}

#Adicionar um item
conjunto.add(7)
print(conjunto)

#Remover o item
conjunto.remove(7)
print(conjunto)

#União
novo_conjunto = {4,6,10,12}
uniao = conjunto.union(novo_conjunto)
print(uniao)

#Intersecção
intersection = conjunto.intersection(novo_conjunto)
print(intersection)