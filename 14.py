import os
os.system("clear")
def funk(Aa):
   
    return [value for value in Aa.values() if isinstance(value, str)]
Aa = {'a': 1, 'b': 'hello', 'c': 3, 'd': 'world', 'e': 5.5}
strings =funk(Aa)
print(strings)
