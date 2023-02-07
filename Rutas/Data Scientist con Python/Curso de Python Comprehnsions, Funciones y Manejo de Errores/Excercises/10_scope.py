price = 100 # global scope

def increment():
  price = 10
  result = price + 10
  print(price)

increment()
print(result) # Gives an error cause variable result is defined in a scope unreachable