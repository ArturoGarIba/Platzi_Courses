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

# Adding taxes of each item
def add_taxes(item):
  item['taxes'] = item['price'] * .19
  return item

new_items = list(map(add_taxes, items))
print(new_items)

