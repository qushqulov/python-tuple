words = ("apple", "banana", "strawberry", "kiwi")
uzun_soz = ""

for soz in words:
    if len(soz) > len(uzun_soz):
        uzun_soz = soz

print(uzun_soz)   