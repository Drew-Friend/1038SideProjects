from digitalio import DigitalInOut
import board

digitalList = {}

def pinSetup():
    for pin in digitalList:
        digitalList[pin].switch_to_input()

def sensorCheck(index):
    return digitalList[index].value