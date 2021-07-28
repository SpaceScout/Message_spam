import pyautogui, keyboard
key1 = "1"
key2 = "2"
while True:
    if keyboard.is_pressed(key1):
        f = open("bee_script", 'r')
        for word in f:
            pyautogui.typewrite(word)
            pyautogui.press("enter")
            if keyboard.is_pressed(key2):
                break
