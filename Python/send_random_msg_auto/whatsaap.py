import pyautogui
import time
import random

time.sleep(1)
count = 0
msglst = ["hey ullu", "abey lukhe", "dingdong khi ka"]

while count <= 150:
    msg = random.choice(msglst)
    pyautogui.typewrite(msg)
    pyautogui.press('enter')
    count += 1
    time.sleep(0.1) 