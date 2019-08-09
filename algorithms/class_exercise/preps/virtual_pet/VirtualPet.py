import Pet
import threading
import time

class VirtualPet:
    # private methods
    def __choosePet(self):
        petType = input("What type of pet would you like? ")
        return petType

    def __enterPetName(self, petType):
        petName = input("What would you like to name your " + petType + "? ")
        return petName

    def __timer(self, secondsPerTick):
        while True:
            # do these in a game tick
            print(self.__pet.getPetName() + "'s stats are")
            print("Hunger: {}%".format(self.__pet.getHunger()))
            print("Bored: {}%".format(self.__pet.getBored()))
            print("Intelligence: {}".format(self.__pet.getIntelligence()))
            print("What would you like to do with your pet? (P)lay, (R)ead or (F)eed? [(Q)uit game]")
            time.sleep(secondsPerTick)
            self.__pet.advanceGameTick()

    def __getCauseOfDeath(self):
        cause = ""
        if self.__pet.getHunger() == 100:
            cause = "starvation"
        if self.__pet.getBored() == 100:
            if cause != "":
                cause = cause + " and " + "boredom"
            else:
                cause = "boredom"
        return cause

    # public methods
    def startGame(self):
        petType = self.__choosePet()
        petName = self.__enterPetName(petType)
        if str.lower(petType) == "tiger":
            self.__pet = Pet.Tiger(petName, petType)
        else:
            self.__pet = Pet.Pet(petName, petType)
        self.__pet.outputGreeting()

    def playGame(self):    
        choice = ""
        gameTickThread = threading.Thread(target=self.__timer, args=(1, ))
        gameTickThread.daemon = True
        gameTickThread.start()
        while choice != "q":
            choice = str.lower(input())
            if not self.__pet.isAlive():
                print("Sorry, {} has died from {}".format(self.__pet.getPetName(), self.__getCauseOfDeath()))
                break
            if choice == "p":
                self.__pet.play()
            elif choice == "f":
                self.__pet.feed()
            elif choice == "r":
                self.__pet.read()
        print("Quitting game, thanks for playing!")

if __name__ == "__main__":
    game = VirtualPet()
    game.startGame()
    game.playGame()
