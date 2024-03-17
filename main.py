from player.player import Player
from game.game import Game

player1 = Player(name="Player 1")
player2 = Player(name="Player 2")

game = Game(player1=player1, player2=player2)
game.start()