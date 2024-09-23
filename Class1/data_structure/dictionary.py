# Dicionários são coleções desordenadas de pares chave-valor. Cada valor é associado a uma chave única. 
# São mutáveis e permitem a modificação dos valores associados às chaves. Dicionários são definidos com chaves

dicionario = {
    "nome" : "João",
    "idade" : 30,
    "cidade" : "Fortaleza",
}

# Acessar um valor 
print(f"Nome : {dicionario['nome']}")
print(f"Idade : {dicionario['idade']}")
print(f"Cidade : {dicionario['cidade']}")

# Adicionar uma nova chave
dicionario['profissão'] = 'dev'
print(f"Profissão : {dicionario['profissão']}")

#Remover uma par chave valor
del dicionario['idade']
print(dicionario)

#Listar todas as chaves
print(dicionario.keys())

#Listar os valores
print(dicionario.values())