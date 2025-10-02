cpf = input("Digite o CPF (apenas números): ")

# Verifica se tem 11 dígitos e se são apenas números
if len(cpf) == 11 and cpf.isdigit():
    print("✅ CPF válido no formato (11 dígitos numéricos).")
else:
    print("❌ Erro: O CPF deve conter exatamente 11 dígitos numéricos.")