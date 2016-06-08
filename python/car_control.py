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


# TODO:
# why the wheel on one side runs first ==> this cause problem on restart (too much power)
# findout a little shock cause raspberry pi to restart !!!


# init gpio pins
def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(pin_input_1, gpio.OUT)
    gpio.setup(pin_input_2, gpio.OUT)
    gpio.setup(pin_input_3, gpio.OUT)
    gpio.setup(pin_input_4, gpio.OUT)
    gpio.setup(pin_enable_a, gpio.OUT)
    gpio.setup(pin_enable_b, gpio.OUT)


def cleanup():
    gpio.cleanup()


def start_engine():
    init()
    gpio.output(pin_enable_a, True)
    gpio.output(pin_enable_b, True)


def stop_engine():
    init()
    gpio.output(pin_enable_a, False)
    gpio.output(pin_enable_b, False)


def forward():
    init()
    # left side
    gpio.output(pin_input_3, False)
    gpio.output(pin_input_4, True)

    # right side
    gpio.output(pin_input_2, True)
    gpio.output(pin_input_1, False)
    time.sleep(2)
    cleanup()


def backward():
    init()
    # left side
    gpio.output(pin_input_3, True)
    gpio.output(pin_input_4, False)

    # right side
    gpio.output(pin_input_2, False)
    gpio.output(pin_input_1, True)


def left():
    init()
    # left side
    gpio.output(pin_input_4, True)
    gpio.output(pin_input_3, True)

    # right side
    gpio.output(pin_input_2, True)
    gpio.output(pin_input_1, False)


def right():
    init()
    # left side
    gpio.output(pin_input_4, True)
    gpio.output(pin_input_3, False)

    # right side
    gpio.output(pin_input_2, True)
    gpio.output(pin_input_1, True)


start_engine()
forward()
