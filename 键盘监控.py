import threading
from pynput.mouse import Button, Listener, Controller
from pynput import keyboard
import time


def keyboard_release(key):
	print(key)
	print(time.asctime(time.localtime(time.time())))

def keyboardListener():
    with keyboard.Listener(on_release=keyboard_release) as listener:
        listener.join()

keyboardListener()