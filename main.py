import win10toast
import time
from tkinter import *

message = 0
deadline = 0

def makeVariables():
    global message
    message = val1.get()
    global deadline
    deadline = val2.get()
    print(message,deadline)
    deadline = int(deadline) * 60
    time.sleep(deadline)
    notify = win10toast.ToastNotifier()
    notify.show_toast("Reminder",message)
root = Tk()
root.title("Reminder")
txt1 = Label(root,text = "Create a simple reminder\nKeep this application open inorder not to terminate the app.").pack()
txt2 = Label(root,text = "Remind about?").pack()
val1 = Entry(root)
val1.pack()
txt3 = Label(root,text = "In how many minutes?").pack()
val2 = Entry(root)
val2.pack()
key = Button(root,text = "Set Reminder",width = 20,command = makeVariables)
key.pack()

root.mainloop()
