# String são um conjunto de caracteres 
# ''
# ""
# 'a'
# 'falou'

texto = '           Python é incrível                    '
print(texto)

# 1 -  Remover espaços extras
texto_strip = texto.strip()
print(f"{texto_strip}")

# Conversão pra maiúscula
texto_upper = texto.upper()
print(f"{texto_upper}")

# Conversão pra minúscula
texto_lower = texto.lower()
print(f"{texto_lower}")

# Substuir string
texto_replace = texto.replace("incrível", "fantástico")
print(f"{texto_replace}")

# Dividir a string
texto_split = texto.split()
print(f"{texto_split}")

# tamanho da string
print(f"tamanho total de texto: {len(texto)}")
print(f"tamanho total de texto split: {len(texto_split)}")

# Verificar se um string começa com algum carctere
inicio = texto_strip.startswith("Python")
print(f"{inicio}")