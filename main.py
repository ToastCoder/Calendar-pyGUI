import win10toast
import time
from tkinter import *

#Window Class
class Window:
    def __init__(self,win):
# Real time clock
        self.tstamp = Label(win)
        self.tstamp.place(x=90,y=26)
        self.rt_val = time.strftime('%H:%M:%S %p')
        self.tstamp.config(text = self.rt_val)
        self.tstamp.after(1000,time)
# Heading of the code       
        self.head= Label(win, text="Create a simple reminder",width=20,font=('bold',20))
        self.head.place(x=90,y=53)
# Input fields
        self.cmd_title = Label(win, text="Remind about?",width=20,font=('bold',10))
        self.cmd_title.place(x=80,y=130)
        self.cmd = Entry(win)
        self.cmd.place(x=240,y=130)
        self.dl_title = Label(win,text="In how many minutes?",width=20,font=('bold',10))
        self.dl_title.place(x=80,y=160)
        self.dl = Entry(win)
        self.dl.place(x=240,y=160)
        self.bt = Button(win, text='Submit',width=20,bg='brown',fg='white',command=self.getData)
#Function to store the data
    def getData(self):
        self.cmd_f = str(self.cmd.get())
        self.dl_f = int(self.dl.get())
    def return_cmd(self):
        return self.cmd_f
    def return_dl(self):
        return self.dl_f
# MAIN FUNCTION
root = Tk()
newwin=Window(root)
root.geometry('500x500')
root.title("Reminder")
root.iconphoto(False,PhotoImage(file='icon.png'))
command = newwin.return_cmd()
deadline = newwin.return_dl()

deadline = deadline * 60
time.sleep(deadline)
notify = win10toast.ToastNotifier()
notify.show_toast("Reminder",command)
root.mainloop()
