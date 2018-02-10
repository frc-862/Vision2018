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
exp = 500
redbal = 125
bluebal = 151
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
def getExp():
    print ("HOST>> getcam absexp")
    ser.write('getcam absexp\n'.encode())
    out = ''
    time.sleep(0.1)
    while ser.inWaiting() > 0:
        out += ser.read(1).decode()
    if out != '':
        print ("JEVOIS>> " + out), # the final comma suppresses extra newline, since JeVois already sends one
        return out
        
####################################################################################################
def getRedBal():
    print ("HOST>> getcam redbal")
    ser.write('getcam redbal\n'.encode())
    out = ''
    time.sleep(0.1)
    while ser.inWaiting() > 0:
        out += ser.read(1).decode()
    if out != '':
        print ("JEVOIS>> " + out), # the final comma suppresses extra newline, since JeVois already sends one
        return out
        
####################################################################################################
def getBlueBal():
    print ("HOST>> getcam bluebal")
    ser.write('getcam bluebal\n'.encode())
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
def update_exp(val):
    exp = val
    send_command('setcam absexp ' + exp)
    
####################################################################################################
def update_redbal(val):
    redbal = val
    send_command('setcam redbal ' + redbal)
    
####################################################################################################
def update_bluebal(val):
    bluebal = val
    send_command('setcam bluebal ' + bluebal)
    
####################################################################################################
def save_params():
    send_command('saveParams ' + str(exp))
    
####################################################################################################
def streamon():
    send_command('streamon')
    
####################################################################################################
def streamoff():
    send_command('streamoff')
    
####################################################################################################
def send_frames():
    send_command('sendFrames')
    
####################################################################################################
# Main code
ser = serial.Serial(serdev, 115200, timeout=1)
#send_command('ping')                   # should return ALIVE

send_command('hello')
send_command('stopSendFrames')
buffer = getVals() #Clear serial buffer
vals = getVals().split('[')[1].split(',')
print(vals)
hmin = float(vals[0])
hmax = float(vals[1])
smin = float(vals[2])
smax = float(vals[3])
lmin = float(vals[4])
lmax = float(vals[5])
minarea = float(vals[6])
exp = int(getExp().split(' ')[1].split('\r')[0])
redbal = int(getRedBal().split(' ')[1].split('\r')[0])
bluebal = int(getBlueBal().split(' ')[1].split('\r')[0])
#send_command('sendFrames')

master = Tk()
second = Tk()

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

w11 = Label(second, text = "Min Area")
w11.pack()
w12 = Scale(second, from_=500, to=2000, tickinterval=100, length=600, orient=HORIZONTAL, command=update_min_area)
w12.set(minarea)
w12.pack()

w13 = Label(second, text = "Exposure")
w13.pack()
w14 = Scale(second, from_=1, to=1000, tickinterval=100, length=600, orient=HORIZONTAL, command=update_exp)
w14.set(exp)
w14.pack()

w15 = Label(second, text = "Redbal")
w15.pack()
w16 = Scale(second, from_=0, to=255, tickinterval=15, length=600, orient=HORIZONTAL, command=update_redbal)
w16.set(redbal)
w16.pack()

w17 = Label(second, text = "Bluebal")
w17.pack()
w18 = Scale(second, from_=0, to=255, tickinterval=15, length=600, orient=HORIZONTAL, command=update_bluebal)
w18.set(bluebal)
w18.pack()

w19 = Button(second, text="Save", command=save_params)
w19.pack()
w20 = Button(second, text="Stream on", command=streamon)
w20.pack()
w21 = Button(second, text="Stream off", command=streamoff)
w21.pack()
w22 = Button(second, text="Start sending frames to serial", command=send_frames)
w22.pack()

mainloop()