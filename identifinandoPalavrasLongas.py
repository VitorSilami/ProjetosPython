# Entrada de texto
texto = input("Digite um texto: ")

# Separar palavras
palavras = texto.split() # Divide o texto em palavras com base nos espaços

# Lista para armazenar palavras longas
palavras_longas = []

# Verificar tamanho de cada palavra
for palavra in palavras:
    if len(palavra) > 10: # Verifica se a palavra tem mais de 10 letras
        palavras_longas.append(palavra) # Adiciona à lista se tiver mais de 10 letras

# Exibir resultado
if palavras_longas:
    print("Palavras com mais de 10 letras:")
    for p in palavras_longas:
        print("-", p)  # Imprime cada palavra longa encontrada
else:
    print("Nenhuma palavra com mais de 10 letras foi encontrada.")