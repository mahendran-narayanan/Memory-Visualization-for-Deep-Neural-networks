#start
import os
import time
import psutil
import signal
from multiprocessing import Process
import sys

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
import numpy as np
import pandas as pd

from tkinter import messagebox
from time import gmtime, strftime
from tkinter import *



def _exit():
	root.quit()
	root.destroy()

def _submit():
	pass

rocket = 0
maxint = 9999


def func1():
    global rocket
    count=0
    print ('start func1')
    if not os.path.exists('EAHPdata'):
        os.makedirs('EAHPdata')
    #os.system('mkdir EAHPdata')
    print("Tool Initialized!...\n")
    print("Scanning Mem started!...")
    interrupted=False
    while True:
        with open("EAHPdata/dataset"+str(count)+".csv","a") as fw:
            fw.write(
                str(psutil.virtual_memory().total)+","+
                str(psutil.virtual_memory().available)+","+
                str(psutil.virtual_memory().percent)+","+
                str(psutil.virtual_memory().used)+","+
                str(psutil.virtual_memory().active)+"\n")
            time.sleep(0.2)
        if interrupted:
            break
    fw.close()
    count+=1

rocket = 0
maxint = 9999

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
    def submit(self):
        d1 = self.e1.get()
        d2 = self.e2.get()
        d3 = self.e3.get()
        d4 = self.e4.get()
        d5 = self.e5.get()
        d6 = self.e6.get()
        d7 = self.e7.get()
        d8 = self.e8.get()
        d9 = self.e9.get()
        d10 = self.e10.get()
        d11 = self.e11.get()
        d12 = self.e12.get()
        currtime = strftime("%Y_%m_%d_%H%M%S", gmtime())
        with open("datasets/"+str(currtime)+".csv","a") as f:
            f.write("d2,"+d2+"\n")
            f.write("d3,"+d3+"\n")
            f.write("d4,"+d4+"\n")
            f.write("d5,"+d5+"\n")
            f.write("d6,"+d6+"\n")
            f.write("d7,"+d7+"\n")
            f.write("d8,"+d8+"\n")
            f.write("d9,"+d9+"\n")
            f.write("d10,"+d10+"\n")
            f.write("d11,"+d11+"\n")
            f.write("d12,"+d12+"\n")
        gotdata= "Submitted!..."
        self.ldata.configure(text=gotdata)
        p1.pack()# Problem here ref : https://stackoverflow.com/questions/48480974/how-to-implement-lift-method
        p2.pack()
        p3.lift()
        #tk.Button(buttonframe, text="Graph", command=p3.lift)
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(background="#ffe5b4")
        l1 = tk.Label(self,text="Machine Type",background="#ffe5b4")
        self.e1 = tk.Entry(self,bd=1)
        l2 = tk.Label(self,text="Learning rate",background="#ffe5b4")
        self.e2 = tk.Entry(self,bd=1)
        l3 = tk.Label(self,text="Batch Size",background="#ffe5b4")
        self.e3 = tk.Entry(self,bd=1)
        l4 = tk.Label(self,text="Epochs",background="#ffe5b4")
        self.e4 = tk.Entry(self,bd=1)
        l5 = tk.Label(self,text="nbClasses",background="#ffe5b4")
        self.e5 = tk.Entry(self,bd=1)
        l6 = tk.Label(self,text="No. of Layers",background="#ffe5b4")
        self.e6 = tk.Entry(self,bd=1)
        l7 = tk.Label(self,text="Train Loss",background="#ffe5b4")
        self.e7 = tk.Entry(self,bd=1)
        l8 = tk.Label(self,text="Train Accuracy",background="#ffe5b4")
        self.e8 = tk.Entry(self,bd=1)
        l9 = tk.Label(self,text="Test Loss",background="#ffe5b4")
        self.e9 = tk.Entry(self,bd=1)
        l10 = tk.Label(self,text="Test Accuracy",background="#ffe5b4")
        self.e10 = tk.Entry(self,bd=1)
        l11 = tk.Label(self,text="Memory Utilization value",background="#ffe5b4")
        self.e11 = tk.Entry(self,bd=1)
        l12 = tk.Label(self,text="Energy Utilization value",background="#ffe5b4")
        #v = StringVar(self, value='default text')
        self.e12 = tk.Entry(self,bd=1)
        self.e12.insert(0, 'default text')
        self.e12.pack(side="bottom", fill="both", expand=False)
        l12.pack(side="bottom",fill="x",expand=0,ipadx=30, ipady=6)
        self.e11.pack(side="bottom", fill="both", expand=False)
        l11.pack(side="bottom",fill="x",expand=0,ipadx=30, ipady=6)
        self.e10.pack(side="bottom", fill="both", expand=False)
        l10.pack(side="bottom",fill="x",expand=0,ipadx=30, ipady=6)
        self.e9.pack(side="bottom", fill="both", expand=False)
        l9.pack(side="bottom",fill="x",expand=0,ipadx=30, ipady=6)
        self.e8.pack(side="bottom", fill="both", expand=False)
        l8.pack(side="bottom",fill="x",expand=0,ipadx=30, ipady=6)
        self.e7.pack(side="bottom", fill="both", expand=False)
        l7.pack(side="bottom",fill="x",expand=0,ipadx=30, ipady=6)
        self.e6.pack(side="bottom", fill="both", expand=False)
        l6.pack(side="bottom",fill="x",expand=0,ipadx=30, ipady=6)
        self.e5.pack(side="bottom", fill="both", expand=False)
        l5.pack(side="bottom",fill="x",expand=0,ipadx=30, ipady=6)
        self.e4.pack(side="bottom", fill="both", expand=False)
        l4.pack(side="bottom",fill="x",expand=0,ipadx=30, ipady=6)
        self.e3.pack(side="bottom", fill="both", expand=False)
        l3.pack(side="bottom",fill="x",expand=0,ipadx=30, ipady=6)
        self.e2.pack(side="bottom", fill="both", expand=False)
        l2.pack(side="bottom",fill="x",expand=0,ipadx=30, ipady=6)
        self.e1.pack(side="bottom", fill="both", expand=False)
        l1.pack(side="bottom", fill="x", expand=0,ipadx=30, ipady=6)
        self.ldata = tk.Label(self,text="",background="#ffe5b4")
        self.ldata.pack(side="bottom",fill="x",expand=0,ipadx=30,ipady=6)
        submit = tk.Button(master=self,text="Submit",command=self.submit)
        submit.pack(side="bottom",fill="none",expand=False,ipadx=30,ipady=6)

