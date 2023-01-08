import os

carros = [
        ("Chevrolet Tracker", 120,
        ("Chevrolet Onix", 90),
        ("Chevrolet Spin", 150),
        ("Hyundai Hb20", 85),
        ("Hyundai Tucson", 120),
        ("Fiat Uno", 60),
        ("Fiat Mobi", 70),
        ("Fiat Pulse", 130))
        ]
alugueis = []

print("==============================")
print("Bem Vendo à locadora de carros!")
print("==============================\n")


def mostrar_lista_de_carros (lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print(i, car)

mostrar_lista_de_carros(carros)

print("O que deseja fazer?")
print("0 - Mostrar portifólio / 1 - Alugar um carro / 2 - Devolver um carro")
res = input()


 
