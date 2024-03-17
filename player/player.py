class Player:
    def __init__(self, name: str):
        self.name: str = name
        self.firstHand: int = 1
        self.secondHand: int = 1
    def attack(self, target: "Player", attackFirstHand: bool, attackWithMyFirstHand: bool) -> int:

        if (attackWithMyFirstHand and self.firstHand == 0) or (not attackWithMyFirstHand and self.secondHand == 0):
            return 0
    
        target_hand = target.firstHand if attackFirstHand else target.secondHand
        attack_hand = self.firstHand if attackWithMyFirstHand else self.secondHand

        target_hand += attack_hand
        if target_hand > 5:
            target_hand %= 5

        if attackFirstHand:
            target.firstHand = target_hand
        else:
            target.secondHand = target_hand
        
        return 1

    def switch(self, firstHandNewVal: int, secondHandNewVal: int) -> int:
        if {self.firstHand, self.secondHand} == {0, 1} or (self.firstHand == self.secondHand == firstHandNewVal == secondHandNewVal):
            return 0

        if (self.firstHand == 0 and self.secondHand != 0 and firstHandNewVal != 0 and secondHandNewVal == 0) or \
        (self.firstHand != 0 and self.secondHand == 0 and firstHandNewVal == 0 and secondHandNewVal != 0):
            return 0

        if firstHandNewVal + secondHandNewVal != self.firstHand + self.secondHand:
            return 0

        self.firstHand, self.secondHand = firstHandNewVal, secondHandNewVal

        return 1