class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        fig = Figure(figsize=(5, 4), dpi=100)
        t = pd.read_csv('EAHPdata/dataset0.csv')
        fig.suptitle('Memory Utilization')
        fig.add_subplot(421).plot(t.iloc[:,1])
        fig.add_subplot(421).set_title("Memory total")
        fig.subplots_adjust(hspace=.2)
        fig.add_subplot(422).plot(t.iloc[:,1])
        fig.add_subplot(422).set_title("Memory available")
        fig.add_subplot(423).plot(t.iloc[:,2])
        fig.add_subplot(423).set_title("Memory percent")
        fig.add_subplot(424).plot(t.iloc[:,3])
        fig.add_subplot(424).set_title("Memory used")
        fig.add_subplot(425).plot(t.iloc[:,4])
        fig.add_subplot(425).set_title("Memory active")
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


class Page3(Page):
    def startrec(self):
        print("Startrec")
        
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        abouttext = "This area contains text of about "
        about = tk.Label(self,text=abouttext,background="#ffe5b4")
        about.pack(side="top",fill="x",expand=0,ipadx=55, ipady=15)
        buttonframe = tk.Frame(self)
        buttonframe.pack(side="top",fill="x",expand=False)
        rec = tk.Button(buttonframe,text="Start",command=self.startrec)
        rec.pack(side="left")


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Input Data", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Graph", command=p2.lift)

        b1.pack(side="left")
        b2.pack(side="left")

        p1.show()



def func2():
    global rocket
    print ('start func2')
    main = MainView(root)
    p1 = Page1()
    p2 = Page2()
    p3 = Page3()
    b1 = tk.Button(root, text="Input Data", command=p1.lift)
    b2 = tk.Button(root, text="Graph", command=p2.lift)
    b3 = tk.Button(root, text="Rec", command=p3.lift)
    main.configure(background="#ffe5b4")
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("520x800")
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
    print ('To stop background measuring. Press CTRL+C')

def func3():
    global rocket
    count=0
    print ('start func1')
    if not os.path.exists('EAHPdata'):
        os.makedirs('EAHPdata')
    #os.system('mkdir EAHPdata')
    print("Scanning Mem started!...")
    print ('To stop background measuring. Press CTRL+C')

def rec():
    pr1 = Process(target = func1)
    pr1.start()
    pr2 = Process(target = func2)
    pr2.start()
    pr3 = Process(target = func3)
    pr3.start()

root = tk.Tk()

if __name__=='__main__':
    pr1 = Process(target = func1)
    pr1.start()
    pr2 = Process(target = func2)
    pr2.start()
    pr3 = Process(target = func3)
    pr3.start()