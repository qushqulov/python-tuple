students = [("Ali", ["Fizika", "Matematika"]), ("Laylo", ["Ingliz tili"]), ("Jasur", ["Matematika", "Informatika"])]
count = 0
for talaba, subjects in students:
    if "Matematika" in subjects:
        count += 1

print(f"{count} talaba Matematika fanini tanlagan.") 