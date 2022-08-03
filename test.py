import tkinter
import tkinter.messagebox
import customtkinter
import datetime
import time
import sys
import ast
import os, signal
from os import system
import subprocess
import testing
from testing import live
import trace
import threading
import servomotortest

class thread_with_trace(threading.Thread):
  def __init__(self, *args, **keywords):
    threading.Thread.__init__(self, *args, **keywords)
    self.killed = False
 
  def start(self):
      try:
          self.__run_backup = self.run
          self.run = self.__run     
          threading.Thread.start(self)
      except SensorNotReadyError:
          print("error")
 
  def __run(self):
    sys.settrace(self.globaltrace)
    self.__run_backup()
    self.run = self.__run_backup
 
  def globaltrace(self, frame, event, arg):
    if event == 'call':
      return self.localtrace
    else:
      return None
 
  def localtrace(self, frame, event, arg):
    if self.killed:
      if event == 'line':
        raise SystemExit()
    return self.localtrace
 
  def kill(self):
    self.killed = True

customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()
root.title('Temperature Monitoring System App')
root.geometry("800x480")

text_var = tkinter.StringVar(value="Temperature Monitoring System")
number = [26.5,27.0,26.7,24.0,25.0,26.0,27.0,26.0,26.7,26.8]

#Temperature Reading
lab1 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = "Tray 01",text_font=("Roboto Medium","16"),text_color=("black"))
lab2 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = "Tray 02",text_font=("Roboto Medium","16"),text_color=("black"))
lab3 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = "Tray 03",text_font=("Roboto Medium","16"),text_color=("black"))
lab4 = customtkinter.CTkLabel(master=root,width=25,height=40,fg_color=("light blue"),corner_radius=10,text = "Tray 04",text_font=("Roboto Medium","16"),text_color=("black"))
lab5 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = "Tray 05",text_font=("Roboto Medium","16"),text_color=("black"))
lab6 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = "Tray 06",text_font=("Roboto Medium","16"),text_color=("black"))
lab7 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = "Tray 07",text_font=("Roboto Medium","16"),text_color=("black"))
lab8 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = "Tray 08",text_font=("Roboto Medium","16"),text_color=("black"))
lab9 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = "Tray 09",text_font=("Roboto Medium","16"),text_color=("black"))
lab10 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("light blue"),corner_radius=10,text = "Tray 10",text_font=("Roboto Medium","16"),text_color=("black"))

temp1 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("blue"),corner_radius=10,text = str(0)+"°C",text_font=("Roboto Medium","16"),text_color=("black"))
temp2 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("blue"),corner_radius=10,text = str(0)+"°C",text_font=("Roboto Medium","16"),text_color=("black"))
temp3 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("blue"),corner_radius=10,text = str(0)+"°C",text_font=("Roboto Medium","16"),text_color=("black"))
temp4 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("blue"),corner_radius=10,text = str(0)+"°C",text_font=("Roboto Medium","16"),text_color=("black"))
temp5 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("blue"),corner_radius=10,text = str(0)+"°C",text_font=("Roboto Medium","16"),text_color=("black"))
temp6 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("blue"),corner_radius=10,text = str(0)+"°C",text_font=("Roboto Medium","16"),text_color=("black"))
temp7 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("blue"),corner_radius=10,text = str(0)+"°C",text_font=("Roboto Medium","16"),text_color=("black"))
temp8 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("blue"),corner_radius=10,text = str(0)+"°C",text_font=("Roboto Medium","16"),text_color=("black"))
temp9 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("blue"),corner_radius=10,text = str(0)+"°C",text_font=("Roboto Medium","16"),text_color=("black"))
temp10 = customtkinter.CTkLabel(master=root,width=20,height=40,fg_color=("blue"),corner_radius=10,text = str(0)+"°C",text_font=("Roboto Medium","16"),text_color=("black"))

#Functions()
global process
process = 0
global switch
switch = 0
def Measure():
    try:
        global process
        global liveprocess
        process = thread_with_trace(target = testing.func)
        liveprocess = thread_with_trace(target = live)
        process.start()
        liveprocess.start()
        global switch
        switch = 1
        if switch == 1:
            button1.place_forget()
            button2.place(relx=0.32, rely=0.37, anchor=tkinter.CENTER)
    except:
        print("Something went wrong")
        
def StopMeasure():
    #os.killpg(os.getpgid(process.pid), signal.SIGTERM)
    process.kill()
    #liveprocess.kill()
    process.join()
    #liveprocess.join()
    
    global switch
    switch = 0
    if switch == 0:
        button2.place_forget()
        button1.place(relx=0.32, rely=0.37, anchor=tkinter.CENTER)
        
    print("Measurement has been halted")

def live():
    while(1):
        #time.sleep(5)
        for i in range(10):
                #print("this is", i)
            if testing.live[i] == 26.7 and len(testing.live) == 10:
                #print("tray ", i+1, "at temperature : ",testing.live[i], ", is green")
                globals()['temp%s'%str(i+1)].configure(fg_color=("green"),text = str(testing.live[i])+"°C")
                    
            elif testing.live[i] >= 26.8 and len(testing.live) == 10:
                globals()['temp%s'% str(i+1)].configure(fg_color=("red"),text = str(testing.live[i])+"°C")
                    
            elif testing.live[i] <= 26.6 and len(testing.live) == 10:
                globals()['temp%s'%str(i+1)].configure(fg_color=("blue"),text = str(testing.live[i])+"°C")
            
            else:
                print("nothing changed")
        #time.sleep(5)

