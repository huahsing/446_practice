class Pet:
    def __init__(self, petName, petType):
        self._petName = petName
        self._type = petType
        self._hunger = 0
        self._bored = 0
        self._intelligence = 0

    def getPetName(self):
        return self._petName

    def getPetType(self):
        return self._type

    def getHunger(self):
        return self._hunger

    def getBored(self):
        return self._bored

    def getIntelligence(self):
        return self._intelligence

    def feed(self):
        self._hunger = 0
        print("{}'s hunger is now {}%".format(self._petName, self._hunger))
    
    def play(self):
        self._bored = 0
        print("{}'s bored is now {}%".format(self._petName, self._bored))

    def read(self):
        if self._intelligence < 150:
            self._intelligence = self._intelligence * 1.006
        print("{}'s intelligence is now {}".format(self._petName, self._intelligence))

    def advanceGameTick(self):
        self._bored = self._bored + 1
        self._hunger = self._hunger + 1

    def isAlive(self):
        if self._bored == 100 or self._hunger == 100:
            return False
        else:
            return True
        
    def outputGreeting(self):
        print("Hello, I'm {}, I'm a {}".format(self._petName, self._type))


class Tiger(Pet):
    def __init__(self, petName, petType):
        super().__init__(petName, petType)
        self._hunger = 50
        self._bored = 10
        self._intelligence = 10

    def outputGreeting(self):
        super().outputGreeting()
        print("I like to eat meat and roar")

