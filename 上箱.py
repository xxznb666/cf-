from keywinio import *
import time
import pywinio
import win32api

def 上箱():
	while True:
		#检测鼠标中键是否点击
		if win32api.GetAsyncKeyState(0x04)&0x8000 == 32768:
			flag=1
			if flag == 1:
				print(win32api.GetCursorPos())
				print('我跳!')
				key_down(0x11)#按住w
				time.sleep(0.05)
				key_down(0x39)#按跳
				time.sleep(0.16)
				key_up(0x39)
				time.sleep(0.48)
				key_down(0x39)
				time.sleep(0.12)
				key_up(0x39)#按跳
				time.sleep(0.1)
				key_down(0x2a)
				time.sleep(0.13)
				key_up(0x2a)
				time.sleep(0.26)
				key_up(0x11)
				time.sleep(1)
				if win32api.GetAsyncKeyState(0x04)&0x8000 != 32768:
					flag=0
					print(flag)

		
		else:
			pass
上箱()