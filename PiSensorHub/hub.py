# v Imports/variables v#
from digitalio import DigitalInOut
import board
import time
from Sensors import laser_base
from Sensors import digitalSensors
import rio_coms
import animations

lightCount = animations.qty
xshut = laser_base.xshut
lasers = laser_base.vl53
dio = digitalSensors.digitalList
enabled = True


# v Between these are the only things you should change v#

listedShutoffs = [
    # DigitalInOut(board.D20),
    # DigitalInOut(board.D19)
]  # Add list of Laser XSHUT pins
# xshut.append(listedShutoffs)                    #Keep commented unless using lasers

# dio['limitSwitch'] = DigitalInOut(board.D16)    #copy to add digital sensors, board port is signal pin, change name

# LED Signal Pin is set in animations, D21 to start
lightCount = 10  # Number of leds
mode = "Rotate"  # "Rotate" or "Message" right now
message = "Message Here"  # If running message code, message to convert
cycleDelay = 0.1
hex1 = (125, 0, 200)
hex2 = (0, 0, 255)

# ^ Between these are the only things you should change ^#


# code that runs during the match
digitalSensors.pinSetup()
laser_base.set_addresses()
animations.setup(lightCount, mode, hex1, hex2, message)

while enabled:
    if rio_coms.disabled():
        enabled = False
    else:
        # input()                #only use when debugging, comment out otherwise

        # Runs the chosen LED program
        animations.run(mode, hex1, hex2)

        for i in range(len(lasers)):
            rio_coms.send_value(i + 1, int(laser_base.distance(i)))
        # you may need a delay for the lights depending on the number of sensors, comment it out if you don't
        time.sleep(cycleDelay)


# This runs after the robot is disabled
laser_base.reset_addresses()
animations.rainbow_cycle(0)
