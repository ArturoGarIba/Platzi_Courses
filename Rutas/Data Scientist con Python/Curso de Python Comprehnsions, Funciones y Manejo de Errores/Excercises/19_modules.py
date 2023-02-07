import sys

print(sys.path)

# This module is used to declare regular expressions
import re

text = 'My telephone number is 438 111 00 00, el codigo de pais es +52'
result = re.findall('[0-9]+', text)
print(result)

#Module used to obtain date and localtime
import time

timestamp = time.time()
local_hour = time.localtime()
result = time.asctime(local_hour)
print(timestamp)
print(result)

# Module to manage collections of data
import collections

numbers = [1,2,4,31,1,12,1,2,2,2,2,1,1,12,2]
counter = collections.Counter(numbers)
print('Counter : ', counter)