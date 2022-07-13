import tkinter
import tkinter.messagebox
import customtkinter
import pandas as pd
import datetime
import arraytest

customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()
root.title('Temperature Monitoring System App')
root.geometry("800x480")

text_var = tkinter.StringVar(value="Temperature Monitoring System")
number = [26.5,27.0,26.7,24.0,25.0,26.0,27.0,26.0,26.7,26.8]

#Temperature Reading
lab1 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = "Tray 01",text_font=("Roboto Medium","16"),text_color=("black"))
temp1 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = str(number[0])+"°C",text_font=("Roboto Medium","16"),text_color=("black"))
lab2 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = "Tray 02",text_font=("Roboto Medium","16"),text_color=("black"))
temp2 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = str(number[1])+"°C",text_font=("Roboto Medium","16"),text_color=("black"))
lab3 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = "Tray 03",text_font=("Roboto Medium","16"),text_color=("black"))
temp3 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = str(number[2])+"°C",text_font=("Roboto Medium","16"),text_color=("black"))
lab4 = customtkinter.CTkLabel(master=root,width=25,height=40,fg_color=("light blue"),corner_radius=10,text = "Tray 04",text_font=("Roboto Medium","16"),text_color=("black"))
temp4 = customtkinter.CTkLabel(master=root,width=50,height=40,fg_color=("light blue"),corner_radius=10,text = str(number[3])+"°C",text_font=("Roboto Medium","16"),text_color=("black"))
lab5 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = "Tray 05",text_font=("Roboto Medium","16"),text_color=("black"))
temp5 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = str(number[4])+"°C",text_font=("Roboto Medium","16"),text_color=("black"))

lab6 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = "Tray 06",text_font=("Roboto Medium","16"),text_color=("black"))
temp6 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = str(number[5])+"°C",text_font=("Roboto Medium","16"),text_color=("black"))
lab7 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = "Tray 07",text_font=("Roboto Medium","16"),text_color=("black"))
temp7 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = str(number[6])+"°C",text_font=("Roboto Medium","16"),text_color=("black"))
lab8 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = "Tray 08",text_font=("Roboto Medium","16"),text_color=("black"))
temp8 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = str(number[7])+"°C",text_font=("Roboto Medium","16"),text_color=("black"))
lab9 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = "Tray 09",text_font=("Roboto Medium","16"),text_color=("black"))
temp9 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = str(number[8])+"°C",text_font=("Roboto Medium","16"),text_color=("black"))
lab10 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = "Tray 10",text_font=("Roboto Medium","16"),text_color=("black"))
temp10 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = str(number[9])+"°C",text_font=("Roboto Medium","16"),text_color=("black"))

for i in range(10):
    if number[i] == 26.7:
        globals()[f"temp{i+1}"] = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("green"),corner_radius=10,text = str(number[i])+"°C",text_font=("Roboto Medium","16"),text_color=("black"))
    elif number[i] >= 26.8:
        globals()[f"temp{i+1}"] = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("red"),corner_radius=10,text = str(number[i])+"°C",text_font=("Roboto Medium","16"),text_color=("black"))
    elif number[i] <= 26.6:
        globals()[f"temp{i+1}"] = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("blue"),corner_radius=10,text = str(number[i])+"°C",text_font=("Roboto Medium","16"),text_color=("black"))
        
#Functions()
def Measure():
    #time.sleep(5)
    print("measuring")
        
def Tilt():
    print("tilting")

def optionmenu(choice):
    if choice == "Temperature Reading":
        label1.place_forget()
        button1.place_forget()
        button2.place_forget()
        lab1.place(relx=0.1, rely=0.01, anchor=tkinter.N)
        temp1.place(relx=0.25, rely=0.01, anchor=tkinter.N)
        lab2.place(relx=0.1, rely=0.15, anchor=tkinter.N)
        temp2.place(relx=0.25, rely=0.15, anchor=tkinter.N)
        lab3.place(relx=0.1, rely=0.30, anchor=tkinter.N)
        temp3.place(relx=0.25, rely=0.30, anchor=tkinter.N)
        lab4.place(relx=0.1, rely=0.45, anchor=tkinter.N)
        temp4.place(relx=0.25, rely=0.45, anchor=tkinter.N)
        lab5.place(relx=0.1, rely=0.60, anchor=tkinter.N)
        temp5.place(relx=0.25, rely=0.60, anchor=tkinter.N)
        lab6.place(relx=0.58, rely=0.01, anchor=tkinter.N)
        temp6.place(relx=0.83, rely=0.01, anchor=tkinter.N)
        lab7.place(relx=0.58, rely=0.15, anchor=tkinter.N)
        temp7.place(relx=0.83, rely=0.15, anchor=tkinter.N)
        lab8.place(relx=0.58, rely=0.30, anchor=tkinter.N)
        temp8.place(relx=0.83, rely=0.30, anchor=tkinter.N)
        lab9.place(relx=0.58, rely=0.45, anchor=tkinter.N)
        temp9.place(relx=0.83, rely=0.45, anchor=tkinter.N)
        lab10.place(relx=0.58, rely=0.60, anchor=tkinter.N)
        temp10.place(relx=0.83, rely=0.60, anchor=tkinter.N)
    else:
        label1.place(relx=0.5, rely=0.01, anchor=tkinter.N)
        lab1.place_forget()
        lab2.place_forget()
        lab3.place_forget()
        lab4.place_forget()
        lab5.place_forget()
        lab6.place_forget()
        lab7.place_forget()
        lab8.place_forget()
        lab9.place_forget()
        lab10.place_forget()
        temp1.place_forget()
        temp2.place_forget()
        temp3.place_forget()
        temp4.place_forget()
        temp5.place_forget()
        temp6.place_forget()
        temp7.place_forget()
        temp8.place_forget()
        temp9.place_forget()
        temp10.place_forget()
        button1.place(relx=0.32, rely=0.37, anchor=tkinter.CENTER)
        button2.place(relx=0.68, rely=0.37, anchor=tkinter.CENTER)


#clock
def update_clock():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    lab.configure(text=current_time)
    root.after(1000, update_clock) 

lab=customtkinter.CTkLabel(root)
lab.place(relx=1, rely=1, anchor=tkinter.SE)
update_clock()


#Top Label
label1 = customtkinter.CTkLabel(master=root,
                               textvariable=text_var,
                               width=500,
                               height=110,
                               fg_color=("white", "light blue"),
                               corner_radius=10,
                               text="Temperature Monitoring App",
                               text_font=("Roboto Medium","24"),
                               text_color=("black"))
label1.place(relx=0.5, rely=0.01, anchor=tkinter.N)


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
                                       values=["Controls", "Temperature Reading"],
                                       command=optionmenu)
optionmenu.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
optionmenu.set("Controls")  # set initial value

#Temperature Reading
df = pd.DataFrame({
    "Tray": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    "Temperature": arraytest.temperature
})

if __name__ == "__main__":
    root.mainloop()
