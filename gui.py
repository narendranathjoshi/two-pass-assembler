from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as box

fileptr = [False, 0]

class MainWIndow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='#eed')
        self.parent = parent
        self.initUI()
        self.quitButton()
        self.fileButton()
        
    def initUI(self):
        self.parent.title('Two-Pass Assembler')
        self.pack(fill=BOTH, expand=1)
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        self.parent.geometry('500x500+%d+%d' % ((sw - 500)/2, (sh - 500)/2))
        
    def quitButton(self):
        quitButton = Button(self, text = "Quit", command = self.quit)
        quitButton.place(relx = 0.8, rely = 0.8, relwidth = 0.1)
        
    def fileButton(self):
        fileButton = Button(self, text = "Browse", command = self.onOpen)
        fileButton.place(relx = 0.68, rely = 0.8, relwidth = 0.1)
        
    def onOpen(self):      
        filename = filedialog.askopenfilename()
        if filename is '':
            box.showinfo("Info", "You did not select a file.")
        else:
            global fileptr
            fileptr[0] = True
            fileptr[1] = filename
            f = open(fileptr[1], 'r')
            text = f.read()
            text = text.split('\n')
            #for i in text: #testing #success
                #print(i)       #testing
        
def main():
    root = Tk()
    app = MainWIndow(root)
    root.mainloop()
    
#main() #success #called in _init__.py