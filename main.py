import max30102
import hrcalc
import bluetooth
import time

def connect(addr):
 serverMACAddress = addr
 port = 2
 s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
 s.connect((serverMACAddress, port))
 while 1:
    text = str(hr2) 
    if text == "quit":
      break
    if(addr): 
       s.send(text)
    time.sleep(1)
    print(addr)
 s.close()

addr = "70:2C:1F:31:AF:7B"

m = max30102.MAX30102()

hr2 = 0
#sp2 = 0

while True:
    red, ir = m.read_sequential()
    
    hr,hrb,sp,spb = hrcalc.calc_hr_and_spo2(ir, red)

    print("hr detected:",hrb)
    #print("sp detected:",spb)
    
    if(hrb == True and hr != -999):
        hr2 = int(hr)
        #print("Heart Rate : ",hr2)
    #if(spb == True and sp != -999):
        #sp2 = int(sp)
        #print("SPO2       : ",sp2)

        time.sleep(16)
        connect(addr)