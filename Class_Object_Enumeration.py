import enum
from enum import Enum, unique, auto

class WeaponDamage(Enum):
    CombatRifle = 10
    Pistol = 5
    SniperRifle = 20
    RocketLauncher = 50
    FragmentationGrenade = 30
    LightMachineGun = 10
    CombatKnife = 5
    CombatShotgun = 20

def main():

    print(WeaponDamage.FragmentationGrenade)
    print(type(WeaponDamage.FragmentationGrenade))
    print(repr(WeaponDamage.FragmentationGrenade))

    print (" ")

    print(WeaponDamage.FragmentationGrenade.name, 
    WeaponDamage.FragmentationGrenade.value)

    print(" ")

    myWeaponDamage = {}
    myWeaponDamage[WeaponDamage.CombatShotgun] = "Close Range Spread Shot"
    print(myWeaponDamage[WeaponDamage.CombatShotgun])

if __name__ == "__main__":
    main()

# Created an enumeration class at line 4
# Created class variables and gave them specific values
# Printed out an enumeration type and value from line 16 to 18 
# Printed out the properties of an enumeration
# Created a hash and printed it out from line 27 to 29
# Enumerations are hashable and can be used as a key-value pair
