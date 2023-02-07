#function 1
def increment(x):
  return x + 1
#lambda 1
increment2 = lambda x : x + 2

def high_ord_func(x, func):
  return x + func(x)

# HOF
result =  high_ord_func(2, increment)
print(result)

#High Order Function as lambda
high_ord_func_lambd = lambda x, func : x + func(x)
print(high_ord_func_lambd(3,increment2))
