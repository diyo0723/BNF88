import os
os.system("clear")  
def process_dict(Aa): 
    return {v: k for k, v in Aa.items()}
Aa = {'a': 1, 'b': 2, 'c': 3}
main = process_dict(Aa)
print(main)
