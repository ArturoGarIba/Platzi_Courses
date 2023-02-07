'''
EXAMPLE 1
'''
import random
# creation of dictionary
countries = ['col', 'mex','per','arg']
population2 = {country : random.randint(1,100) for country in countries}
print(population2)


# creation 2nd dictionary in base the first one with condition

result = { country: population for (country, population) in population2.items() if population > 50}
print(result)

'''
EXAMPLE 2
'''
text = 'Hola mundo, soy Arturo'
unique_vocal = { c: c.upper() for c in text if c in 'aeiou'}
print(unique_vocal)
