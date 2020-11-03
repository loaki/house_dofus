import time
import sys
import pyautogui
import re
#import msvcrt
import keyboard
#import winsound
from playsound import playsound

def get_pos(name):
    pos = input('point the '+str(name+1)+' button and press enter')
    return pyautogui.position()

def init_data(d):
    d.max = 3
    d.sleep = 0.1
    for i in range(0, d.max):
        d.button[i] = pos()
        d.button[i] = get_pos(i)
    pyautogui.moveTo(d.button[1].x, d.button[1].y)
    im = pyautogui.screenshot(region=(d.button[2].x, d.button[2].y, 30, 30))
    im.save('pro.png')

def action(d):
	for i in range(0, d.max - 1):
		pyautogui.moveTo(d.button[i].x, d.button[i].y)
		time.sleep(d.sleep)
	if pyautogui.locateOnScreen('pro.png') == None:
		print('lol')
		playsound('oui.mp3')
		return 1
	return 0

class pos():
    x = 0
    y = 0

class data():
    max = 0
    sleep = 0
    button = {}

if __name__ == "__main__":
    d = data()
    init_data(d)
    print('\npress esc to quit')
    ex = 0
    while ex != 1:
        ex = action(d)
        ##if keyboard.is_pressed('escape') == True:
     #       print('exiting...')
     #       ex = 1
