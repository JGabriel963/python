import webbrowser
import os

done = False

while not done:
    print("Para onde você quer ir?")
    print("1 - GitHub")
    print("2 - MNShopify")
    print("3 - Shopify")
    print("4 - Sair")

    choice = input("> ")

    if choice == "1":
        webbrowser.open("https://github.com/JGabriel963?tab=repositories")
    elif choice == "2":
        webbrowser.open("https://mnshopping.com.br")
    elif choice == "3":
        webbrowser.open("https://admin.shopify.com/store/b512e8-4")
    elif choice == "4":
        print("The End")
        break
    else:
        print("Opção inválida")

    os.system("clear")
