from tkinter import *
import sqlite3
from datetime import datetime

class Application():
    root = Tk()
    mode = 1                                                 
    primary = ['#d6dbce','#40676e']
    primaryfg = ['#202d2e','#b0e1eb']
    secondary = ['#69878a','#113036']
    buttons = ['#88a6a8','#19464f']
    buttonsfg = ['black','white']
    topBarColor = ['#113036','#19464f']
    Frames = [0]
    eqMode = -1

    def __init__(self):

        conn = sqlite3.connect('calculator.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS calculations (
                            id INTEGER PRIMARY KEY,
                            timestamp DATETIME,
                            calculation TEXT
                        )''')

        conn.commit()
        conn.close()
        self.HomeFn()

    # Event Bindings for entering leaving buttons
    #------------------------------------------------

    def enterEvent(self, e):
        e.widget.config(cursor='hand2', bg=self.secondary[self.mode])
        pass

    def leaveEvent(self, e):
        e.widget.config(cursor='arrow', bg=self.buttons[self.mode], fg=self.buttonsfg[self.mode])
        pass

    def ButtonEnt(self,e):
        e.widget.config(cursor='hand2')
        pass

    def ButtonLeave(self,e):
        e.widget.config(cursor='arrow')
        pass

    
    def HomeFn(self):
        root = self.root
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()

        root.geometry('900x600+220+50')
        root.state('zoomed')
        root.title('Simulator')

        topBar = Frame(root, width=self.width, height=50, bg=self.topBarColor[self.mode])
        topBar.pack()
        topBar.pack_propagate(False) 
        
        Label(topBar, text='Calculator', font='Arial 17 bold', bg=self.topBarColor[self.mode], fg='white').place(x=self.width/2-60, y=10)
        for i in range(1):
            frame = Frame(root, height=self.height, width=self.width, bg=self.primary[self.mode])
            frame.place(x=0, y=50)
            self.Frames[i] = frame
        
        self.mainframe()
        
        pass
    
    
    def updateRightFrame(self):
        frame = self.rightFrame
        
        for widget in frame.winfo_children():
            widget.destroy()
            
        conn = sqlite3.connect('calculator.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM calculations;")
        calculations = cursor.fetchall()
        conn.close()
        calculations.reverse()
        
        for calculation in calculations:
            Label(frame, text=f'{calculation[2]}', font='Arial 15', bg=self.secondary[self.mode], fg=self.primaryfg[self.mode]).pack()
            Label(frame, text=f'{calculation[1].split(".")[0]}', font='Arial 10', bg=self.secondary[self.mode], fg=self.primaryfg[self.mode]).pack(pady=(0,10))
            
            
    def mainframe(self):
        master = self.Frames[0]
        self.Frames[0].tkraise()
        
        leftFrame = Frame(master, width=3*self.width/4, height=self.height, bg=self.primary[self.mode])
        leftFrame.pack(side=LEFT)
        leftFrame.pack_propagate(False)
        
        self.rightFrame = Frame(master, width=self.width/4, height=self.height, bg=self.secondary[self.mode])
        self.rightFrame.pack(side=RIGHT)
        self.rightFrame.pack_propagate(False)
        
        self.updateRightFrame()
        
        frame = Frame(leftFrame, width=3*self.width/4, height=80, bg=self.primary[self.mode])
        frame.pack()
        frame.pack_propagate(False)
        
        Entry(frame, width=42, font='Arial 30',relief='flat').place(x=12, y=12)
        
        self.entry = Entry(frame, width=47, font='Arial 26',relief='flat')
        self.entry.place(x=15, y=14)
        
        
        BUTTONS = [
            ['%','C','DEL','/'],
            ['7','8','9','+'],
            ['4','5','6','-'],
            ['1','2','3','*'],
            ['.','0','^','=']
        ]
        
        frame = Frame(leftFrame, width=3*self.width/4, height=3*self.height/4, bg=self.primary[self.mode])
        frame.pack()
        frame.pack_propagate(False)
        
        for i in range(5):
            for j in range(4):
                button = Button(frame, text=BUTTONS[i][j], font='Arial 20', width=14, height=3, relief='flat', bg=self.buttons[self.mode], fg=self.buttonsfg[self.mode])
                button.place(x=15+j*230, y=i*110)
                button.bind('<Enter>', self.enterEvent)
                button.bind('<Leave>', self.leaveEvent)
                button.bind('<Button-1>', self.ButtonClick)


    def ButtonClick(self,e):
        text = e.widget.cget('text')
        
        if text in ['0','1','2','3','4','5','6','7','8','9','.', '%', '^', '+', '-', '*', '/']:
            self.entry.insert(END, text)
        elif text == 'C':
            self.entry.delete(0, END)
        elif text == 'DEL':
            if str(self.entry.get()) == 'Syntax Error' or str(self.entry.get()) == 'Math Error':
                self.entry.delete(0, END)
            self.entry.delete(len(self.entry.get())-1)
        elif text == '=':
            answer = self.evaluate(self.entry.get())
            if answer != 'Syntax Error' and answer != 'Math Error':
                self.saveCalculation(f'{self.entry.get()} = {answer}')
            self.updateRightFrame()
            self.entry.delete(0, END)
            self.entry.insert(END, answer)
        

    def evaluate(self, text):
        try:
            text = text.replace('^', '**')
            return str(eval(text))
        except ZeroDivisionError as e:
            return "Math Error"
        except SyntaxError as e:
            return "Syntax Error"
    
    def saveCalculation(self, text):
        conn = sqlite3.connect('calculator.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO calculations (timestamp, calculation) VALUES (?, ?)', (datetime.now(), text))
        conn.commit()
        conn.close()
    
app = Application()
app.root.mainloop()
