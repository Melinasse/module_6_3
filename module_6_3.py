import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed=7):
        self._cords = [0, 0, 0]
        self.speed = speed


    def move(self, dx, dy, dz):
        new_dz = self._cords[2] + dz * self.speed
        if new_dz < 0:
            print("It's too deep, i can't dive :(")
            return
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] = new_dz



    def get_cords(self):
        print(f'X:{self._cords[0]}, Y:{self._cords[1]}, Z:{self._cords[2]}')

    def attack(self):
        danger = max(self._DEGREE_OF_DANGER, AquaticAnimal._DEGREE_OF_DANGER, PoisonousAnimal._DEGREE_OF_DANGER)
        if danger < 5:
            print("Sorry i'm peaceful:)")
        else:
            print("Be careful, a'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    def __init__(self, speed=7):
        super().__init__(speed)
        self.beak = True

    def lay_eggs(self):
        print(f'Here are(is) {random.randint(1, 4)} eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed=7):
        super().__init__(speed)

    def dive_in(self, dz):
        # diving_speed = self.speed / 2
        # self._cords[2] -= abs(dz) * (self.speed / 2)
        self.move(0, 0, -abs(dz) / 2)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

    def __init__(self, speed=7):
        super().__init__(speed)



class Duckbill(AquaticAnimal, Bird, PoisonousAnimal):
    sound = 'Click-click-click'
    def __init__(self, speed=7):
        super().__init__(speed)

print(Duckbill.mro())


db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
