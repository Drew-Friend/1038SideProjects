#v Imports/variables v#
import board
import serial
rio = serial.Serial('/dev/serial0', 9600, timeout = 0, write_timeout = 0)

#checks if the robot has been disabled
def disabled():
    standin = rio.read().decode('utf-8')
    if standin is 'D':
        return True
    else:
        return False

def loop():
    rio.write('D'.encode('utf-8'))
    

#def disabled():
#    print((rio.read()).decode('utf-8'))
#    if rio.read() is 'D':                  #This block can be renamed and use a different byte for any command from the rio
#        return True
#    else:
#        return False


#sends values to rio and prints them, add any new sensors to this
def send_value(laser, value):
    print("Laser {}: {}".format(laser, value))
    rio.write([value])