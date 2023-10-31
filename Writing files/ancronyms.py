look_up = input('Which acronym do you want to lookup: ')

with open('./files/acronyms.txt') as file:
    for line in file:
        if look_up in line:
            print(line)
            exit(0)

    print(f'Acronym {look_up} not found in file: {file.name}')