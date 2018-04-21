import pyautogui

with open('log.txt', 'w') as f:
    for x in str(pyautogui.KEYBOARD_KEYS).split(','):
        f.write(x + '\r')

f.close()
