from PIL import Image
import os

list_files = os.listdir("images")

for file in list_files:
    # Abrir o arquivo
    image = Image.open(f"images/{file}")


    # Salvar o arquivo com outro formato
    image.save(f"dist/{file.replace('webp', 'jpg')}")