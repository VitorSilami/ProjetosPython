import random

# Número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")

while True:
    try:
        palpite = int(input("Digite seu palpite: "))
        
        # Verifica se o número está dentro do intervalo permitido
        if palpite < 1 or palpite > 100:
            raise ValueError("O número deve estar entre 1 e 100.") #raise lança uma exceção com a mensagem personalizada
        
        # Verifica se o palpite está correto
        if palpite < numero_secreto:
            print("Mais alto! Tente novamente.")
        elif palpite > numero_secreto:
            print("Mais baixo! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou. O número era {numero_secreto}.")
            break  # Sai do loop quando acertar

    except ValueError as e:
        print("Entrada inválida:", e)
