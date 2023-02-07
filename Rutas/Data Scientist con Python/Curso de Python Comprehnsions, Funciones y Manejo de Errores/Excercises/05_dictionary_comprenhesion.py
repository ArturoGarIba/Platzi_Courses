'''
EXAMPLE 1
'''
# 1st way to create a dictionary automatically
dictionary = {}
for i in range(1,11):
  dictionary[i] = i * 2
print(dictionary)

# 2nd way (better)
dictionary_comprenhesion = {i: i *2 for i in range(1,11)}
print(dictionary_comprenhesion)

'''
EXAMPLE 2
'''
import random
# 1st way
countries = ['col', 'mex','per','arg']
population = {}
for country in countries:
  population[country] = random.randint(1,100)
print(population)

# 2nd way
population2 = {country : random.randint(1,100) for country in countries}
print(population2)

'''
EXAMPLE 3
'''
name = ['juan','denis','arturo']
age = [20,31,30]
list_people = list(zip(name,age))
dict_comp = {name:age for (name,age) in zip(name,age)}
print(dict_comp)
