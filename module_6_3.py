import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed=7):
        self._cord = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if dz < 0:
            print("It's too deep, i can't dive :(")
            return
        self._cord[0] += dx * self.speed
        self._cord[1] += dy * self.speed
        self._cord[2] += dz * self.speed

    def get_cords(self):
        print(f'X:{self._cord[0]}, Y:{self._cord[1]}, Z:{self._cord[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
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
        print(f'Here are(is) {random.randint(1, 4)}, eggs for you')


class AquaticAnimal(Animal):
    def __init__(self, speed=7):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        # self._cord[2] = abs(dz * (self.speed / 2))
        dz = abs(dz)
        diving_speed = self.speed / 2
        self._cord[2] = 0


class PoisonousAnimal(Animal):
    def __init__(self, speed=7):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = 'Click-click-click'

    def __init__(self, speed=7):
        super().__init__(speed)
        Bird.__init__(self, speed)
        AquaticAnimal.__init__(self, speed)
        PoisonousAnimal.__init__(self, speed)


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
