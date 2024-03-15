import os

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

player1 = Player(name="Brian")
player2 = Player(name="Jonathan")
winner = None

def print_hand_table():
    global player1, player2
    def print_separator():
        print("+-----------+---------+-----------+---------+")

    def print_row(row_data):
        print(f"| {row_data[0]:^9} | {row_data[1]:^8} | {row_data[2]:^9} | {row_data[3]:^8} |")

    print("+---------------------+---------------------+")
    print("|      Player 1       |       Player 2      |")
    print_separator()
    print("|   First   |  Second |   First   |  Second |")
    print_separator()
    print_row([player1.firstHand, player1.secondHand, player2.firstHand, player2.secondHand])
    print_separator()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def checking_win_or_lose_or_continue():
    global winner
    if (player1.firstHand, player1.secondHand) == (0,5) or (player1.firstHand, player1.secondHand) == (5,0):
        winner = player2
    elif (player2.firstHand, player2.secondHand) == (0,5) or (player2.firstHand, player2.secondHand) == (5,0):
        winner = player1
    else:
        player1.firstHand = 0 if player1.firstHand == 5 else player1.firstHand
        player1.secondHand = 0 if player1.secondHand == 5 else player1.secondHand
        player2.firstHand = 0 if player2.firstHand == 5 else player2.firstHand
        player2.secondHand = 0 if player2.secondHand == 5 else player2.secondHand

def main():
    global winner
    turn = 1
    menu = """
[1] Attack enemy with my 1's hand.
[2] Attack enemy with my 2's hand.
[3] Nah, I'd switch my hand.
"""
    while winner is None:
        clear_screen()
        print_hand_table()
        
        current_turn = 1 if turn%2 != 0 else 2
        current_player = player1 if current_turn == 1 else player2
        current_enemy = player1 if current_turn != 1 else player2
        
        print(menu)

        choice = int(input(f"Player {current_turn}'s turn. Enter [1/2/3] "))

        if choice != 3:
            isGoingToAttackWithFirstHand = choice == 1
            isGoingToAttackFirstHand = int(input("Enemy hand to attack [1/2]: ")) == 1

            while not current_player.attack(target=current_enemy, attackFirstHand=isGoingToAttackFirstHand, attackWithMyFirstHand=isGoingToAttackWithFirstHand):
                clear_screen()
                print_hand_table()
                isGoingToAttackWithFirstHand = not isGoingToAttackFirstHand
                isGoingToAttackFirstHand = int(input("Enemy hand to attack [1/2]: ")) == 1
        else:
            firstHandNewVal = int(input("Enter new value for first hand: "))
            secondHandNewVal = int(input("Enter new value for second hand: "))

            while not current_player.switch(firstHandNewVal=firstHandNewVal, secondHandNewVal=secondHandNewVal):
                clear_screen()
                print("Bro is trying to do illegal moves 💀")
                print_hand_table()
                firstHandNewVal = int(input("Enter new value for first hand: "))
                secondHandNewVal = int(input("Enter new value for second hand: "))
        
        checking_win_or_lose_or_continue()
        turn += 1

    print(f"GAME OVER, {winner.name} WINS THE GAME")

if __name__ == "__main__":
    main()