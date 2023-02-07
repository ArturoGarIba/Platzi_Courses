# Definition of list from mapping another one
numbers = [1,2,3,4]
numbers2 = list(map(lambda i : i * 2, numbers))

print(numbers2)