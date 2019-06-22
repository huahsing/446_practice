
class debugUtil:
    def __init__(self):
        self.__debugflag = False

    def enableDebug(self):
        self.__debugflag = True

    def disableDebug(self):
       self. __debugflag = False

    def debugPrompt(self, debugString):
        if self.__debugflag:
            print(debugString)
            input("Press \'Enter\' to continue...")