""" 
1 - option w - write
2 - option a - append
3 - option r - read
"""
with open("names.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())
