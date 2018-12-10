# KeyLogger
A simple python keylogger which uploads the log file of your keyboard to server.

It implements pyHook, pythoncom, requests modules to do the job.

Global keyboard events are tracked and stored in a tmp file in the Windows temp dir.
Later on, a separate thread uploads that file to the server two times in every one min.
