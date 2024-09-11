from machine import Pin
from time import sleep
#Trafiklys
pb1 = Pin(4, Pin.IN)

tryk = 0

RED_PIN = 26
led1 = Pin(RED_PIN, Pin.OUT)

YELLOW_PIN = 12
led2 = Pin(YELLOW_PIN, Pin.OUT)
led2.on()

GREEN_PIN = 13
led3 = Pin(GREEN_PIN, Pin.OUT)

#Del 1
"""while True:
    print("Red led1 ON!")
    led1.on()
    sleep(1)
    print("Red led1 OFF!")
    led1.off()
    sleep(1)"""

#Del 2
"""while True:
    print("Red led1 ON!")
    led1.on()
    sleep(0.5)
    print("Red led1 OFF!")
    led1.off()
    sleep(0.5)"""

#DEl 3
"""while True:
    print("Green led3 ON!")
    led3.on()
    sleep(0.01)
    print("Green led3 OFF!")
    led3.off()
    sleep(0.01)"""

#Del 4
"""
while True:
    led3.on()
    led2.off()
    led1.on()
    sleep(1)
    led3.off()
    led2.on()
    led1.off()
    sleep(1)
"""
#Del 5
"""
while True:
    led1.on()
    sleep(1)
    led1.off()
    sleep(1)
    led2.off()
    sleep(1)
    led2.on()
    sleep(1)
    led3.on()
    sleep(1)
    led3.off()
    sleep(1)
    """
#Del 6
"""
while True:
    led1.on()
    sleep(2)
    led2.off()
    sleep(2)
    led1.off()
    led2.on()
    led3.on()
    sleep(4)
    led3.off()
    """


#Kode-knap/LED
#Øvelse 5
#Del 3
"""while True:
    if pb1.value() == 0:
        tryk += 1
        print("Antal tryk", tryk)
        sleep(0.2)"""
        
#Del 2
"""
led_state = False  
last_button_state = 1 

while True:
   
    current_button_state = pb1.value()

    
    if last_button_state == 1 and current_button_state == 0:
        
        led_state = not led_state  # Toggler mellem True og False
        if led_state:
            led1.on()  
        else:
            led1.off() 
        
        sleep(0.2)

    last_button_state = current_button_state
    """
    
#Øvelse 6
    #Del1
""" while True:
    if pb1.value() == 0:
        tryk += 1
        print("Antal tryk", tryk)
        sleep(0.2)"""#sleep sørger for en debounc håndtering af knappen


    


    
        
    

  
   
    
   
    
    
    

