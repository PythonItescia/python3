import time
from Arduino import Arduino

port = 'COM6'
ard = Arduino(port)

ard.pinMode(2, ard.OUTPUT)
ard.pinMode(3, ard.INPUT)
ard.pinMode(4, ard.OUTPUT)
for i in range(10):
    print(ard.analogRead(0))
    time.sleep(1)
ard.analogWrite(5, 100)  # utiliser une sortie PWM pour cela
for i in range(10):
    ard.digitalWrite(2, ard.HIGH)
    time.sleep(1)
    ard.digitalWrite(2, ard.LOW)
    time.sleep(1)
    print(ard.digitalRead(3))
ard.close()