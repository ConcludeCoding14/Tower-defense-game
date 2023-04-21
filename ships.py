class Ship:
    #creat ships! Attributes to consider : health/armor type/armor value/speed/atk?
    def __init__(self,HP,AP,SPD):
        self.hp = HP
        self.AP = AP
        self.SPD = SPD
class Sailer(Ship):
    def __init__(self,HP,AP,SPD,armor_type):
        super().__init__(HP,AP,SPD)
        self.armor_type = armor_type

"""Patrol boat
Gunboat
Missile boat
Minesweeper
Landing craft
Fast attack craft
Hydrofoil
Decently armored:

Light aircraft carrier
Destroyer escort
Landing ship, tank (LST)
Missile cruiser
Mine countermeasures vessel
Heavily armored:

Armored cruiser
Heavy cruiser
Battlecruiser
Dreadnought battleship
Heavy battleship
Super battleship"""
