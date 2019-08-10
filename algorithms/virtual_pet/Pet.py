################################################################################
# Class defintion for Pet
################################################################################
class Pet:
    # constructor
    def __init__(self, name, theType):
        self._petName = name
        self._type = theType
        self._bored = 0
        self._hunger = 0
        self._intelligence = 0

    # public methods
    def feed(self):
        self._hunger = 0
        print("{}'s hunger is now 0%".format(self._petName))

    def play(self):
        self._bored = 0
        print("{}'s bored is now 0%".format(self._petName))

    def read(self):
        if self._intelligence < 150:
            self._intelligence *= 1.006
        print("{}'s intelligence is now {}".format(self._petName, self._intelligence))

    def outputGreeting(self):
        print( "Hello, I'm {}, I'm a {}".format(self._petName, self._type) )

    def advanceGameTick(self):
        self._bored += 1
        self._hunger += 1

################################################################################


################################################################################
# Class defintion for Tiger (Tiger extends Pet)
################################################################################
class Tiger(Pet):
    def __init__(self, name):
        super().__init__(name, "Tiger")
        self._bored = 10
        self._hunger = 50
        self._intelligence = 10

    def outputGreeting(self):
        super().outputGreeting()
        print("I like to eat meat and roar")

################################################################################


##########
# TEST
##########
if __name__ == "__main__":
    aFox = Pet("Reddy", "Fox")
    aFox.outputGreeting()

    aTiger = Tiger("Tora")
    aTiger.outputGreeting()
