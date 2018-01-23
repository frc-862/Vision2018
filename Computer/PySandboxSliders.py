#!/usr/bin/python

# Needed packages: sudo apt-get install python python-tk python-serial

# This tutorial is a simple program that allows one to adjust the hue, saturation, and value ranges of the ObjectTracker
# module using sliders

serdev = input("What port: ") # serial device of JeVois

from tkinter import *
import serial
import time


# default values for Hue, Saturation, and Value ranges:
hmin = 95
hmax = 110
smin = 100
smax = 255
vmin = 60
vmax = 253
minarea = 2000
hslToggle = False

####################################################################################################
# Send a command to JeVois and show response
def send_command(cmd):
    print ("HOST>> " + cmd)
    ser.write(cmd.encode() + '\n'.encode())
    out = ''
    time.sleep(0.1)
    while ser.inWaiting() > 0:
        out += ser.read(1).decode()
    if out != '':
        print ("JEVOIS>> " + out), # the final comma suppresses extra newline, since JeVois already sends one
        
####################################################################################################
# Get hsl parameters from camera
def getVals():
    print ("HOST>> getVals")
    ser.write('getVals\n'.encode())
    out = ''
    time.sleep(0.1)
    while ser.inWaiting() > 0:
        out += ser.read(1).decode()
    if out != '':
        print ("JEVOIS>> " + out), # the final comma suppresses extra newline, since JeVois already sends one
        return out
        
####################################################################################################
def update_hmin(val):
    global hmin
    global hmax
    hmin = val
    send_command('setHMin ' + hmin)
    
####################################################################################################
def update_hmax(val):
    global hmin
    global hmax
    hmax = val
    send_command('setHMax ' + hmax)
    
####################################################################################################
def update_smin(val):
    global smin
    global smax
    smin = val
    send_command('setSMin ' + smin)
    
####################################################################################################
def update_smax(val):
    global smin
    global smax
    smax = val
    send_command('setSMax ' + smax)

####################################################################################################
def update_vmin(val):
    global vmin
    global vmax
    vmin = val
    send_command('setVMin ' + vmin)
    
####################################################################################################
def update_vmax(val):
    global vmin
    global vmax
    vmax = val
    send_command('setVMax ' + vmax)
    
####################################################################################################
def update_min_area(val):
    minarea = val
    send_command('setMinArea ' + vmax)
    
####################################################################################################
def toggleHSL():
    if hslToggle == True:
        send_command('toggleHSL t')
    else:
        send_command('toggleHSL f')
    
####################################################################################################
# Main code
ser = serial.Serial(serdev, 115200, timeout=1)
#send_command('ping')                   # should return ALIVE

send_command('hello')
vals = getVals().split('[')[1].split(',')
print(vals)
hmin = float(vals[0])
hmax = float(vals[1])
smin = float(vals[2])
smax = float(vals[3])
vmin = float(vals[4])
vmax = float(vals[5])
minarea = float(vals[6])

master = Tk()

w1 = Label(master, text = "Hue min")
w1.pack()
w2 = Scale(master, from_=0, to=255, tickinterval=15, length=600, orient=HORIZONTAL, command=update_hmin)
w2.set(hmin)
w2.pack()

w3 = Label(master, text = "Hue max")
w3.pack()
w4 = Scale(master, from_=0, to=255, tickinterval=15, length=600, orient=HORIZONTAL, command=update_hmax)
w4.set(hmax)
w4.pack()

w5 = Label(master, text = "Saturation min")
w5.pack()
w6 = Scale(master, from_=0, to=255, tickinterval=15, length=600, orient=HORIZONTAL, command=update_smin)
w6.set(smin)
w6.pack()

w7 = Label(master, text = "Saturation max")
w7.pack()
w8 = Scale(master, from_=0, to=255, tickinterval=15, length=600, orient=HORIZONTAL, command=update_smax)
w8.set(smax)
w8.pack()

w9 = Label(master, text = "Value min")
w9.pack()
w10 = Scale(master, from_=0, to=255, tickinterval=15, length=600, orient=HORIZONTAL, command=update_vmin)
w10.set(vmin)
w10.pack()

w11 = Label(master, text = "Value max")
w11.pack()
w12 = Scale(master, from_=0, to=255, tickinterval=15, length=600, orient=HORIZONTAL, command=update_vmax)
w12.set(vmax)
w12.pack()

w11 = Label(master, text = "Min Area")
w11.pack()
w12 = Scale(master, from_=1000, to=2000, tickinterval=100, length=600, orient=HORIZONTAL, command=update_min_area)
w12.set(minarea)
w12.pack()

w15 = Checkbutton(master, text="Show raw HSL output", variable=hslToggle, onvalue=True, offvalue=False, command=toggleHSL)

mainloop()