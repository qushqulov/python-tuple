emails = (("Ali", "ali@gmail.com"), ("Vali", "vali@yandex.ru"), ("Sami", "sami@mail.ru"))
domenlar = []

for ism, email in emails:
    qismlar = email.split('@') 
    domen = qismlar[1]         
    domenlar.append(domen)

print(domenlar)  