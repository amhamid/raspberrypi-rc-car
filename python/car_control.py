import RPi.GPIO as gpio
import time

# motor 1: right side (e.g. input 1 from L298N driver to pin 15)
pin_input_1 = 15
pin_input_2 = 13  # true ==> forward

# motor 2: left side
pin_input_3 = 11
pin_input_4 = 7  # true  ==> forward

pin_enable_a = 16
pin_enable_b = 18

# init gpio pins
def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(pin_input_1, gpio.OUT)
    gpio.setup(pin_input_2, gpio.OUT)
    gpio.setup(pin_input_3, gpio.OUT)
    gpio.setup(pin_input_4, gpio.OUT)
    gpio.setup(pin_enable_a, gpio.OUT)
    gpio.setup(pin_enable_b, gpio.OUT)
    start_engine()


def cleanup():
    gpio.cleanup()


def start_engine():
    gpio.output(pin_input_1, False)
    gpio.output(pin_input_2, False)
    gpio.output(pin_input_3, False)
    gpio.output(pin_input_4, False)
    gpio.output(pin_enable_a, True)
    gpio.output(pin_enable_b, True)


def stop_engine():
    init()
    gpio.output(pin_input_1, False)
    gpio.output(pin_input_2, False)
    gpio.output(pin_input_3, False)
    gpio.output(pin_input_4, False)
    gpio.output(pin_enable_a, False)
    gpio.output(pin_enable_b, False)


def left():
    init()
    gpio.output(pin_input_3, False)
    gpio.output(pin_input_4, True)
    gpio.output(pin_input_2, True)
    gpio.output(pin_input_1, False)


def right():
    init()
    gpio.output(pin_input_3, True)
    gpio.output(pin_input_4, False)
    gpio.output(pin_input_2, False)
    gpio.output(pin_input_1, True)


def forward():
    init()
    gpio.output(pin_input_3, True)
    gpio.output(pin_input_4, False)
    gpio.output(pin_input_2, True)
    gpio.output(pin_input_1, False)


def backward():
    init()
    gpio.output(pin_input_3, False)
    gpio.output(pin_input_4, True)
    gpio.output(pin_input_2, False)
    gpio.output(pin_input_1, True)

