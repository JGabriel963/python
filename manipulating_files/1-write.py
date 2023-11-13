""" 
1 - option w - write
2 - option a - append
3 - option r - read
"""

# Choose 1
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()


def menu():
    print("Enter your choise")
    print("1 - Add new Linguage")
    print("2 - Add framework")
    print("3 - Sair")


def write_file(value, type):
    with open("names.txt", "a") as file:
        file.write(f"{type}={value}\n")


# Choose 2
while True:
    menu()
    choise = input("> ")

    if choise == "1":
        language = input("Enter any language: ")
        write_file(language, "language")
    elif choise == "2":
        framework = input("Enter any framework> ")
        write_file(framework, "framework")
    elif choise == "3":
        print("The end!")
        break
    else:
        print("Opção inválida!")
