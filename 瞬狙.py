from keywinio import *
import time
import ctypes
import pywinio
import win32api
import win32con

def 瞬狙():
	while True:
		#检测鼠标中键是否点击
		if win32api.GetAsyncKeyState(0x04)&0x8000 == 32768:
			flag=1
			if flag == 1:
				print(win32api.GetCursorPos())
				print('我瞬!')
				
				win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
				win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
				time.sleep(0.05)#左右按键切换时间
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
				key_press(0x05)#4
				time.sleep(0.14)#切换另一个枪停留时间
				key_press(0x02)#1
				time.sleep(1.4)#缓冲
				if win32api.GetAsyncKeyState(0x04)&0x8000 != 32768:
					flag=0
					print(flag)

		
		else:
			pass
瞬狙()