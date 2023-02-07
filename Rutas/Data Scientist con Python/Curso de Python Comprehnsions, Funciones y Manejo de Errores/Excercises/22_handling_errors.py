# try 1
try:
  print(0/0)
except Exception as error:
  print(error)

# try 2
try:
  assert 1 != 1, 'One isnt different that one'
except Exception as e:
  print(e)

# try 3
try:
  age = 10
  if age < 18:
    raise Exception('No minors allowed')
except Exception as e:
  print(e)