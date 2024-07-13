import os
os.system("clear")

def main(Aa, key):
    if key in Aa:
        del Aa[key]
    return Aa

Aa = {'a': 1, 'b': 2, 'c': 3}
key = 'c'
natija = main(Aa, key)
print(natija)
