set_countries = {'mexico', 'colombia', 'bolivia', 'mexico'}

size = len(set_countries)
print(size)
# Search object in set array
print('colombia' in set_countries)
print('argentina' in set_countries)

# Add elements in set
set_countries.add('peru')
print(set_countries)

# Update
set_countries.update({'argentina', 'peru','ecuador'})
print(set_countries)

# Remove
set_countries.remove('argentina')
set_countries.discard('argentina')
print(set_countries)

# Clear all the set
set_countries.clear()
print(set_countries)