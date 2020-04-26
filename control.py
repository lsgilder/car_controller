import serial


class Control:
    port = ""
    s = serial.Serial()

    def __init__(self, port):
        self.port = port
        self.s = serial.Serial(port, 9600)

    #encodes the message to a bitstring for the bluetooth module
    def send(self, data):
        self.s.write(str.encode(str(data)))
