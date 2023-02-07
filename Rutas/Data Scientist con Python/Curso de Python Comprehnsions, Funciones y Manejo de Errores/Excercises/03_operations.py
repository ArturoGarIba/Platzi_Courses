set_countries1 = {'mex','bol','col'}
set_countries2 = {'peru','col'}

# Union of both sets
# 1st way
set_countries3 = set_countries1.union(set_countries2)
print(set_countries3)
#2nd way
set_3 = set_countries2 | set_countries1
print(set_3) 

# Intersection of both sets (elements in common)
# 1st way
set_intersection = set_countries1.intersection(set_countries2)
print(set_intersection)
# 2nd way
set_inter = set_countries1 & set_countries2
print(set_inter)


# Difference
set_difference = set_countries1.difference(set_countries2)
print(set_difference)
# 2nd way
set_diff = set_countries1 - set_countries2
print(set_diff)


#Symmetric difference
set_symetric_diff = set_countries1.symmetric_difference(set_countries2)
print(set_symetric_diff)
# 2nd way
set_sym_diff = set_countries1 ^ set_countries2
print(set_sym_diff )


