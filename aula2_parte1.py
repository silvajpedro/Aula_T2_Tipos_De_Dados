# =============================
# Exemplo 1: Loop 'while'
# =============================

# Inicializamos a variável 'pessoas' com o valor 1.
pessoas = 1

# Enquanto o valor de 'pessoas' for menor ou igual a 38, o bloco de código será executado.
while pessoas <= 38:
    print(f'A queridíssima instrutora Fernanda deve {pessoas} pessoas')
    pessoas += 1  # Incrementamos 'pessoas' em 1 a cada iteração

print("Fim do loop 'while'.")

# Obs: Cuidado com loops 'while' que não alteram a condição de parada, pois podem gerar loops infinitos.
# Exemplo (comentado para não travar o programa):
# pesquisa = "Ayr Frier"
# while pesquisa == "Ayr Frier":
#     print("Este bloco seria executado infinitamente!")

# =============================
# Exemplo 2: Loop 'for' iterando sobre listas
# =============================

# Lista de pessoas que Fernanda deve
lista_pessoas_fernanda_deve = [
    "Emanuelle", "Karyne", "Leonardos", "Jakeline", "Danilo", "Yuri", "Graziele"
]

print("Lista de pessoas que Fernanda deve:")
for pessoa in lista_pessoas_fernanda_deve:
    print(pessoa)

print("Fim do loop 'for' sobre a lista de pessoas.")

# Lista de marcas de airfryer
airfryer = [
    "Philco", "Polishop", "Samsung", "Mondial", "Wallita", "Brastemp", "Cadense"
]

print("Lista de marcas de airfryer:")
for marca in airfryer:
    print(marca)

print("Fim do loop 'for' sobre a lista de marcas.")

# =============================
# Exemplo 3: Loop 'for' utilizando a função range
# =============================

print("Imprimindo números de 0 a 9 usando 'range':")
for numero in range(10):  # range(10) gera números de 0 até 9
    print(numero)

print("Fim do loop 'for' com range.")

# =============================
# Exemplo 4: Manipulação de Strings
# =============================

# Exemplo 4.1: Manipulando uma única string
usuario = "fernANDA pix"

print("Manipulação de string (exemplo com uma única string):")
print("Original:", usuario)
print("Uppercase (tudo maiúsculo):", usuario.upper())
print("Lowercase (tudo minúsculo):", usuario.lower())
print("Replace (substitui 'pix' por 'Correa'):", usuario.replace("pix", "Correa"))
print("Capitalize (apenas a primeira letra em maiúsculo):", usuario.capitalize())

# Exemplo 4.2: Manipulando uma lista de strings
# Aqui, temos uma lista com duas strings. Alguns métodos de string não podem ser aplicados diretamente na lista,
# mas podemos, por exemplo, unir os elementos ou iterar sobre cada um para aplicar transformações.

lista_usuaria = ["fernANDA", "pix"]

# Usando join para unir os elementos da lista com "--" entre eles:
print("-".join(lista_usuaria))
print("Manipulação de string (exemplo com uma lista de strings):")
# print("String unida com '--':", string_unida)

# Definindo a string com nomes separados por vírgula
nomes = "Alice-Bob-Charlie-David"

# Utilizando o split diretamente dentro do print para transformar a string em uma lista
print("Lista de nomes:", nomes.split("-"))

# Se quisermos aplicar um método de string a cada elemento da lista, podemos iterar sobre ela:
print("Elementos da lista em lowercase:")
for elemento in lista_usuaria:
    print(elemento.lower())
