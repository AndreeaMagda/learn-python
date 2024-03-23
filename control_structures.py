'''
   1. Tricky picture:
        picture = [
        [0,0,0,1,0,0,0],
        [0,0,1,1,1,0,0],
        [0,1,1,1,1,1,0],
        [1,1,1,1,1,1,1],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0]
        ]
'''

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


def draw_picure(picture):
    for row in picture:
        for number in row:
            print('x' if number == 1 else ' ', end='')
        print()


print(draw_picure(picture))

'''
    Verificati daca o lista contine duplicate si adaugati-le intr-o alta lista.
    ex: a = [2, 4, 2, 2, 6, 1, 2 , 1]
    duplicate = [2, 1]
'''


def find_duplicates(list):
    counts = {}
    duplicates = []

    for item in list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    for item, counts in counts.items():
        if counts > 1:
            duplicates.append(item)

    return duplicates


a = [2, 4, 2, 2, 6, 1, 2, 1]
print("Elementele duplicate sunt:", find_duplicates(a))

'''
    Verificati daca un numar întreg, citit de la tastatura, este perfect.
    ex: 6, 28, 496
'''

number = int(input("Introduceti un nr intreg pozitiv: "))

suma_divizori = sum(i for i in range(1, number) if number % i == 0)

if suma_divizori == number:
    print(number, "este perfect")
else:
    print(number, "nu este perfect")

'''
    Verificati daca doua numere intregi, citite de la tastatura, sunt prietene. Doua
    numere naturale diferite a si b se numesc prietene daca suma divizorilor lui a
    fara a este egala cu b si suma divizorilor lui b fara b este egala cu a.
    ex:(220,284), (1184,1210),(2620,2924)
    220: 1+2+4+5+10+11+ 20+ 22+44+55+110 = 284
    284: 1+2+4+71+142 = 220
'''


def suma_div(number):
    return sum(i for i in range(1, number) if number % i == 0)


number_one = int(input("Introduceti primul  nr : "))
number_two = int(input("Introduceti al 2 lea  nr : "))
if suma_div(number_one) == number_two and suma_div(number_two) == number_one:
    print("Sunt prietene")
else:
    print("Nu sunt prietene")

'''
    Verificati daca un cuvant este palindrom.
'''

something = input("Scrie un cuvant: ")
if something == something[::-1]:
    print("Este palindrom!!")
else:
    print("Nu este palinrom")

'''
    Creati o lista cu elementele pare dintr-o alta lista.(intr-o singura linie de cod -
    hint: list comprehension)
'''

lista_orig=[2,7,5,6,9,12,14,4]
lista_para= [i for i in lista_orig if i%2==0 ]
print("Lista de nr pare este: ",lista_para)

'''
    Creati o lista care contine doar elementele comune din 2 liste(fara duplicate).
    Extra:
    ● generati random cele 2 liste
    ● rezolvati intr-o singura linie de cod
'''

import random

lista_comuna = list(set(random.sample(range(1, 20), 10)) & set(random.sample(range(1, 20), 10)))

print("Elementele comune din cele două liste:", lista_comuna)
