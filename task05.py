numbers = (3, 6, 7, 8, 10, 11)
juftlar = []

for son in numbers:
    if son % 2 == 0:
        juftlar.append(son)

print(tuple(juftlar))  