from conect_orm import Base, engine, session
from User import User
from Post import Post

# Criar as tabelas
Base.metadata.create_all(engine)


# Função para exibir o menu de opções
def show_menu():
    print("Menu de Opções:")
    print("1 - Adicionar Usuário")
    print("2 - Adicionar Post")
    print("3 - Consultar Usuário e seus Posts")
    print("4 - Sair")


# Função para adicionar usuário
def add_user():
    print("Adicionar novo usuário")
    name = input("Nome: ")
    email = input("Email: ")
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    print("Usuário adicionado com sucesso")


# Função para adicionar um novo post
def add_post():
    print("Adicionar novo post:")
    title = input("Título: ")
    content = input("Conteúdo: ")
    author_id = input("Id do Autor: ")
    user = session.query(User).filter_by(id=author_id).first()
    if user:
        post = Post(title=title, content=content, author=user)
        session.add(post)
        session.commit()
        print("Post adicionado com sucesso")
    else:
        print("Usuário não encontrado")


def query_users_posts():
    users = session.query(User).join(User.posts).order_by(User.name).all()
    for user in users:
        print(f"User: {user.name}; Email: {user.email}")
        for post in user.posts:
            print(f"Post: {post.title}; Conteúdo: {post.content}")
