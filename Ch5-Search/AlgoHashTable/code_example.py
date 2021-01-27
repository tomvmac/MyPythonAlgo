records = [ ('tom@example.com','Hello world'),
            ('kobe@example.com','Hello 24'),
            ('lebron@example.com','Hello King')
           ]

for index, record in enumerate(records):
    key, value = record
    if key == "kobe@example.com":
        break
    print(index, key, value)

print(records[index])