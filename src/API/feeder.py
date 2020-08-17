import machine

from src.API.led import Led
from src.API.pump import Pump
from src.API.sensor import Sensor


class Feeder(Sensor, Pump, Led):

    def __init__(self, pin1, pin2, pin3, pin4, nummes):
        Sensor.__init__(pin1, nummes)
        Pump.__init__(pin2, pin3)
        Led.__init__(pin4)
        self.bvd = 0


    def algaeMeasure(self):
        # k is the number of rotations

        self.measure()
        self.backward()
        self.rotation()

    def feed(self, value):
        self.forward()
        self.rotation(value)
