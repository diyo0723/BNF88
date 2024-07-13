import os
os.system("clear")
from collections import Counter
def main (lst):
    sum  = Counter(lst)
    number = min(sum.items(), key=lambda i:i[1])
    return number
lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
natija = main (lst)
print(natija) 
