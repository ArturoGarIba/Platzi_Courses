'''
EXPORTATION EXPLICIT
'''
from package.module_1 import func1, func2
from package.module_2 import func3, func4

print(func1())
print(func2())
print(func3())
print(func4())

import package
print(package.URL)

'''
ANOTHER WAY OF IMPORTATION WITH NAMESPACE
'''
import package as pkg
print(pkg.URL)
print(pkg.module_1.func1())



