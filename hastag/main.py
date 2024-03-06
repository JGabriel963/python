# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer login

# Size(width=1920, height=1080)
import pyautogui
import time
pyautogui.PAUSE = 1

# pyautogui.PAUSE = 5
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.write('google-chrome')
pyautogui.press('enter')


link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press('enter')

# Passo 3 Importar a base de dados
# Passo 4: Cadastrar 1 produtor