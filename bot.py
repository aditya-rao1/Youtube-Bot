import pyautogui
import time


# Goal - Create a script that can automate opening up a youtube video related to a certain topic i want.
time.sleep(3)
print(pyautogui.position())

#This function will open up Youtube. 
def openYoutube():
    pyautogui.leftClick(214, 1050)
    time.sleep(2)
    pyautogui.leftClick(287, 64)
    pyautogui.hotkey('ctrl', 't')
    pyautogui.press('y')
    pyautogui.press('o')
    pyautogui.press('u')
    pyautogui.press('t')
    pyautogui.press('u')
    pyautogui.press('b')
    pyautogui.press('e')
    pyautogui.press('.')
    pyautogui.press('c')
    pyautogui.press('o')
    pyautogui.press('m')
    pyautogui.press('enter')

#This function is responsible for opening either videos or shorts.
def consumeContent():
    userDesire = input("What do you want to watch on Youtube?")
    i = 0
    if userDesire == "videos" or " videos":
        openYoutube()
        time.sleep(4)
        pyautogui.click(133, 664)
        time.sleep(3)
        pyautogui.click(1297, 404)
        #GO TO WATCH LATER VIDEOS
    if userDesire == " shorts" or "shorts":
        range = input("How many?")
        openYoutube()
        time.sleep(4)
        pyautogui.click(124, 338)
        pyautogui.moveTo(500, 500)
        while i < int(range):
            time.sleep(10)
            pyautogui.press('down')
            i += 1



consumeContent()



