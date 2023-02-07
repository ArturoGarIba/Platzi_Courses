
items = [
  {
    'product' : 'jeans',
    'price': 250
  },
  {
    'product' : 'shirt',
    'price': 450
  },
  {
    'product' : 'shoes',
    'price': 1250
  }
]

prices = list(map(lambda item: item['price'], items))
print(prices)

# Here i fixed the problem of the editing of both lists
def add_taxes(item):
  new_item = item.copy() # Creating a copy of the list to not edit the item list
  new_item['taxes'] = item['price'] * .19
  return new_item

print('New list')
new_items = list(map(add_taxes, items))
print(new_items)
print('Old list')
print(items)
