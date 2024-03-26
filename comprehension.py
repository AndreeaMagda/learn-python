"""
Să presupunem că aveți două liste de numere și doriți să creați o funcție care
va returna o listă de tupluri în care fiecare tuplu va conține suma elementelor
corespunzătoare din cele două liste. Pentru a face acest lucru, veți utiliza
funcția zip() pentru a itera prin cele două liste și a aduna elementele
corespunzătoare.
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
result = sum_lists(list1, list2)
print(result) # Output: [11, 22, 33, 44, 55]
"""


def sum_lists(list1, list2):
    return [a + b for a, b in zip(list1, list2)]


list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
result = sum_lists(list1, list2)
print(result)




'''
List Comprehension:
● Creati o lista cu numere pare de la 0 la 100.
● Creati o lista care contine cuburile primelor 10 numere intregi.
● Creati o lista care contine toate elementele comune din doua liste date.
'''

list_even=[i for i in range(101) if i%2==0]
print(list_even)

list_cubes=[i**3 for i in range(1,11) ]
print(list_cubes)

list_one = [1, 2, 3, 4, 5]
list_two = [4, 3, 6, 7, 8]
common_elements = [i for i in list_one if i in list_two]
print(common_elements)


'''
Set Comprehension:
● Creati un set care contine primele 10 numere pare.
● Creati un set care contine toate literele distincte dintr-un string dat.
● Creati un set care contine toate cuvintele care au cel putin 5 litere
dintr-un string dat.
'''

even_set={i for i in range(20) if i%2==0}
print(even_set)

s="racing formula 1"
string_set={char for char in s if char.isalpha()}
print(s)
print(string_set)

phrase="Racing in Formula 1 is the best sport in the world"
phrase_set={word for word in phrase.split() if len(word)>=5}
print(phrase_set)


'''
Dictionary Comprehension:
● Creati un dictionar cu numerele de la 1 la 10 ca si chei si patratelele lor
ca si valori.
● Creati un dictionar care contine literele unui string dat ca si chei si
numarul de aparitii ale fiecarei litere ca si valori.
● Creati un dictionar care contine primele 10 numere intregi ca si chei si
lista lor de divizori ca si valori.
'''
squares_dict = {i: i**2 for i in range(1, 11)}
print(squares_dict)

race="Charles Leclerc "
letter_dict={char: race.count(char) for char in race if char.isalpha()}
print(letter_dict)

def find_divisors(n):
    return [i for i in range(1, n+1) if n % i == 0]

divisors_dict = {i: find_divisors(i) for i in range(1, 11)}
print(divisors_dict)
