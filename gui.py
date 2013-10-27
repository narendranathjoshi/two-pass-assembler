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
        self.inputText()
        self.outputText()
        self.labels()
        
    def initUI(self):
        self.parent.title('Two-Pass Assembler')
        self.pack(fill=BOTH, expand=1)
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        self.parent.geometry('500x500+%d+%d' % ((sw - 500)/2, (sh - 500)/2))
        
    def quitButton(self):
        quitButton = Button(self, text = "Quit", command = self.quit)
        quitButton.place(relx = 0.8, rely = 0.9, relwidth = 0.1)
        
    def genButton(self):
        genButton = Button(self, text = "Assemble", command = self.assemble)
        genButton.place(relx = 0.32, rely = 0.9, relwidth = 0.2)
        
    def fileButton(self):
        fileButton = Button(self, text = "Select Input", command = self.onOpen)
        fileButton.place(relx = 0.1, rely = 0.9, relwidth = 0.2)
        
    def inputText(self, textParam=''):
        self.inputText = Text(self)
        self.inputText.place(relx = 0.1, rely = 0.07, relwidth = 0.8, relheight = 0.35)
        #self.inputText.insert(chars = textParam, index = 0)
        
    def labels(self):
        l1 = Label(self, text = "Input Assembly Source", background='#eed')
        l2 = Label(self, text = "Output Machine Code", background='#eed')
        l1.place(relx = 0.35, rely = 0.02, relwidth = 0.3)
        l2.place(relx = 0.35, rely = 0.45, relwidth = 0.3)
        
    def outputText(self, textParam=''):
        self.outputText = Text(self)
        self.outputText.place(relx = 0.1, rely = 0.5, relwidth = 0.8, relheight = 0.35)
        
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
            #self.inputText(text)
            text = text.split('\n')
            self.genButton()
            #for i in text: #testing #success
                #print(i)       #testing
        
    def assemble(self):
        #call to assembly code module
        print("Call") #testing
    
def main():
    root = Tk()
    app = MainWIndow(root)
    root.mainloop()
    
#main() #success #called in _init__.py