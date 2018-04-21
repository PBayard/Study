import pyautogui

with open('log.txt', 'w') as f:
    f.write('KEYBOARD_KEYS' + '\r')
    f.write('**************' + '\r')
    for x in str(pyautogui.KEYBOARD_KEYS).split(','):
        f.write(x + '\r')
    f.write('\r')


with open('log.txt', 'a') as f:
    f.write('print_function' + '\r')
    f.write('**************' + '\r')
    for x in str(pyautogui.print_function).split(','):
        f.write(x + '\r')