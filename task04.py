orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]
filterlangan = []

for raqam, ism in orders:
    if raqam % 2 == 0:
        filterlangan.append((raqam, ism))

print(filterlangan)