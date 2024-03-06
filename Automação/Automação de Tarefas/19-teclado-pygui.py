import pyautogui
import time

time.sleep(1)

with pyautogui.hold('win'):
    pyautogui.press('right')

time.sleep(2)

pyautogui.click()
time.sleep(2)

