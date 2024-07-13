import os
os.system("clear")

def max (lst: list):
    son = sorted(lst)[-2]
    print(son)

lst = [5,7,6,8,7,9,3,2,4,6,7,1,3,12,23,21]
max(lst)
