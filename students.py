#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#    Feb 12, 2019 12:36:11 AM IST  platform: Windows NT

import sys
import mysql.connector as mysql
from tkinter import messagebox
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


import students_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    students_support.set_Tk_var()
    top = Toplevel1 (root)
    students_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    students_support.set_Tk_var()
    top = Toplevel1 (w)
    students_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def show(self):
        sql = "select * from students"
        self.mycursor.execute(sql)
        result = self.mycursor.fetchall()
        for info in result:
            self.Listbox1.insert(END,info)

    def __init__(self, top=None):
        try:
            self.studentDB = mysql.connect(host="localhost",user="chetan",passwd="chetan123",database="pythonDB")
            self.mycursor = self.studentDB.cursor()
        except Exception:
            messagebox.showerror("ERROR","Can't connect to Student database.")




        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("645x656+323+0")
        top.title("Student Data")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.186, rely=0.046, relheight=0.373
                , relwidth=0.628)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=405)

        self.Name = tk.Label(self.Frame1)
        self.Name.place(relx=0.173, rely=0.816, height=21, width=38)
        self.Name.configure(activebackground="#f9f9f9")
        self.Name.configure(activeforeground="black")
        self.Name.configure(background="#d9d9d9")
        self.Name.configure(disabledforeground="#a3a3a3")
        self.Name.configure(foreground="#000000")
        self.Name.configure(highlightbackground="#d9d9d9")
        self.Name.configure(highlightcolor="black")
        self.Name.configure(text='''Age''')

        self.Name_3 = tk.Label(self.Frame1)
        self.Name_3.place(relx=0.173, rely=0.612, height=21, width=38)
        self.Name_3.configure(activebackground="#f9f9f9")
        self.Name_3.configure(activeforeground="black")
        self.Name_3.configure(background="#d9d9d9")
        self.Name_3.configure(disabledforeground="#a3a3a3")
        self.Name_3.configure(foreground="#000000")
        self.Name_3.configure(highlightbackground="#d9d9d9")
        self.Name_3.configure(highlightcolor="black")
        self.Name_3.configure(text='''Sex''')

        self.Name_4 = tk.Label(self.Frame1)
        self.Name_4.place(relx=0.173, rely=0.082, height=21, width=38)
        self.Name_4.configure(activebackground="#f9f9f9")
        self.Name_4.configure(activeforeground="black")
        self.Name_4.configure(background="#d9d9d9")
        self.Name_4.configure(disabledforeground="#a3a3a3")
        self.Name_4.configure(foreground="#000000")
        self.Name_4.configure(highlightbackground="#d9d9d9")
        self.Name_4.configure(highlightcolor="black")
        self.Name_4.configure(text='''Name''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.173, rely=0.408, height=21, width=38)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Marks''')

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.173, rely=0.245, height=21, width=44)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Roll no.''')

        self.Text1 = tk.Text(self.Frame1)
        self.Text1.place(relx=0.444, rely=0.082, relheight=0.098, relwidth=0.306)

        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=124)
        self.Text1.configure(wrap='word')

        self.Text1_2 = tk.Text(self.Frame1)
        self.Text1_2.place(relx=0.444, rely=0.245, relheight=0.098
                , relwidth=0.306)
        self.Text1_2.configure(background="white")
        self.Text1_2.configure(font="TkTextFont")
        self.Text1_2.configure(foreground="black")
        self.Text1_2.configure(highlightbackground="#d9d9d9")
        self.Text1_2.configure(highlightcolor="black")
        self.Text1_2.configure(insertbackground="black")
        self.Text1_2.configure(selectbackground="#c4c4c4")
        self.Text1_2.configure(selectforeground="black")
        self.Text1_2.configure(width=124)
        self.Text1_2.configure(wrap='word')

        self.Text2 = tk.Text(self.Frame1)
        self.Text2.place(relx=0.444, rely=0.408, relheight=0.098, relwidth=0.306)

        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(selectforeground="black")
        self.Text2.configure(width=124)
        self.Text2.configure(wrap='word')

        self.Spinbox1 = tk.Spinbox(self.Frame1, from_=1.0, to=100.0)
        self.Spinbox1.place(relx=0.432, rely=0.796, relheight=0.078
                , relwidth=0.333)
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1.configure(foreground="black")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(highlightcolor="black")
        self.Spinbox1.configure(insertbackground="black")
        self.Spinbox1.configure(selectbackground="#c4c4c4")
        self.Spinbox1.configure(selectforeground="black")
        self.Spinbox1.configure(textvariable=students_support.spinbox)
        self.value_list = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,]
        self.Spinbox1.configure(values=self.value_list)

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.42, rely=0.571, relheight=0.184, relwidth=0.358)

        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=145)

        self.Radiobutton4 = tk.Radiobutton(self.Frame2)
        self.Radiobutton4.place(relx=0.483, rely=0.222, relheight=0.556
                , relwidth=0.455)
        self.Radiobutton4.configure(activebackground="#ececec")
        self.Radiobutton4.configure(activeforeground="#000000")
        self.Radiobutton4.configure(background="#d9d9d9")
        self.Radiobutton4.configure(disabledforeground="#a3a3a3")
        self.Radiobutton4.configure(foreground="#000000")
        self.Radiobutton4.configure(highlightbackground="#d9d9d9")
        self.Radiobutton4.configure(highlightcolor="black")
        self.Radiobutton4.configure(justify='left')
        self.Radiobutton4.configure(text='''Female''')

        self.Radiobutton3 = tk.Radiobutton(self.Frame2)
        self.Radiobutton3.place(relx=0.069, rely=0.222, relheight=0.556
                , relwidth=0.372)
        self.Radiobutton3.configure(activebackground="#ececec")
        self.Radiobutton3.configure(activeforeground="#000000")
        self.Radiobutton3.configure(background="#d9d9d9")
        self.Radiobutton3.configure(disabledforeground="#a3a3a3")
        self.Radiobutton3.configure(foreground="#000000")
        self.Radiobutton3.configure(highlightbackground="#d9d9d9")
        self.Radiobutton3.configure(highlightcolor="black")
        self.Radiobutton3.configure(justify='left')
        self.Radiobutton3.configure(text='''Male''')

        self.Frame3 = tk.Frame(top)
        self.Frame3.place(relx=0.109, rely=0.442, relheight=0.069
                , relwidth=0.783)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(background="#d9d9d9")
        self.Frame3.configure(highlightbackground="#d9d9d9")
        self.Frame3.configure(highlightcolor="black")
        self.Frame3.configure(width=505)

        self.Button1 = tk.Button(self.Frame3)
        self.Button1.place(relx=0.079, rely=0.222, height=24, width=90)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(command=self.show,text='''Show''')

        self.Button1_7 = tk.Button(self.Frame3)
        self.Button1_7.place(relx=0.297, rely=0.222, height=24, width=87)
        self.Button1_7.configure(activebackground="#ececec")
        self.Button1_7.configure(activeforeground="#000000")
        self.Button1_7.configure(background="#d9d9d9")
        self.Button1_7.configure(disabledforeground="#a3a3a3")
        self.Button1_7.configure(foreground="#000000")
        self.Button1_7.configure(highlightbackground="#d9d9d9")
        self.Button1_7.configure(highlightcolor="black")
        self.Button1_7.configure(pady="0")
        self.Button1_7.configure(text='''Add''')

        self.Button1_8 = tk.Button(self.Frame3)
        self.Button1_8.place(relx=0.515, rely=0.222, height=24, width=87)
        self.Button1_8.configure(activebackground="#ececec")
        self.Button1_8.configure(activeforeground="#000000")
        self.Button1_8.configure(background="#d9d9d9")
        self.Button1_8.configure(disabledforeground="#a3a3a3")
        self.Button1_8.configure(foreground="#000000")
        self.Button1_8.configure(highlightbackground="#d9d9d9")
        self.Button1_8.configure(highlightcolor="black")
        self.Button1_8.configure(pady="0")
        self.Button1_8.configure(text='''Update''')

        self.Button1_9 = tk.Button(self.Frame3)
        self.Button1_9.place(relx=0.733, rely=0.222, height=24, width=87)
        self.Button1_9.configure(activebackground="#ececec")
        self.Button1_9.configure(activeforeground="#000000")
        self.Button1_9.configure(background="#d9d9d9")
        self.Button1_9.configure(disabledforeground="#a3a3a3")
        self.Button1_9.configure(foreground="#000000")
        self.Button1_9.configure(highlightbackground="#d9d9d9")
        self.Button1_9.configure(highlightcolor="black")
        self.Button1_9.configure(pady="0")
        self.Button1_9.configure(text='''Delete''')

        self.Listbox1 = tk.Listbox(top)
        self.Listbox1.place(relx=0.109, rely=0.518, relheight=0.445
                , relwidth=0.781)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(width=504)

if __name__ == '__main__':
    vp_start_gui()





