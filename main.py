# main.py -- put your code here!

from pyb import Pin, ExtInt, Timer

pm1 = Pin('X1') # X1 has TIM2, CH1
tim2 = Timer(2, freq=1000)
ch1 = tim2.channel(1, Timer.PWM, pin=pm1)
ch1.pulse_width_percent(0)


callback_m1c1 = lambda e: print("intr_m1c1")
ext_m1c1 = ExtInt(Pin('Y1'), ExtInt.IRQ_RISING, Pin.PULL_NONE, callback_m1c1)

callback_m1c2 = lambda e: print("intr_m1c2")
ext_m1c2 = ExtInt(Pin('Y2'), ExtInt.IRQ_RISING, Pin.PULL_NONE, callback_m1c2)
