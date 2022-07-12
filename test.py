import tkinter
import tkinter.messagebox
import customtkinter
import subprocess
import threading
import time
import os

customtkinter.set_appearance_mode("dark")
#customtkinter.set_default_color_theme("green")  

root = customtkinter.CTk()
root.title('Temperature Monitoring System App')
root.geometry("800x480")

text_var = tkinter.StringVar(value="Temperature Monitoring System")

#Functions()
def Measure():
    #time.sleep(5)
    print("u dum bitch")
    
def Tilt():
    print("tilting u dum bitch")

#Top Label
label = customtkinter.CTkLabel(master=root,
                               textvariable=text_var,
                               width=500,
                               height=110,
                               fg_color=("white", "light blue"),
                               corner_radius=10,
                               text_font=("Roboto Medium","24"),
                               text_color=("black"))
label.place(relx=0.5, rely=0.01, anchor=tkinter.N)

#Measure Button
button1 = customtkinter.CTkButton(master=root,
                                 width=220,
                                 height=90,
                                 fg_color=("white", "light blue"),
                                 border_width=2,
                                 corner_radius=10,
                                 text="Measure",
                                 text_font=("Roboto Medium","24"),
                                 text_color=("black"),
                                 command=Measure)
button1.place(relx=0.32, rely=0.37, anchor=tkinter.CENTER)

#Tilt Button
button2 = customtkinter.CTkButton(master=root,
                                 width=220,
                                 height=90,
                                 fg_color=("white", "light blue"),
                                 border_width=2,
                                 corner_radius=10,
                                 text="Tilt",
                                 text_font=("Roboto Medium","24"),
                                 text_color=("black"),
                                 command=Tilt)
button2.place(relx=0.68, rely=0.37, anchor=tkinter.CENTER)

if __name__ == "__main__":
    root.mainloop()
