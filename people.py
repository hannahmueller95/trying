with open("people.csv", "r") as people:
    for line in people:
        line = line.strip()
        if line == '':
            continue

        data = line.split(",")
        name, age, gender = data

        print(name, 'is', age, 'years old and', gender)

