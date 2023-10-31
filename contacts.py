contacts = {
    'number': 4,
    'students': 
        [
        {'name': 'Matthias Müller', 'email': 'matthias@example.com'},
        {'name': 'Harry Potter', 'email': 'harry@example.com'},
        {'name': 'Matze Fischer', 'email': 'fischer@example.com'},
        {'name': 'Günther Müller', 'email': 'günther@example.com'}
        ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])
