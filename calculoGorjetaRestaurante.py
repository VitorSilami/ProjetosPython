# Programa para calcular gorjeta e valor final da conta

# Entrada de dados
conta = float(input("Digite o valor da conta: R$ "))
gorjeta_percentual = float(input("Digite a porcentagem da gorjeta (%): "))

# Cálculo da gorjeta e valor total
valor_gorjeta = conta * (gorjeta_percentual / 100)
total = conta + valor_gorjeta

# Saída de dados
print(f"\nValor da gorjeta: R$ {valor_gorjeta:.2f}")
print(f"Valor total a pagar: R$ {total:.2f}")