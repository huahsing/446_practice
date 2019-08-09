import Pet
import threading
import _thread
import time

class VirtualPet:
    # private methods
    def _choosePet(self):
        petType = input("What type of pet would you like? ")
        return petType

    def _enterPetName(self, petType):
        petName = input("What would you like to name your " + petType + "? ")
        return petName

    def _timer(self, secondsPerTick):
        while True:
            # do these in a game tick
            print(self._pet.getPetName() + "'s stats are")
            print("Hunger: {}%".format(self._pet.getHunger()))
            print("Bored: {}%".format(self._pet.getBored()))
            print("Intelligence: {}".format(self._pet.getIntelligence()))
            print("What would you like to do with your pet? (P)lay, (R)ead or (F)eed? [(Q)uit game]\n")
            time.sleep(secondsPerTick)
            self._pet.advanceGameTick()
            if not self._pet.isAlive():
                break
        print("Sorry, {} has died from {}".format(self._pet.getPetName(), self._getCauseOfDeath()))
        print("Press 'Enter'...")
        _thread.interrupt_main()

    def _getCauseOfDeath(self):
        cause = ""
        if self._pet.getHunger() == 100:
            cause = "starvation"
        if self._pet.getBored() == 100:
            if cause != "":
                cause = cause + " and " + "boredom"
            else:
                cause = "boredom"
        return cause

    # public methods
    def startGame(self):
        petType = self._choosePet()
        petName = self._enterPetName(petType)
        if str.lower(petType) == "tiger":
            self._pet = Pet.Tiger(petName, petType)
        else:
            self._pet = Pet.Pet(petName, petType)
        self._pet.outputGreeting()

    def playGame(self):    
        choice = ""
        gameTickThread = threading.Thread(target=self._timer, args=(5, ))
        gameTickThread.daemon = True
        gameTickThread.start()
        while choice != "q":
            try:
                choice = str.lower(input())
            except KeyboardInterrupt:                
                break
            if choice == "p":
                self._pet.play()
            elif choice == "f":
                self._pet.feed()
            elif choice == "r":
                self._pet.read()
        print("Quitting game, thanks for playing!")

if __name__ == "__main__":
    game = VirtualPet()
    game.startGame()
    game.playGame()
