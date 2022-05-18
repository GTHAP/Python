class arsenal:
    def __init__(self):
        super().__init__()
        self.weapon1 = "Machine Gun"
        self.weapon2 = "Combat Rifle"
        self.weapon3 = "Sniper Rifle"
        self.weapon4 = "Sidearm"
        self.weapon5 = "Rocket Launcher"
        self.weapon6 = "Grenade"
        self.weapon7 = "Shotgun"
        self.weapon8 = "Submachine Gun"

class marine(arsenal):
    def __init__(self):
        super().__init__()       
    def show_weapons(self):
        return self.weapon2, self.weapon7

class heavy(arsenal):
    def __init__(self):
        super().__init__()
    def show_weapons(self):
        return self.weapon1, self.weapon5

class sniper(arsenal):
    def __init__(self):
        super().__init__()
    def show_weapons(self):
        return self.weapon3, self.weapon8

class support(arsenal):
    def __init__(self):
        super().__init__()
    def show_weapons(self):
        return self.weapon2, self.weapon4

soldier1 = marine()
print(soldier1.show_weapons())
soldier2 = heavy()
print(soldier2.show_weapons())
soldier3 = sniper()
print(soldier3.show_weapons())
soldier4 = support()
print(soldier4.show_weapons())
