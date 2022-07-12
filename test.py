import tkinter
import tkinter.messagebox
import customtkinter
import subprocess
import threading
import time
import os

customtkinter.set_appearance_mode("dark")  

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

def optionmenu(choice):
    if choice == "Temperature Chart":
        label.place_forget()
        button1.place_forget()
        button2.place_forget()
    else:
        label.place(relx=0.5, rely=0.01, anchor=tkinter.N)
        button1.place(relx=0.32, rely=0.37, anchor=tkinter.CENTER)
        button2.place(relx=0.68, rely=0.37, anchor=tkinter.CENTER)

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

#OptionMenu for View between controls and Temperature
optionmenu = customtkinter.CTkOptionMenu(master=root,
                                       width=300,
                                       height=50,
                                       fg_color=("white", "light blue"),
                                       text_font=("Roboto Medium","14"),
                                       dropdown_text_font=("Roboto Medium","14"),
                                       text_color=("black"),
                                       values=["Controls", "Temperature Chart"],
                                       command=optionmenu)
optionmenu.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
optionmenu.set("Controls")  # set initial value

if __name__ == "__main__":
    root.mainloop()
