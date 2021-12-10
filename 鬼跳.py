from keywinio import *
import time
import win32api

def 鬼跳():
	while True:
		#检测鼠标中键是否点击
		if win32api.GetAsyncKeyState(0x04)&0x8000 == 32768:
			flag=1
			if flag == 1:
				print(win32api.GetCursorPos())
				print('我跳!')
				key_down(0x39)
				time.sleep(0.01)
				key_up(0x39)
				time.sleep(0.01)
				key_down(0x2a)
				if win32api.GetAsyncKeyState(0x04)&0x8000 != 32768:
					flag=0
					print(flag)
					key_up(0x2a)

		
		else:
			pass
鬼跳()