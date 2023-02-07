def find_volume(length=1, width=1, depth=1):
  return length * width * depth, width, 'hola'

volume, w, str = find_volume(1, 23, 9)

print(volume)
print(w)
print(str)