global tilt
tilt = 0
def Tilt():
    servomotortest.tilt()
    global tilt
    tilt = 1
    if tilt == 1:
        button3.place_forget()
        button4.place(relx=0.68, rely=0.37, anchor=tkinter.CENTER)

def Untilt():
    servomotortest.untilt()
    global tilt
    tilt = 0
    if tilt == 0:
        button4.place_forget()
        button3.place(relx=0.68, rely=0.37, anchor=tkinter.CENTER)
        
def optionmenu(choice):
    if choice == "Temperature Reading":
        #output = subprocess.check_output('python3', 'cloud.py', shell=True)
        #live = ast.literal_eval(output.decode("ascii"))
        #print(live)
        label1.place_forget()
        button1.place_forget()
        button2.place_forget()
        button3.place_forget()
        button4.place_forget()
        lab1.place(relx=0.15, rely=0.01, anchor=tkinter.N)
        temp1.place(relx=0.30, rely=0.01, anchor=tkinter.N)
        lab2.place(relx=0.15, rely=0.15, anchor=tkinter.N)
        temp2.place(relx=0.30, rely=0.15, anchor=tkinter.N)
        lab3.place(relx=0.15, rely=0.30, anchor=tkinter.N)
        temp3.place(relx=0.30, rely=0.30, anchor=tkinter.N)
        lab4.place(relx=0.15, rely=0.45, anchor=tkinter.N)
        temp4.place(relx=0.30, rely=0.45, anchor=tkinter.N)
        lab5.place(relx=0.15, rely=0.60, anchor=tkinter.N)
        temp5.place(relx=0.30, rely=0.60, anchor=tkinter.N)
        lab6.place(relx=0.63, rely=0.01, anchor=tkinter.N)
        temp6.place(relx=0.78, rely=0.01, anchor=tkinter.N)
        lab7.place(relx=0.63, rely=0.15, anchor=tkinter.N)
        temp7.place(relx=0.78, rely=0.15, anchor=tkinter.N)
        lab8.place(relx=0.63, rely=0.30, anchor=tkinter.N)
        temp8.place(relx=0.78, rely=0.30, anchor=tkinter.N)
        lab9.place(relx=0.63, rely=0.45, anchor=tkinter.N)
        temp9.place(relx=0.78, rely=0.45, anchor=tkinter.N)
        lab10.place(relx=0.63, rely=0.60, anchor=tkinter.N)
        temp10.place(relx=0.78, rely=0.60, anchor=tkinter.N)
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
        if switch == 0:
            button1.place(relx=0.32, rely=0.37, anchor=tkinter.CENTER)
        else:
            button2.place(relx=0.32, rely=0.37, anchor=tkinter.CENTER)
        if tilt == 0:
            button3.place(relx=0.68, rely=0.37, anchor=tkinter.CENTER)
        else:
            button4.place(relx=0.68, rely=0.37, anchor=tkinter.CENTER)


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

#Stop Button
button2 = customtkinter.CTkButton(master=root,
                                 width=220,
                                 height=90,
                                 fg_color=("white", "light blue"),
                                 border_width=2,
                                 corner_radius=10,
                                 text="Stop",
                                 text_font=("Roboto Medium","24"),
                                 text_color=("black"),
                                 command=StopMeasure)
#button2.place(relx=0.32, rely=0.37, anchor=tkinter.CENTER)

#Tilt Button
button3 = customtkinter.CTkButton(master=root,
                                 width=220,
                                 height=90,
                                 fg_color=("white", "light blue"),
                                 border_width=2,
                                 corner_radius=10,
                                 text="Tilt",
                                 text_font=("Roboto Medium","24"),
                                 text_color=("black"),
                                 command=Tilt)
button3.place(relx=0.68, rely=0.37, anchor=tkinter.CENTER)

#Untilt Button
button4 = customtkinter.CTkButton(master=root,
                                 width=220,
                                 height=90,
                                 fg_color=("white", "light blue"),
                                 border_width=2,
                                 corner_radius=10,
                                 text="Untilt",
                                 text_font=("Roboto Medium","24"),
                                 text_color=("black"),
                                 command=Untilt)
#button2.place(relx=0.32, rely=0.37, anchor=tkinter.CENTER)

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
optionmenu.place(relx=0.5, rely=0.82, anchor=tkinter.CENTER)
optionmenu.set("Controls")  # set initial value

if __name__ == "__main__":
     root.mainloop()


Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/lib/python3.7/threading.py", line 917, in _bootstrap_inner
    self.run()
  File "/home/pi/Desktop/MP/tkintertest.py", line 32, in __run
    self.__run_backup()
  File "/usr/lib/python3.7/threading.py", line 865, in run
    self._target(*self._args, **self._kwargs)
  File "/home/pi/Desktop/MP/testing.py", line 77, in func
    calibratedval = sensor.get_temperature() + reference[x]
  File "/usr/local/lib/python3.7/dist-packages/w1thermsensor/core.py", line 267, in get_temperature
    raw_temperature_line = self.get_raw_sensor_strings()[1]
  File "/usr/local/lib/python3.7/dist-packages/w1thermsensor/core.py", line 250, in get_raw_sensor_strings
    raise SensorNotReadyError(self)
w1thermsensor.errors.SensorNotReadyError: Sensor 3c01f096fcdd is not yet ready to read temperature
