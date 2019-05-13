"""
Program: craps.py
Author: James Jutt

This module studies and plays the game of craps
"""

from die import Die

class Player(object):
    def __init__(self):
        """Player object will have a pair of dice and an empty rolls list"""
        self.die1 = Die()
        self.die2 = Die()
        self.rolls = []

    def __str__(self):
        """Returns the string rep of the history of rolls."""
        result = ""
        for (v1, v2) in self.rolls:
            result = result + str((v1, v2)) + " " + str(v1 + v2) + "\n"
        return result

    def getNumberOfRolls(self):
        """Returns the number of rolls in one game"""
        return len(self.rolls)

    def play(self):
        """Plays a game, saves the rolls for that game, and returns True for a win and False for a lose"""
        self.rolls = []
        self.die1.roll()
        self.die2.roll()
        
        # Creates a tuple which grabs the values of the two dice that have been rolled 
        (v1, v2) = (self.die1.getValue(), self.die2.getValue())
        self.rolls.append((v1, v2))
        
        # Variable that stores the sum of each die value per roll  
        initialSum = v1 + v2

        # Check to see if the player won or lost on the first rolls
        if initialSum in (2, 3, 12):
            return False
        elif initialSum in (7, 11):
            return True

        # If initial rolls are not a win or loss, continue rolling
        while True:
            self.die1.roll()
            self.die2.roll()
            (v1, v2) = (self.die1.getValue(), self.die2.getValue())
            self.rolls.append((v1, v2))
            laterSum = v1 + v2
            
            if laterSum == 7:
                return False
            elif laterSum == initialSum:
                return True

# Functions that interact with the user to play the games
def playOneGame():
    """Plays a single game and prints the results"""
    player = Player()
    youWin = player.play()
    print(player)
    if youWin:
        print("You win!")
    else: 
        print("You lose")

def playManyGames(number):
    """Plays a number of games and prints statistics"""
    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0
    player = Player()
    for count in range(number):
        hasWon = player.play()
        rolls = player.getNumberOfRolls()
        if hasWon:
            wins += 1
            winRolls += rolls
        else:
            losses += 1
            lossRolls += rolls
    print(f"The total number of wins is {wins}")
    print(f"The total number of losses is {losses}")
    print("The average number of rolls per win is %0.2f" % (winRolls / wins))
    print("The average number of rolls per loss is %0.2f" % (lossRolls / losses))
    print("The winning percentage is %0.3f" % (wins / number))

def main():
    """Plays a number of games and prints statistics"""
    number = int(input("Enter the number of games: "))
    playManyGames(number)

if __name__ == "__main__":
    main()