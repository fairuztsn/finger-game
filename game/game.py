from player.player import Player
import os

class Game:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.winner = None
    def show_menu(self):
        menu = """
[1] Attack enemy with my 1's hand.
[2] Attack enemy with my 2's hand.
[3] Nah, I'd switch my hand.
"""
        print(menu)

    def start(self):
        turn = 1
        while self.winner is None:
            self.clear_screen()
            self.print_hand_table()
            
            current_turn = 1 if turn%2 != 0 else 2
            current_player = self.player1 if current_turn == 1 else self.player2
            current_enemy = self.player1 if current_turn != 1 else self.player2
            
            self.show_menu()

            choice = int(input(f"Player {current_turn}'s turn. Enter [1/2/3] "))

            if choice != 3:
                isGoingToAttackWithFirstHand = choice == 1
                isGoingToAttackFirstHand = int(input("Enemy hand to attack [1/2]: ")) == 1

                while not current_player.attack(target=current_enemy, attackFirstHand=isGoingToAttackFirstHand, attackWithMyFirstHand=isGoingToAttackWithFirstHand):
                    self.clear_screen()
                    self.print_hand_table()
                    isGoingToAttackWithFirstHand = not isGoingToAttackFirstHand
                    isGoingToAttackFirstHand = int(input("Enemy hand to attack [1/2]: ")) == 1
            else:
                firstHandNewVal = int(input("Enter new value for first hand: "))
                secondHandNewVal = int(input("Enter new value for second hand: "))

                while not current_player.switch(firstHandNewVal=firstHandNewVal, secondHandNewVal=secondHandNewVal):
                    self.clear_screen()
                    print("Bro is trying to do illegal moves 💀")
                    self.print_hand_table()
                    firstHandNewVal = int(input("Enter new value for first hand: "))
                    secondHandNewVal = int(input("Enter new value for second hand: "))
            
            self.checking_win_or_lose_or_continue()
            turn += 1

        print(f"GAME OVER, {self.winner.name} WINS THE GAME")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def checking_win_or_lose_or_continue(self):
        if (self.player1.firstHand, self.player1.secondHand) == (0,5) or (self.player1.firstHand, self.player1.secondHand) == (5,0):
            self.winner = self.player2
        elif (self.player2.firstHand, self.player2.secondHand) == (0,5) or (self.player2.firstHand, self.player2.secondHand) == (5,0):
            self.winner = self.player1
        else:
            self.player1.firstHand = 0 if self.player1.firstHand == 5 else self.player1.firstHand
            self.player1.secondHand = 0 if self.player1.secondHand == 5 else self.player1.secondHand
            self.player2.firstHand = 0 if self.player2.firstHand == 5 else self.player2.firstHand
            self.player2.secondHand = 0 if self.player2.secondHand == 5 else self.player2.secondHand
    
    def print_hand_table(self):
        def print_separator():
            print("+-----------+---------+-----------+---------+")

        def print_row(row_data):
            print(f"| {row_data[0]:^9} | {row_data[1]:^8} | {row_data[2]:^9} | {row_data[3]:^8} |")

        print("+---------------------+---------------------+")
        print("|      Player 1       |       Player 2      |")
        print_separator()
        print("|   First   |  Second |   First   |  Second |")
        print_separator()
        print_row([self.player1.firstHand, self.player1.secondHand, self.player2.firstHand, self.player2.secondHand])
        print_separator()