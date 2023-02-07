import functools

numbers = [1,2,3,4,5]
# Using reduce
reduce = functools.reduce(lambda counter, number : counter + number, numbers)
print(reduce)