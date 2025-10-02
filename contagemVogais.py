texto = input("Digite um texto: ")
vogais = "aeiouAEIOU"
contador = 0

for letra in texto:
    if letra in vogais:
        contador += 1

print("O texto contém", contador, "vogais.")
print("As vogais sao: ", end=" ")
for letra in texto:
    if letra in vogais:
        print(letra, end=" ")
print()