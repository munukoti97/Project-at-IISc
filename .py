import Tkinter
from Tkinter import *
import tkMessageBox

import visa
import numpy as np
import time
import cv2
s=visa.instrument('USB0::0x0699::0x0353::1613189::INSTR')

def establishconnection():
            try :
             print s.ask('*IDN?')
             print ("connection established")
            except Exception as ex:
                
                print "exception raised"
                print (ex)

root=Tkinter.Tk()
label_1=Label(root, text="fre")
label_1.grid(row=0,column=0)
label_2=Label(root, text="amp")
label_2.grid(row=1,column=0)

entry_1=Entry(root)
entry_2=Entry(root)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

def help():
  tkMessageBox.showinfo("help", "ONLY GOD CAN HELP YOU!!")

def set_amplitude():
            try:
                amp=float(input('enter the amplitude:'))
                while amp>10 && amp<0:
                 if amp>10:
                    print ('enter the amplitude less than 10')
                 elif amp<0:
                    print ('enter the amplitude greater  than 0')
                 amp=float(input('enter the amplitude:'))
                s.write('SOURce1:VOLTage:LEVel:IMMediate:AMPLitude '+str(amp)+'Vpp)
                print ("amplitude set to"+str(amp)+"Vpp")
             except Exception as ex:
                        print (ex)
                        
def set_frequency():
                        
              try:
                  fre=float(input("enter the frequency:"))
                   while fre>60 && fre<0:
                      if fre>60:
                          print ('enter the frequency less than 60Mhz')
                      elif fre<0:
                          print ('enter the frequency greater  than 0')
                      fre=float(input('enter the frequency:'))
                   s.write('SOURce1:FREQUENCY '+str(fre))
                   print ("frequency set to "+str(fre)+"Mhz")
               except Exception as ex:
                        print (ex)
                        
#sets CH1 source of modulating signal to internal
s.write('SOURce1:AM:SOURce INTernal')
def set_sinusoidalwaveform():
            try:
                 s.write('SOURce1:FUNCtion SINusoid')
                 print ("sine wave form generated")
             except Exception as ex:
                  print (ex)      

def set_squarewaveform():
             try:
                   s.write('SOURce1:FUNCtion SQUare')     
                   print ("square wave form generated")
             except Exception as ex:
                  print (ex)
                        
establishconnection()
s.write('*RST')
set_amplitude()
set_frequency()
s.write('SOURce1:AM:SOURce INTernal')  
                

b=Button(root, text="help", command=help)

b.grid(row=5,columnspan=2)



B1=Button(root, text="sine", command=set_amplitude,command=set_frequency,command=set_sinusoidalwaveform)
B2=Button(root, text="square", command=set_amplitude,command=set_frequency,command=set_squarewaveform)

B1.place(width=30, height=30)
B2.place(width=30, height=30)
B1.grid(row=2,column=0)
B2.grid(row=2,column=1)


root.mainloop()
