'''

Scrieți o expresie lambda care primește două șiruri și returnează concatenarea lor, inversată.
    s1 = ‘exemplu’
    s2= ‘Python’
    concatenare_inversata = > ‘nohtypulpmexe’
'''

s1='lando'
s2='carlos'

concatenare_inversata = (lambda x, y: (x + y)[::-1])(s1, s2)
print(concatenare_inversata)


'''
 Implementați un program care să elimine elementele duplicate dintr-o listă folosind un set.
'''


lista_initiala = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7, 8, 8, 8, 8, 9]
setul = set(lista_initiala)
lista_fara_duplicate = list(setul)
print(lista_fara_duplicate)

'''
Scrieți un program care să 
folosească funcția map() pentru a dubla fiecare element dintr-o listă de numere întregi.
'''
my_list = [1, 2, 45]
new_list = list(map(lambda x: x * 2, my_list))
print(new_list)

'''
 Scrieți un program care să creeze o listă de cuvinte și să
  afișeze fiecare cuvânt împreună cu lungimea sa.
'''

lista_cuvinte = ["racing", "lando", "drs", "charles", "redbull"]

for cuvant in lista_cuvinte:
    print(f"Cuvânt: {cuvant}, Lungime: {len(cuvant)}")


'''
Implementați un program care să folosească list comprehensions pentru a genera o 
listă de pătrate ale numerelor de la 1 la 10.
'''

patrate = [i**2 for i in range(1, 11)]

print(patrate)


'''

10. Implementați un program care să sorteze o listă de tuple în funcție de al doilea element folosind o expresie lambda.
* Original list of tuples:
        [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
* Sorting the List of Tuples:
        [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)] 

'''

lista = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
lista_sortata = sorted(lista, key = lambda x: x[1])

print(lista_sortata)


'''
Scrieți o funcție numită putere care primește două numere întregi x și n și returnează x ridicat la puterea n.

'''

def putere(x,n):
    return x ** n
print(putere(5,2))



'''
Implementați o funcție numită cuvinte_lungi care primește o listă de șiruri și utilizează funcția filter
pentru a returna o listă care conține doar cuvintele cu lungimea mai mare de 5 caractere.
'''
formula_one=['Verstappen','race','charles']
def cuvinte_lungi(lista):
    return list(filter(lambda x: len(x) > 5, lista))

print(cuvinte_lungi(formula_one))