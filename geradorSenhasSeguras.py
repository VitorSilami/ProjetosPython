import random

# Conjuntos de caracteres
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
especiais = "!@#$%^&*()_+-=[]{};:,.<>?/"

# Garantir pelo menos um de cada tipo
senha = []
senha.append(random.choice(maiusculas))  # 1 letra maiúscula
senha.append(random.choice(minusculas))  # 1 letra minúscula
senha.append(random.choice(numeros))     # 1 número
senha.append(random.choice(especiais))   # 1 caractere especial

# Preencher os outros 8 caracteres restantes com qualquer tipo
todos_caracteres = maiusculas + minusculas + numeros + especiais
for i in range(8):
    senha.append(random.choice(todos_caracteres))

# Embaralhar a lista para a senha ficar aleatória
random.shuffle(senha)

# Transformar a lista em uma string
senha_final = "".join(senha)  # Concatena os caracteres em uma única string

# Mostrar a senha
print("Senha gerada:", senha_final)
