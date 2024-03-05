from Blog.Blog import show_menu, add_post, add_user, query_users_posts

while True:
    show_menu()
    option: int = int(input(">_"))

    if option == 1:
        add_user()
    elif option == 2:
        add_post()
    elif option == 3:
        query_users_posts()
    elif option == 4:
        print("Thanks :)")
        break
    else:
        print("Informe um opção válida!")
