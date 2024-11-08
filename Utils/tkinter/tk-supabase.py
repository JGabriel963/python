from supabase import create_client, Client
import customtkinter

SUPABASE_URL='https://fvotvtbkjkviwxfsjhrt.supabase.co'
SUPABASE_KEY='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ2b3R2dGJramt2aXd4ZnNqaHJ0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzEwMjkzOTMsImV4cCI6MjA0NjYwNTM5M30.I-ekazJ4-A4H-32pJvRW4ge4hkWag8sZ7c1Aij5Qky8'

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

print(supabase)

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

window = customtkinter.CTk()
window.geometry("500x300")

def click():
    response = (
        supabase.table('users')
        .insert({"name": email.get(), "email": email.get(), "password": password.get()})
        .execute()
    )

    print("Tudo certo!")

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