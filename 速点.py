import win32api
import win32con
import time
def sudian():
	while True:

		if win32api.GetAsyncKeyState(0x02)&0x8000 == 32768:
			print(1)
			flag=1
			while flag == 1:
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
				print(win32api.GetCursorPos())
				print('速点一次')
				time.sleep(0.065)
				if win32api.GetAsyncKeyState(0x02)&0x8000 != 32768:
					flag=0

		
		else:
			pass
sudian()
