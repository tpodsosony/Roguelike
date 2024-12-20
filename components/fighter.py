from components.base_component import BaseComponent 

#inherit from BaseComponent
class Fighter(BaseComponent): 
    def __init__(self, hp: int, defense: int, power: int):
        self.max_hp = hp
        self._hp = hp
        self.defense = defense
        self.power = power

    @property # Getter
    def hp(self) -> int:
        return self._hp

    
    @hp.setter #Setter
    def hp(self, value: int) -> None:
        self._hp = max(0, min(value, self.max_hp)) # Insurees HP never goes below 0 or above max_hp

