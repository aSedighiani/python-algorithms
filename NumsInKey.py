l = ['a','c','e','g','n','e','c','c','n','e']
dict = {}
for item in l:
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1
print(dict)