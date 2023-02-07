#import this

#Definition of set elements
# If we put 2 or more elements repeated, only one will be shown
set_countries = {'mexico', 'colombia', 'bolivia', 'mexico'}
print(set_countries)

# Could be mixed. The set sort by importance
set_types = {1, 'hola', False, 12.12}
print(set_types) # {False, 1, 12.12, 'hola'}

# Build set elements from a string
set_from_string = set('HoLa')
print(set_from_string)

# Build set from tuple 
set_from_tuples = set(('abc', 'dfe', 'ghi', 'jkl', 'abc'))
print(set_from_tuples)

#Build set from list of numbers
numbers = [1,2,3,4,1,5,6]
set_numbers = set(numbers)
print(set_numbers)

