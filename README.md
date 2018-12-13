# KeyLogger
A simple python keylogger which uploads the log file of your keyboard to server.

It implements pyHook, pythoncom, requests modules to do the job.

Global keyboard, mouse events are tracked and stored in a tmp file in the Windows temp dir.
Later on, a separate thread uploads that file to the server two times in every one min.

There is a separe thread, which is constantly checking a file in the server.

If there is a remote command in server to change the data to 'L', that thread will immediately lock the computer.

If the command is 'S' in the server, then that thread will shutdown the computer remotely.
