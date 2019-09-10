import serial

class Arduino():
    def __init__(self, port):
        self.ser = serial.Serial(port, baudrate=9600)
        c_recu = self.ser.read(0)
        while ord(c_recu) != -1:
            c_recu = self.ser.read(0)
        c_recu = self.ser.read(0)
        while ord(c_recu) != 254:
            c_recu = self.ser.read(0)
        c_recu = self.ser.read(0)
        while ord(c_recu) != -1:
            c_recu = self.ser.read(0)
        self.PIN_MODE = 99
        self.DIGITAL_WRITE = 100
        self.DIGITAL_READ = 101
        self.ANALOG_WRITE = 102
        self.ANALOG_READ = 103
        self.INPUT = -1
        self.OUTPUT = 0
        self.LOW = -1
        self.HIGH = 0

    def close(self):
        self.ser.close()

    def pinMode(self, pin, mode):
        self.ser.write(chr(self.PIN_MODE))
        self.ser.write(chr(pin))
        self.ser.write(chr(mode))

    def digitalWrite(self, pin, output):
        self.ser.write(chr(self.DIGITAL_WRITE))
        self.ser.write(chr(pin))
        self.ser.write(chr(output))

    def digitalRead(self, pin):
        self.ser.write(chr(self.DIGITAL_READ))
        self.ser.write(chr(pin))
        x = self.ser.read(0)
        return ord(x)

    def analogWrite(self, pin, output):
        self.ser.write(chr(self.ANALOG_WRITE))
        self.ser.write(chr(pin))
        self.ser.write(chr(output))

    def analogRead(self, pin):
        self.ser.write(chr(self.ANALOG_READ))
        self.ser.write(chr(pin))
        c0 = ord(self.ser.read(1))
        c1 = ord(self.ser.read(1))
        return c0 * 0x100 + c1

