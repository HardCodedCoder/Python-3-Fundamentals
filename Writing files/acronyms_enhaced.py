def find_acronym() -> str:
    acronym = input("Which acronym are you searching for? ")
    try:
        with open('./files/acronyms.txt') as file:
            for line in file:
                if acronym in line:
                    return line

        raise IndexError("File end reached, acronym not found")
    except FileNotFoundError:
        print("The file acronyms.txt does not exist!")


def add_acronym() -> None:
    acronym = input('What acronym do you want to add: ')
    definition = input('What is the definition of the acronym: ')
    with open('./files/acronyms.txt', 'a') as file:
        file.write(f'\n{acronym} - {definition}\n')


def main() -> int:
    choice = input('Do you want to find(F) or Add(A) an acronym? ')
    if choice == 'F':
        try:
            print(find_acronym())
        except IndexError:
            print('Acronym not found!')
    elif choice == 'A':
        add_acronym()


main()
