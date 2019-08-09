import random

class Car:
    def __init__(self, colour, brand, licenseNum):
        self.Colour = colour
        self.Brand = brand
        self.LicenseNum = licenseNum
        self.Speed = 0
        self.MaxSpeed = 300
    
    def SetColour(self, newColour):
        self.Colour = newColour

    def Accelerate(self):
        if self.Speed < self.MaxSpeed:
            self.Speed += 10

    def Brake(self):
        self.Speed = 0

    def GetSpeed(self):
        return self.Speed

    def PrintSpecs(self):
        print("SPECS: colour={0}, brand={1}, licenseNo={2}, maxSpeed={3}".format(self.Colour, self.Brand, self.LicenseNum, self.MaxSpeed))
    

if __name__ == "__main__":
    # test function
    c1 = Car("red", "BMW", "ZX1234")
    c1.PrintSpecs()

    accelerateCount = random.randint(1, 30)
    
    for i in range(accelerateCount):
        c1.Accelerate()

    print("Current c1 speed =", c1.GetSpeed())
    c1.SetColour("black")
    c1.PrintSpecs()

    
