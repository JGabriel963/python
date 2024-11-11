from rembg import remove
from PIL import Image, UnidentifiedImageError
import customtkinter
import os
import time

window = customtkinter.CTk()
window.geometry('800x300')
window.title("Removedor de Fundo de Imagem")

def remove_bg():
    filte_path = input_url.get().strip().replace("'", "").replace('"', "")

    if not os.path.isfile(filte_path):
        status_label.configure(text="Arquivo não encontrado. Verifique o caminho." )
        return
    
    try:
        image = Image.open(filte_path)
        output = remove(image)

        base_name = os.path.splitext(os.path.basename(filte_path))[0]
        output_file = f"{base_name}_no_bg_{int(time.time())}.png"

        output.save(output_file)
        status_label.configure(text=f"Fundo removido com sucesso! Imagem salva como '{output_file}'")
    except UnidentifiedImageError:
        status_label.configure(text="Erro: o arquivo não é uma imagem válida")
    except Exception as e:
        status_label.configure(text="Erro ao processar a imagem: {e}")

# Elementos da interface
text = customtkinter.CTkLabel(window, text="Remova o fundo de suas imagens")
text.pack(padx=10, pady=10)

input_url = customtkinter.CTkEntry(window, placeholder_text="Url do arquivo local")
input_url.pack(padx=10, pady=10)

button = customtkinter.CTkButton(window, text="Remover fundo", command=remove_bg)
button.pack(padx=10, pady=10)

status_label = customtkinter.CTkLabel(window, text="")
status_label.pack(padx=10, pady=10)

# Iniciar janela
window.mainloop()