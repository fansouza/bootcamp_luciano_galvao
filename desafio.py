# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite o seu nome:")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Digite o seu salário:"))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
valor_bonus = float(input("Digite o valor do bônus:"))

# 4) Calcule o valor do bônus final
valor_bonus_final = 1000 + salario * valor_bonus


# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bonus
print(f"O usuário: {nome_usuario} tem o valor do bônus de {valor_bonus_final}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
