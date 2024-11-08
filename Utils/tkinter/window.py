# import tkinter

# window = tkinter.Tk()
# window.geometry("500x300")

# def click():
#     print("Fazer login")

# text = tkinter.Label(window, text="Fazer login")
# text.pack(padx=10, pady=10)

# button = tkinter.Button(window, text="Login", command=click)
# button.pack(padx=10, pady=10)

# window.mainloop()

import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

window = customtkinter.CTk()
window.geometry("500x300")

def click():
    print(email.get())
    print(password.get())

text = customtkinter.CTkLabel(window, text="Entrar")
text.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(window, placeholder_text="Digite seu nome")
email.pack(padx=10, pady=10)

password = customtkinter.CTkEntry(window, placeholder_text="Digite sua senha", show="*")
password.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(window, text="Lembrar login")
checkbox.pack(padx=10, pady=10)

button = customtkinter.CTkButton(window, text="Fazer login", command=click)
button.pack(padx=10, pady=10)

window.mainloop()