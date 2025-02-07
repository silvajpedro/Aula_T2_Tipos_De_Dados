# Data Age 2025 -International Data Corporation
# 1,3 GB de dados por dia

# Listas --> Array, Vetores ou Matrizes -> São estruturas que conseguem guardar uma quantidade quase infinita de informação, porém não estão organizadas.

lista_dos_sonhos = ["Aposentar Cedo", "Amandah quer ser Mãe", "Visitar a Suíça", "Uma conta na Suíça cheia de money que a fernanda vai pagar!!!", "Emprego Home Office!!!"]

print(lista_dos_sonhos)
print(type(lista_dos_sonhos))

# Índices

print(lista_dos_sonhos[0], lista_dos_sonhos[1])

# Índexação negativa

print(lista_dos_sonhos[-1], lista_dos_sonhos[-2])

# len() -> retorna o tamanho total da nossa lista

# print(len(lista_dos_sonhos))

# insert -> adiciona uma informação na posição que quisermos em nossa lista

# lista_dos_sonhos.insert(0,"Fernanda pagar todas as minhas dívidas!!!")
# print(lista_dos_sonhos)

# append -> adiciona uma informação ao final da nossa lista

# lista_dos_sonhos.append("Ficar rica e viajar o mundo todo!!!")

# sort -> Ele ordena em ordem alfanúmerica (números e letras) todos os nossos valores dentro da lista

# nomes_que_ela_esta_devendo = ['Tayna', "Nathalia", "Frank", "Enzo", "Lucas", "Camila", "Tulani", "Mayke", "Mônica", "Bianca", "Felipe", "Ana Luiza", "Henrique", "Audrey"]

# nomes_que_ela_esta_devendo.sort()
# nomes_que_ela_esta_devendo.sort(reverse=True)

# print(nomes_que_ela_esta_devendo)

# valores = [1, 15, 678, 987, 4356, 2975, 0, 987]

# valores.sort()

# print(valores)

# remove

# valores.remove(0)
# valores.remove(1)
# valores.remove(987)
# print(valores)

# pop --> remover um valor a partir do seu índice

lista_comidas = ["Hamburguer", "Lasanha", "Macarrão", "Rato Frito"]
#                     0            1          2            3
# print(lista_comidas)

# lista_comidas.pop(3)

# print(lista_comidas)

pessoas_cadastradas = []

qntd_pessoas = int(input("Digite quantas pessoas você quer cadastrar no Sistema:"))

while len(pessoas_cadastradas) < qntd_pessoas:
    pessoas_cadastradas.append(input(f"Digite o nome da pessoa que você ira cadastrar: "))

print(pessoas_cadastradas)