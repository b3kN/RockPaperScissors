#####################################
#####################################
####    Rock, Paper, Scissors    ####
####    Created By:              ####
####    Nick Bekn Bekeris        ####
#####################################
#####################################

# Imports for random & sys
# Will be used to generate computer choice & exiting app
import random
import sys
import os

# Globals to be used in later functions
global player
global player2
global mode
global rockChoice
global scissorsChoice
global paperChoice
global quitChoice
global win
global lose
global tie
global p2win
global p2lose
global p2tie

rockChoice = "rock"
scissorsChoice = "scissors"
paperChoice = "paper"
quitChoice = "quit"
mp = bool()
win = int()
lose = int()
tie = int()
p2win = int()
p2lose = int()
p2tie = int()
mode = 0

# Intro application class
def intro():
  
  # Print initial message
  print "\nWelcome to the game of rock, paper, scissors!"
  
  # Get and set global for player 1
  global player
  player = raw_input("\nWhat is your name? ")

  # Clear screen
  os.system('cls')
  
  # Propt player 1 for game mode
  print "\nHello " + player
  print "\nPlease make a selection:"
  
  # Get and set game mode type
  game = int(input("\n1) Single Player \n2) Multi-Player \n\nGame Mode: "))
  
  if game == 1:
    global player2
    player2 = "CPU"
    rps()
  elif game == 2:
    global mode
    mode = 1
    mp()

# Main application class
def rps():
    
  # Clear screen
  os.system('cls')

  # Print out instructions
  print "\nPlease enter a number as it correlates with either"
  print "rock, paper, or scissors."

  # Get game mode type and set variables according to whether
  # playing against CPU or player 2
  global mode

  if mode == 1:
    playerChoice    = getPlayerChoice(player)
    player2Choice   = getPlayerChoice(player2)
  elif mode == 0:
    playerChoice    = getPlayerChoice(player)
    player2Choice   = getComputerChoice()

  # Clear screen
  os.system('cls')

  # Run function with choices to get result
  determineWinner(playerChoice,player2Choice)

  # Display results menu and options
  displayResults()

# Multi-player application class
def mp():
  
  # Clear screen
  os.system('cls')
  
  # Get and set player 2 name
  print "\nPlayer 2 has entered the arena!"
  global player2
  player2 = raw_input("\nPlayer 2, what is your name? ")
  
  rps()
  
# Computer choice is random int(1,3) assgined to either R P S
def getComputerChoice():
  
  # Random int for computer
  choice = random.randint(1,3)

  # Set number to string according to result
  if choice == 1:
      choice = "rock"
  elif choice == 2:
      choice = "paper"
  elif choice == 3:
      choice = "scissors"

  return choice

# Player choice is determined to users selection
def getPlayerChoice(name):

  # Clear screen
  os.system('cls')
  
  # Use name given in function to advise player selection
  print "\n" + name + ", it's your turn!"
    
  # Input to have user select an option
  choice = int(input("\n1) Rock \n2) Paper \n3) Scissors \n\nSelect One: "))

  # Set number to string according to result
  if choice == 1:
    choice = "rock"
  elif choice == 2:
    choice = "paper"
  elif choice == 3:
    choice = "scissors"
  else:

    os.system('cls')

    # If selection is invalid, make them choose different selection
    print "\nInvaild Selection"
    print "Please enter a valid number!"

    # Run function again to get players choice
    # This will loop each time they choose an invalid selection
    getPlayerChoice()

  return choice

def determineWinner(playerChoice,computerChoice):
  
  # Print out the selections made by both
  print "\n" + player + " chose", playerChoice
  print player2 + " chose", computerChoice
  
  global win
  global p2win
  global lose
  global p2lose
  global tie
  global p2tie
  
  # Based on variables, compare choices and determin winner
  if playerChoice == computerChoice:
    tie += 1
    p2tie += 1
    print "\nIt's a tie!"
  elif playerChoice == rockChoice and computerChoice == scissorsChoice:
    win += 1
    p2lose += 1
    print "\n" + player + " wins! Rock beats scissors."
  elif playerChoice == rockChoice and computerChoice == paperChoice:
    lose += 1
    p2win += 1
    print "\n" + player2 + " wins! Paper beats rock."
  elif playerChoice == scissorsChoice and computerChoice == paperChoice:
    win += 1
    p2lose += 1
    print "\n" + player + " wins! Scissors beats paper."
  elif playerChoice == scissorsChoice and computerChoice == rockChoice:
    lose += 1
    p2win += 1
    print "\n" + player2 + " wins! Rock beats scissors."
  elif playerChoice == paperChoice and computerChoice == rockChoice:
    win += 1
    p2lose += 1
    print "\n" + player + " wins! Paper beats rock."
  elif playerChoice == paperChoice and computerChoice == scissorsChoice:
    lose += 1
    p2win += 1
    print "\n" + player2 + " wins! Scissors beats paper."
  elif playerChoice == quitChoice:
    sys.exit("\nExiting Program")
    return

def displayResults():
  
  global mode
  global player2
  global win
  global p2win
  global lose
  global p2lose
  global tie
  global p2tie
    
  # Print out options for selection in menu
  print "\n    MENU\n"
  print player + " VS " + player2
  print "\n1) Wins"
  print "2) Losses"
  print "3) Ties"
  print "4) Play again"
  print "5) Switch game mode"
  print "6) Quit"

  # Input for user to make a selection
  playerChoice = int(input("\nEnter your choice: "))

  # Display results of user's selection, play again, or quit
  if playerChoice == 1:
    os.system('cls')
    print "\n" + player + " total wins are " + str(win) + "."
    print "\n" + player2 + " total wins are " + str(p2win) + "."
    displayResults()
  elif playerChoice == 2:
    os.system('cls')
    print "\n" + player + " total wins are " + str(lose) + "."
    print "\n" + player2 + " total wins are " + str(p2lose) + "."
    displayResults()
  elif playerChoice == 3:
    os.system('cls')
    print "\n" + player + " total wins are " + str(tie) + "."
    print "\n" + player2 + " total wins are " + str(p2tie) + "."
    displayResults()
  elif playerChoice == 4:
    rps()
  elif playerChoice == 5:    
    win = 0
    p2win = 0
    lose = 0
    p2lose = 0
    tie = 0
    p2tie = 0
    
    if mode == 0:
      mode = 1
      mp()
    elif mode == 1:
      mode = 0
      player2 = "CPU"
      rps()
  elif playerChoice == 6:
    sys.exit("\nExiting Program")
  else:
    os.system('cls')
    print "\nInvalid Selection"
    displayResults()
    
intro()
input("\nPress ENTER to continue...")