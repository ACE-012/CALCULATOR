from tkinter import *
import threading
from tkinter import font
import calculator
class GUI(threading.Thread):
    def __init__(self):
        super().__init__()
        self.root_instance = Tk()
        self.root_instance.geometry("0x0")
        self.root_instance.overrideredirect(1)
        self.mainwindow = None
        self.questionbar=None
        self.answerbar=None
        self.eqvar=StringVar()
        self.ansvar=StringVar()
        self.eqvar.trace("w", lambda name, index, mode,
                             sv=self.eqvar: self._eq(sv.get()))
        self._mainwindow()
        self.equals=True
        self.root_instance.mainloop()
    def _eq(self,eq:str):
        for e in eq:
            if e.isalpha():
                eq=eq.replace(e,'')
                self.eqvar.set(eq)
            elif e.isspace():
                eq=eq.replace(e,'')
                self.eqvar.set(eq)
    def _mainwindow(self):
        self.mainwindow = Toplevel(self.root_instance)
        self.mainwindow.wm_title("CALCULATOR")
        self.mainwindow.wm_maxsize(520,480)
        self.mainwindow.protocol("WM_DELETE_WINDOW", self.close_window)
        self.questionbar=Entry(self.mainwindow,textvariable=self.eqvar,justify='right',width=50)
        self.questionbar.pack()
        self.answerbar=Entry(self.mainwindow,textvariable=self.ansvar,justify='right',width=50)
        self.answerbar.pack()
        self.answerbar.configure(state='disabled')
        self._buttons()
    def _buttons(self):
        self.buttons_Frame = Frame(self.mainwindow)
        myfont=font.Font(family='Helvetica', size=30)
        i = 0
        j = 0
        for k in range(12):
            try:
                text=k+1 if k+1<=9 else "C" if k+1==10 else 0 if k+1==11 else '.'
                Button(
                    self.buttons_Frame,
                    text=text,
                    font= myfont,
                    height=1, width=3,
                    bd='5',
                    command=lambda c=text: self._button_command(c)).grid(row=j, column=i)
            except Exception as e:
                print(e)
                pass
            if i < 2:
                i += 1
            else:
                i = 0
                j += 1
            if j>4:
                break
        self.buttons_Frame.pack(padx=5,pady=10,side=LEFT)
        self.buttons_Frame_operators_right=Frame(self.mainwindow)
        for i in range(4):
            text="+"if i==0 else "-" if i==1 else "/" if i==2 else "*"
            Button(self.buttons_Frame_operators_right,
            text=text,
                    font= myfont,
                    height=1, width=3,
                    bd='5',
                    command=lambda c=text: self._button_command(c)).grid(row=i,column=0)
        Button(self.buttons_Frame_operators_right,
            text="=",
                    font= myfont,
                    height=1, width=3,
                    bd='5',
                    command=lambda c="=": self._button_command(c)).grid(row=0,column=1)
        Button(self.buttons_Frame_operators_right,
            text="(",
                    font= myfont,
                    height=1, width=3,
                    bd='5',
                    command=lambda c="(": self._button_command(c)).grid(row=1,column=1)
        Button(self.buttons_Frame_operators_right,
            text=")",
                    font= myfont,
                    height=1, width=3,
                    bd='5',
                    command=lambda c=")": self._button_command(c)).grid(row=2,column=1)
        self.buttons_Frame_operators_right.pack(padx=5,pady=10,side=LEFT)
    def _button_command(self,val):
        if val=="C":
            self.eqvar.set(self.eqvar.get()[:-1])
        elif val=="=":
            self.ansvar.set(calculator.calculator(self.eqvar.get()).run())
            # print(self.ansvar.get())
            self.equals=True
        else:
            if self.equals==True:
                self.eqvar.set("")
            self.eqvar.set(self.eqvar.get()+str(val))
            self.equals=False
    def close_window(self):
        self.root_instance.quit()

g = GUI()
g.start()
