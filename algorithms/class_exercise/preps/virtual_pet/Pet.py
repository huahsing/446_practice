class Pet:
    def __init__(self, petName, petType):
        self.__petName = petName
        self.__hunger = 0
        self.__bored = 0
        self.__intelligence = 0
        self.__type = petType

    def __init__(self, petName, petType, hunger, bored, intelligence):
        self.__petName = petName
        self.__hunger = hunger
        self.__bored = bored
        self.__intelligence = intelligence
        self.__type = petType

    def getPetName(self):
        return self.__petName

    def getPetType(self):
        return self.__type

    def getHunger(self):
        return self.__hunger

    def getBored(self):
        return self.__bored

    def getIntelligence(self):
        return self.__intelligence

    def feed(self):
        self.__hunger = 0
        print("{}'s hunger is now {}%".format(self.getPetName(), self.getHunger()))
    
    def play(self):
        self.__bored = 0
        print("{}'s bored is now {}%".format(self.getPetName(), self.getBored()))

    def read(self):
        self.__intelligence = self.__intelligence * 1.006
        print("{}'s intelligence is now {}".format(self.getPetName(), self.getIntelligence()))

    def advanceGameTick(self):
        self.__bored = self.__bored + 1
        self.__hunger = self.__hunger + 1

    def isAlive(self):
        if self.__bored == 100 or self.__hunger == 100:
            return False
        else:
            return True
        
    def outputGreeting(self):
        print("Hello, I'm {}, I'm a {}".format(self.getPetName(), self.getPetType()))


class Tiger(Pet):
    def __init__(self, petName, petType):
        super().__init__(petName, petType, 50, 10, 10)

    def outputGreeting(self):
        super().outputGreeting()
        print("I like to eat meat and roar")

