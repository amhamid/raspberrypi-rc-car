import RPi.GPIO as gpio
import time

# motor 1: right side (e.g. input 1 from L298N driver to pin 15)
pin_input_1 = 15
pin_input_2 = 13  # true ==> forward

# motor 2: left side
pin_input_3 = 11
pin_input_4 = 7   # true  ==> forward

# init gpio pins
def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(pin_input_1, gpio.OUT)
    gpio.setup(pin_input_2, gpio.OUT)
    gpio.setup(pin_input_3, gpio.OUT)
    gpio.setup(pin_input_4, gpio.OUT)


def forward():
    init()
    # left side
    gpio.output(pin_input_3, False)
    gpio.output(pin_input_4, True)

    # right side
    gpio.output(pin_input_2, True)
    gpio.output(pin_input_1, False)

    # for a few seconds
    time.sleep(1)
    gpio.cleanup()


def backward():
    init()
    # left side
    gpio.output(pin_input_3, True)
    gpio.output(pin_input_4, False)

    # right side
    gpio.output(pin_input_2, False)
    gpio.output(pin_input_1, True)

    # for a few seconds
    time.sleep(0.3)
    gpio.cleanup()


def left():
    init()
    # left side
    gpio.output(pin_input_4, True)
    gpio.output(pin_input_3, True)

    # right side
    gpio.output(pin_input_2, True)
    gpio.output(pin_input_1, False)

    # for a few seconds
    time.sleep(0.5)
    gpio.cleanup()


def right():
    init()
    # left side
    gpio.output(pin_input_4, True)
    gpio.output(pin_input_3, False)

    # right side
    gpio.output(pin_input_2, True)
    gpio.output(pin_input_1, True)

    # for a few seconds
    time.sleep(0.5)
    gpio.cleanup()
