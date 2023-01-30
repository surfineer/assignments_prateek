from getpass import getpass as input

counter_p1=0
counter_p2=0

while True:
  print()
  print("E P I C    ROCK / PAPER / SCISSORS    B A T T L E ")
  print()
  print("Select your move (R, P or S)")
  print()
  
  player1Move = input("Player 1 > ")
  print()
  player2Move = input("Player 2 > ")
  print()
    
  if player1Move=="R":
    if player2Move=="R":
      print("You both picked Rock, draw!")
      continue
      
    elif player2Move=="S":
      print("Player1 smashed Player2's Scissors into dust with their Rock!")
      counter_p1 +=1
      if counter_p1 == 3: 
        print ("Player1 has won the game!")
        break
      continue
      
    elif player2Move=="P":
      print("Player1's Rock is smothered by Player2's Paper!")
      counter_p2 +=1
      if counter_p2 == 3: 
        print ("Player2 has won the Game!")
        break
    else:
      print("Invalid Move Player 2!")
      continue
      
  elif player1Move=="P":
    if player2Move=="R":
      print("Player2's Rock is smothered by Player1's Paper!")
      counter_p1 +=1
      if counter_p1 == 3: 
        print ("Player1 has won the game!")
        break
      continue
      
    elif player2Move=="S":
      print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
      counter_p2 +=1
      if counter_p2 == 3: 
        print ("Player2 has won the Game!")
        break
      continue
      
    elif player2Move=="P":
      print("Two bits of paper flap at each other. Dissapointing. Draw.")
      continue
      
    else:
      print("Invalid Move Player 2!")
      
  elif player1Move=="S":
    if player2Move=="R":
      print("Player 2's Rock makes metal-dust out of Player1's Scissors")
      counter_p2 +=1
      if counter_p2 == 3: 
        print ("Player2 has won the Game!")
        break
      continue
      
    elif player2Move=="S":
      print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
      continue
      
    elif player2Move=="P":
      print("Player1's Scissors make confetti out of Player2's paper!")
      counter_p1 +=1
      if counter_p1 == 3: 
        print ("Player1 has won the game!")
        break
      continue
    else:
      print("Invalid Move Player 2!")
  else:
    print("Invalid Move Player 1!")


print("Thanks for playing!")
exit()