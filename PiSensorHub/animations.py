import board
import neopixel
import time
import sys

cycle = 0
rotateCheck = 0
qty = 10
offset = 0
digits = []
firstRun = True
primary = True
leds = neopixel.NeoPixel(board.D21, qty)

# sets up the message to run in binary
def messageSetup(message):
    global digits
    res = "".join(format(ord(i), "b") for i in message)
    for i in res:
        digits.append(i)


# actually runs the binary message
def message(colorA, colorB):
    global digits
    global qty
    for i in range(qty):
        if digits[i] == "0":
            leds[i] = colorA
        if digits[i] == "1":
            leds[i] = colorB
    digits = digits[1:] + digits[:1]


# Rotates between 2 colors
def rotate():
    global rotateCheck
    leds[qty - 1] = leds[0]
    for i in range(qty - 1):
        leds[i] = leds[i + 1]


def rotateSetup(colorA, colorB, length, section):
    global primary
    for i in range(length):
        if i % section == 0:
            primary = not primary
        if primary:
            leds[i - rotateCheck] = colorA
        else:
            leds[i - rotateCheck] = colorB


def setup(len=10, mode="Rotate", colorA=(125, 0, 200), colorB=(0, 0, 255), message=""):
    if mode == "Message":
        messageSetup(message)
    else:
        rotateSetup(colorA, colorB, len, 4)


def run(mode, colorA, colorB):
    if mode == "Message":
        message(colorA, colorB)
    else:
        rotate()


# GAY!! fun pretty estop code
def rainbow_cycle(wait):
    while True:
        global qty
        for j in range(255):
            for i in range(qty):
                pixel_index = (i * 256 // qty) + j
                leds[i] = wheel(pixel_index & 255)
            time.sleep(wait)


# Wheel is used by the rainbow to...rainbow
def wheel(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)
