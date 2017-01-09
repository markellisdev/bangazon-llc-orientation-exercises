from superhero import *
from flight import *
from swimming import *
from sidekick import *
from running import *
from bulletproof import *


class Superman(Superhero, Flying, Running, Swimming, Bulletproof): #inherits from both classes

    def __init__(self):
        Superhero.__init__(self, "Superman")
        Bulletproof.__init__(self) #have to initialize
        self.air_speed = 1000000
        self.water_speed = 250


