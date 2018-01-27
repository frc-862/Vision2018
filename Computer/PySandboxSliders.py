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
lmin = 60
lmax = 253
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
def update_lmin(val):
    global lmin
    global lmax
    lmin = val
    send_command('setLMin ' + lmin)
    
####################################################################################################
def update_lmax(val):
    global lmin
    global lmax
    lmax = val
    send_command('setLMax ' + lmax)
    
####################################################################################################
def update_min_area(val):
    minarea = val
    send_command('setMinArea ' + minarea)
    
####################################################################################################
def save_params():
    send_command('saveParams' + '')
    
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
lmin = float(vals[4])
lmax = float(vals[5])
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

w9 = Label(master, text = "Luminance min")
w9.pack()
w10 = Scale(master, from_=0, to=255, tickinterval=15, length=600, orient=HORIZONTAL, command=update_lmin)
w10.set(lmin)
w10.pack()

w11 = Label(master, text = "Luminance max")
w11.pack()
w12 = Scale(master, from_=0, to=255, tickinterval=15, length=600, orient=HORIZONTAL, command=update_lmax)
w12.set(lmax)
w12.pack()

w11 = Label(master, text = "Min Area")
w11.pack()
w12 = Scale(master, from_=1000, to=2000, tickinterval=100, length=600, orient=HORIZONTAL, command=update_min_area)
w12.set(minarea)
w12.pack()

w13 = Button(master, text="Save", command=save_params)
w13.pack()

mainloop()