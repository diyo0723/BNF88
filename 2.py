import os
os.system("clear")

def min (lst: list):
    sonlar = sorted(lst)[2]
    print(sonlar)

lst = [5,12,32,12,24,7,6,1,8,7,9,3,2,4,6,7,1,3]
min(lst)