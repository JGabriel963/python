import pyautogui
import time

print(pyautogui.size())

print(pyautogui.position())
time.sleep(1.5)

pyautogui.moveTo(712, 46)
time.sleep(1.5)
pyautogui.click()

pyautogui.moveTo(1543, 299)
pyautogui.scroll(-900)