# 📌 O que é uma Tupla?
# É uma estrutura semelhante a uma lista, mas seus elementos são **imutáveis**, ou seja, **não podem ser alterados após a criação**.

# Exemplo de tupla com nomes de devedores
devedores = ("Amandah", "Ruan", "Ítalo", "Camila", "Stephanny", "Algeice", "Hayde")

# Exemplo de tupla com informações de um cliente
cliente = ("Thamyres França", 12345678912, "30/10/2001", 100000000)

# Acessando elementos da tupla pelo índice
print(f"💰 Dívida de {cliente[0]}: R$ {cliente[3]}")

# Criando uma tupla vazia e preenchendo com dados (através de conversão para lista)
usuario_VaiNoBanco = ()
usuario_VaiNoBanco = list(usuario_VaiNoBanco)  # Convertendo para lista para permitir modificações

# Adicionando informações ao usuário
usuario_VaiNoBanco.append("Camila")
usuario_VaiNoBanco.append(12332145678)
usuario_VaiNoBanco.append("09/02/2025")
usuario_VaiNoBanco.append(120000000)

# Convertendo de volta para tupla
usuario_VaiNoBanco = tuple(usuario_VaiNoBanco)

# Exibindo os dados do usuário
print("\n📌 Dados do usuário cadastrados:", usuario_VaiNoBanco)

# 📌 Funções em Python
# São blocos de código que realizam uma tarefa específica, tornando o código **mais organizado, limpo e reutilizável**.

# 🔹 Exemplo de operações matemáticas sem função (menos eficiente)
print(34354121298 + 1234546689)  # Soma direta
print(456672 - 34567)  # Subtração direta

# 🔹 Exemplo 1: Função de soma EXATAMENTE como estava no código original
def calculo_soma():
    num1 = int(input("\nDigite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    sinal = input("Digite o sinal da sua operação matemática (+, -, *, /): ")
    
    if sinal == "+":
        print(f"O resultado da soma é {num1 + num2}")

# Chamando a função
calculo_soma()

# 🔹 Exemplo 2: Função de subtração com retorno de valor
def calculo_subtracao(num1, num2):
    print("Vamos calcular")
    return num1 - num2

# Guardando o resultado da função em uma variável
resultado_subtracao = calculo_subtracao(10, 5)
