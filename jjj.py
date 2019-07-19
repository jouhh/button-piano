from gpiozero import Button
from psonic import *

button1 = Button(2)

while True:
    if button1.is_pressed:
        play(A3)
        print("button 1 is pressed")
        
    
