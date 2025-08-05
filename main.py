from machine import Pin
from utime import sleep

print("Hello World!")

led_1 = Pin(14, Pin.OUT) #Vermelho
led_2 = Pin(12, Pin.OUT) #Amarelo
led_3 = Pin(13, Pin.OUT) #Verde

while True:
    led_1.on()
    print("Led1 ON!")
    sleep(0.8)
    led_1.off()
    print("LED1 OFF!")
    sleep(0.5)
    led_2.on()
    print("Led2 ON!")
    sleep(0.8)
    led_2.off()
    print("LED2 OFF!")
    sleep(0.5)
    led_3.on()
    print("Led3 ON!")
    sleep(0.8)
    led_3.off()
    print("LED3 OFF!")
    sleep(0.5)