'''
Creati o expresie lambda care va afisa o lista data ca input ridicata la patrat.
ex: my_list = [1, 2, 3] => [1, 4, 9]
'''
my_list = [1, 2, 3]
new_list = list(map(lambda x: x ** 2, my_list))
print(new_list)

'''
Sortati urmatoarea lista dupa a 2-a valoare din fiecare tuplu folosind expresii
Lambda:
ex: a = [(0, 2), (4, 3), (9, 9), (10, -1)]
sorted_a = [(10, -1), (0, 2), (4, 3), (9, 9)]
'''

a = [(0, 2), (4, 3), (9, 9), (10, -1)]
sorted_a = sorted(a, key=lambda x: x[1])
print(sorted_a)

'''
Scrieti un program Python pentru a filtra o lista de numere intregi folosind
expresii Lambda si functia filter().
ex: orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = [2, 4, 6, 8, 10]
odd_list = [1, 3, 5, 7, 9]
'''

orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda x: x % 2 == 0, orig_list))
print(even_list)
odd_list = list(filter(lambda x: x % 2 != 0, orig_list))
print(odd_list)

'''
Scrieti un program pentru a extrage anul, luna, data si ora folosind Lambda.
ex: 2023-04-24 09:03:32.744178
2023
04
24
09:03:32.744178
'''

date = "2023-04-24 09:03:32.744178"
extract = lambda x: (x.split()[0][:4], x.split()[0][5:7], x.split()[0][8:10], x.split()[1][0:])
an, luna, zi, ora = extract(date)
print(an)
print(luna)
print(zi)
print(ora)
