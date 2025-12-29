people = [("Ali", 24), ("Laylo", 30), ("Jasur", 19)]

oldest = people[0]
for person in people:

    if person[1] > oldest[1]:
        oldest = person
name, age = oldest
print(f"{name} — {age} yosh")
