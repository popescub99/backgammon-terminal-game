import random

class Board:
  # The board is represented as a string with the following format, accordingly to the player's side:
  
  # Board for player 1:
  player1_board = '''
 12 11 10  9  8  7     6  5  4  3  2  1
 ()          {}       {}             ()
 ()          {}       {}             ()
 ()          {}       {}               
 ()                   {}               
 ()                   {}               

 {}                   ()               
 {}                   ()               
 {}          ()       ()               
 {}          ()       ()             {}
 {}          ()       ()             {}
 13 14 15 16 17 18    19 20 21 22 23 24
'''
  player1_board_list = list(player1_board)  # Convert the board string to a list of characters

  # Board for player 2:
  player2_board = '''
 13 14 15 16 17 18    19 20 21 22 23 24
 ()          {}       {}             ()
 ()          {}       {}             ()
 ()          {}       {}               
 ()                   {}               
 ()                   {}               

 {}                   ()               
 {}                   ()               
 {}          ()       ()               
 {}          ()       ()             {}
 {}          ()       ()             {}
 12 11 10  9  8  7     6  5  4  3  2  1
'''
  player2_board_list = list(player2_board)  # Convert the board string to a list of characters

  # The board_map dictionary maps each point on the board to its corresponding coordinates in the string representation.
  # The keys are the point numbers (1-24) and the values are lists of coordinates in the format [x, y] representing a checker for each pair of ['(',')'] and ['{','}'] or empty space for [' ', ' '].

  board_map = {'p1': {5: [238, 239], 4: [198, 199], 3: [158, 159], 2: [118, 119], 1: [78, 79]}, 'p2': {5: [236, 237], 4: [196, 197], 3: [156, 157], 2: [116, 117], 1: [76, 77]}, 'p3': {5: [234, 235], 4: [194, 195], 3: [154, 155], 2: [114, 115], 1: [74, 75]}, 'p4': {5: [232, 233], 4: [192, 193], 3: [152, 153], 2: [112, 113], 1: [72, 73]}, 'p5': {5: [230, 231], 4: [190, 191], 3: [150, 151], 2: [110, 111], 1: [70, 71]}, 'p6': {5: [228, 229], 4: [188, 189], 3: [148, 149], 2: [108, 109], 1: [68, 69]}, 'p7': {5: [226, 227], 4: [186, 187], 3: [146, 147], 2: [106, 107], 1: [66, 67]}, 'p8': {5: [224, 225], 4: [184, 185], 3: [144, 145], 2: [104, 105], 1: [64, 65]}, 'p9': {5: [222, 223], 4: [182, 183], 3: [142, 143], 2: [102, 103], 1: [62, 63]}, 'p10': {5: [220, 221], 4: [180, 181], 3: [140, 141], 2: [100, 101], 1: [60, 61]}, 'p11': {5: [218, 219], 4: [178, 179], 3: [138, 139], 2: [98, 99], 1: [58, 59]}, 'p12': {5: [216, 217], 4: [176, 177], 3: [136, 137], 2: [96, 97], 1: [56, 57]}, 'p13': {5: [243, 244], 4: [283, 284], 3: [323, 324], 2: [363, 364], 1: [403, 404]}, 'p14': {5: [245,246], 4: [285,286], 3: [325,326], 2: [365, 366], 1: [405,406]}, 'p15': {5: [248, 249], 4: [288, 289], 3: [328, 329], 2: [368, 369], 1: [408, 409]}, 'p16': {5: [251, 252], 4: [291, 292], 3: [331, 332], 2: [371, 372], 1: [411,412]}, 'p17': {5: [254,255], 4: [294, 295], 3: [334, 335], 2: [374, 375], 1: [414, 415]}, 'p18': {5: [257, 258], 4: [297,298], 3: [337, 338], 2: [377, 378], 1: [417, 418]}, 'p19': {5: [264, 265], 4: [304, 305], 3: [344, 345], 2: [384, 385], 1: [424, 425]}, 'p20': {5: [267, 268], 4: [307,308], 3: [347,348], 2: [387,388], 1: [427,428]}, 'p21': {5: [270, 271], 4: [310, 311], 3: [350, 351], 2: [390, 391], 1: [430, 431]}, 'p22': {5: [273, 274], 4: [313, 314], 3: [353, 354], 2: [393, 394], 1: [433, 434]}, 'p23': {5: [276, 277], 4: [316, 317], 3: [356, 357], 2: [396, 397], 1: [436, 437]}, 'p24': {5: [279, 280], 4: [319, 320], 3: [359, 360], 2: [399, 400], 1: [439, 440]}}

  # The player1_checkers_count and player2_checkers_count dictionaries store the number of checkers for each player on each point using the same order as displayed in player1's board.

  player1_checkers_count = {'p1': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p2': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p3': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p4': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p5': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p6': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 1, 4: 1, 3: 1, 2: 1, 1: 1}, 'p7': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p8': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 1, 2: 1, 1: 1}, 'p9': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p10': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p11': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p12': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p13': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 1, 4: 1, 3: 1, 2: 1, 1: 1}, 'p14': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p15': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p16': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p17': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p18': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p19': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p20': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p21': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p22': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p23': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p24': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 1, 1: 1}}

  player2_checkers_count = {'p1': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 1, 1: 1}, 'p2': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p3': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p4': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p5': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p6': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p7': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p8': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p9': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p10': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p11': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p12': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 1, 4: 1, 3: 1, 2: 1, 1: 1}, 'p13': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p14': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p15': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p16': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p17': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 1, 2: 1, 1: 1}, 'p18': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p19': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 1, 4: 1, 3: 1, 2: 1, 1: 1}, 'p20': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p21': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p22': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p23': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 'p24': {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}}

  def __init__(self):
    self.board = '''
 xx xx xx xx xx xx    xx xx xx xx xx xx
 ()          {}       {}             ()
 ()          {}       {}             ()
 ()          {}       {}               
 ()                   {}               
 ()                   {}               

 {}                   ()               
 {}                   ()               
 {}          ()       ()               
 {}          ()       ()             {}
 {}          ()       ()             {}
 xx xx xx xx xx xx    xx xx xx xx xx xx
'''

  def __repr__(self):
    return "This is a backgammon board"
  
class Player1:
  def __init__(self, name):
    self.board = Board.player1_board # Player's board
    self.name = name # Player's name
    self.checkers = 15  # Number of checkers
    self.home = 5  # Number of checkers in home
    self.bar = 0  # Number of checkers on the bar
    self.winner = False  # Flag for winning
    self.turn = False  # Flag for player's turn
 
  def __repr__(self):
    return "This is a backgammon player on the upper side of the board."
  
  def check_position(self, selection):
    # Check in the checkers count dictionary on what position the last checker is on the selected point
    k = 'p'+ str(selection) 
    counter = 0
    i = 1
    while Board.player1_checkers_count[k][i] != 0:
      counter += 1
      i += 1
    return counter

  def check_bar(self, dice1, dice2):
    #Check if the player has checkers on the bar, if so, check if the player can enter the board
    entry_points = [24, 23, 22, 21, 20, 19]
    while self.bar > 0 and (dice1 != 0 or dice2 != 0):
      print("You have", self.bar, "checkers on the bar.")
      i = 'p' + str(entry_points[dice1-1])
      j = 'p' + str(entry_points[dice2-1])
      #Check if the entry point is empty or occupied by the player's own checkers
      if Board.player2_checkers_count[i][1] == 0 or (Board.player2_checkers_count[i][1] == 1 and Board.player2_checkers_count[i][2] == 0) or Board.player1_checkers_count[i][1] == 1:
        print("You can enter the board on the point", entry_points[dice1-1])
        selection1 = entry_points[dice1-1]
      else:
        print("You cannot enter the board on the point", entry_points[dice1-1])
        selection1 = 0
        dice1 = 0
      if Board.player2_checkers_count[j][1] == 0 or (Board.player2_checkers_count[j][1] == 1 and Board.player2_checkers_count[j][2] == 0) or Board.player1_checkers_count[j][1] == 1:
        print("You can enter the board on the point", entry_points[dice2-1])
        selection2 = entry_points[dice2-1]
      else:
        print("You cannot enter the board on the point", entry_points[dice2-1])
        selection2 = 0
        dice2 = 0
        
      if (Board.player2_checkers_count[i][1] == 1 and Board.player2_checkers_count[i][2] == 1) and (Board.player2_checkers_count[j][1] == 1 and Board.player2_checkers_count[j][2] == 1):
        print("You cannot enter the board this turn, please wait for your next turn.")
        self.turn = False
        dice1 = 0
        dice2 = 0
        break
      else:
        while True:
          try:
            choice = int(input("Choose where to enter the board: "))
          except ValueError:
            print("Invalid input. Please enter a number.")
            continue
          if choice == selection1:
            break
          elif choice == selection2:
            break
          else: 
            print("Invalid choice. Please choose a valid entry point.")
            continue
            
        entry_position = self.check_position(choice) + 1
        if entry_position > 5:
          Board.player1_checkers_count['p' + str(choice)][entry_position] = 1
          self.bar -= 1
        else:  
          x = Board.board_map['p' + str(choice)][entry_position][0]
          y = Board.board_map['p' + str(choice)][entry_position][1]
          Board.player1_board_list[x] = '{'
          Board.player1_board_list[y] = '}'
          Board.player2_board_list[x] = '{'
          Board.player2_board_list[y] = '}'
          Board.player1_board = ''.join(Board.player1_board_list)
          Board.player2_board = ''.join(Board.player2_board_list)
          Board.player1_checkers_count['p' + str(choice)][entry_position] = 1
          self.bar -= 1
    else:
      print("You have no checkers on the bar.")
      pass

  def check_start(self, dice1, dice2):
    while True:
      selection = 0
      start_position = 0
      while selection not in range(1, 25):
        try:
          selection = int(input("Choose a checker to move: "))
        except ValueError:
          print("Invalid input. Please enter a number.")
          continue      
      k = 'p'+ str(selection)
      i = 'p' + str(selection - dice1)
      j = 'p' + str(selection - dice2)
      if Board.player1_checkers_count[k][1] == 1:
        if (Board.player1_checkers_count[i][1] == 1) or (Board.player1_checkers_count[j][1] == 1) or (Board.player1_checkers_count[i][1] == 0 and Board.player2_checkers_count[i][1] == 0) or (Board.player1_checkers_count[j][1] == 0 and Board.player2_checkers_count[j][1] == 0) or (Board.player2_checkers_count[i][1] == 1 and Board.player2_checkers_count[i][2] == 0) or (Board.player2_checkers_count[j][1] == 1 and Board.player2_checkers_count[j][2] == 0):
          start_position = self.check_position(selection)
          break
        else:  
            print("The selection is not a valid choice.")
      else:
          print("You do not have a checker on the selected point.")
    return start_position, selection, dice1, dice2
  
  def check_stop(self, dice1, dice2, start_selection):
    while dice1 != 0 or dice2 != 0:
      selection = 0
      stop_position = 0
      while selection not in range(1, 25):
        try:
          selection = int(input("Choose where to move the selected checker: "))
        except ValueError:
          print("Invalid input. Please enter a number.")
          continue      
      k = 'p'+ str(selection)
      if selection == start_selection - dice1 or selection == start_selection - dice2:
        if (Board.player1_checkers_count[k][1] == 1) or (Board.player1_checkers_count[k][1] == 0 and Board.player1_checkers_count[k][1] == 0):
          stop_position = self.check_position(selection) + 1
          if selection == start_selection - dice1:
            dice1 = 0
            break
          elif selection == start_selection - dice2:
            dice2 = 0
            break
        elif (Board.player2_checkers_count[k][1] == 1 and Board.player2_checkers_count[k][2] == 0):
          stop_position = self.check_position(selection)
          if selection == start_selection - dice1:
            dice1 = 0
            break
          elif selection == start_selection - dice2:
            dice2 = 0
            break
      else:  
        print("The selection is not a valid choice.")
    return stop_position, selection, dice1, dice2
  
  def move(self, start, stop, start_position, stop_position):
    # Move the checker from start_position to stop_position
    # Update the board and checkers count
    Board.player1_checkers_count['p' + str(start)][start_position] = 0
    if start_position <= 5:
      m = Board.board_map['p' + str(start)][start_position][0]
      n = Board.board_map['p' + str(start)][start_position][1]
      Board.player1_board_list[m] = ' '
      Board.player1_board_list[n] = ' '
      Board.player2_board_list[m] = ' '
      Board.player2_board_list[n] = ' '
      if stop_position < 5:
        x = Board.board_map['p' + str(stop)][stop_position][0]
        y = Board.board_map['p' + str(stop)][stop_position][1]
        if Board.player2_checkers_count['p' + str(stop)][stop_position] == 1:
          Board.player1_board_list[x] = '{'
          Board.player1_board_list[y] = '}'
          Board.player2_board_list[x] = '{'
          Board.player2_board_list[y] = '}'
          Board.player1_board = ''.join(Board.player1_board_list)
          Board.player2_board = ''.join(Board.player2_board_list)
          Board.player1_checkers_count['p' + str(stop)][stop_position] = 1
          Board.player2_checkers_count['p' + str(stop)][stop_position] = 0
        else:
          Board.player1_board_list[x] = '{'
          Board.player1_board_list[y] = '}'
          Board.player2_board_list[x] = '{'
          Board.player2_board_list[y] = '}'
          Board.player1_board = ''.join(Board.player1_board_list)
          Board.player2_board = ''.join(Board.player2_board_list)
          Board.player1_checkers_count['p' + str(stop)][stop_position] = 1
      else:
        Board.player1_checkers_count['p' + str(stop)][stop_position] = 1
 
  def check_home(self):
    # Check if the player has moved all checkers to the home board
    counter = 0
    for i in range(19, 25):
      k = 'p' + str(i)
      j = 1
      while Board.player1_checkers_count[k][j] == 1:
        counter += 1
        j += 1
    if counter == 15:
      print("You have moved all your checkers to the home board. You can start bearing off.")
    return counter
  
  def bear_off(self, dice1, dice2):
    #Check if the player can bear off
    if self.check_home() == 15:
      while dice1 != 0 or dice2 != 0:
        while selection not in range(1, 7):
          try:
            selection = int(input("Choose a checker to bear off: "))
          except ValueError:
            print("Invalid input. Please enter a number.")
            continue
          if Board.player1_checkers_count['p' + str(selection)][1] != 0:
            print("You do not have a checker on the selected point. Please select a valid point.")
            continue
          else:
            break
        try:
          dice_selection = int(input("Choose a dice to use for moving the checker: "))
        except ValueError:
          print("Invalid input. Please enter a number.")
          continue
        if dice_selection != dice1 or dice_selection != dice2:
          print("You cannot use this dice to bear off. Please select a valid dice.")
          continue
        if dice_selection == dice1:
          dice1 = 0
        elif dice_selection == dice2:
          dice2 = 0
        if selection - dice_selection <= 0:
          selected_checker = self.check_position(selection)
          Board.player1_checkers_count['p' + str(selection)][selected_checker] = 0
          Board.player1_board_list[Board.board_map['p' + str(selection)][selected_checker][0]] = ' '
          Board.player1_board_list[Board.board_map['p' + str(selection)][selected_checker][1]] = ' '
          Board.player2_board_list[Board.board_map['p' + str(selection)][selected_checker][0]] = ' '
          Board.player2_board_list[Board.board_map['p' + str(selection)][selected_checker][1]] = ' '
          Board.player1_board = ''.join(Board.player1_board_list)
          Board.player2_board = ''.join(Board.player2_board_list)
          self.checkers -= 1
          if self.checkers == 0:
            print("You have borne off all your checkers. You win!")
            self.winner = True
        else:
          start_position = self.check_position(selection)
          stop_position = self.check_position(selection - dice_selection)
          self.move(selection, selection - dice_selection, start_position, stop_position)  

class Player2:
  def __init__(self, name):
    self.board = Board.player2_board # Player's board
    self.name = name # Player's name
    self.checkers = 15  # Number of checkers
    self.home = 5  # Number of checkers in home
    self.bar = 0  # Number of checkers on the bar
    self.winner = False  # Flag for winning
    self.turn = False  # Flag for player's turn
 
  def __repr__(self):
    return "This is a backgammon player on the down side of the board."
  
  def check_position(self, selection):
    # Check in the checkers count dictionary on what position the last checker is on the selected point
    k = 'p'+ str(selection) 
    counter = 0
    i = 1
    while Board.player2_checkers_count[k][i] != 0:
      counter += 1
      i += 1
    return counter
    
  def check_bar(self, dice1, dice2):
    #Check if the player has checkers on the bar
    while self.bar > 0 and (dice1 != 0 or dice2 != 0):
      print("You have", self.bar, "checkers on the bar.")
      i = 'p' + str(dice1)
      j = 'p' + str(dice2)
      #Check if the entry point is empty or occupied by the player's own checkers
      if Board.player1_checkers_count[i][1] == 0 or (Board.player1_checkers_count[i][1] == 1 and Board.player1_checkers_count[i][2] == 0) or Board.player2_checkers_count[i][1] == 1:
        print("You can enter the board on the point", (25 - dice1))
        selection1 = (25 - dice1)
      else:
        print("You cannot enter the board on the point", (25 - dice1))
        selection1 = 0
      if Board.player1_checkers_count[j][1] == 0 or (Board.player1_checkers_count[j][1] == 1 and Board.player1_checkers_count[j][2] == 0) or Board.player2_checkers_count[j][1] == 1:
        print("You can enter the board on the point", (25 - dice2))
        selection2 = 25 - dice2
      else:
        print("You cannot enter the board on the point", (25 - dice2))
        selection2 = 0
        
      if (Board.player1_checkers_count[i][1] == 1 and Board.player1_checkers_count[i][2] == 1) and (Board.player1_checkers_count[j][1] == 1 and Board.player1_checkers_count[j][2] == 1):
        print("You cannot enter the board this turn, please wait for your next turn.")
        self.turn = False
        dice1 = 0
        dice2 = 0
        break
      else:
        while True:
          try:
            choice = int(input("Choose where to enter the board: "))
          except ValueError:
            print("Invalid input. Please enter a number.")
            continue
          if choice == (25 - selection1):
            break
          elif choice == (25 - selection2):
            break
          else: 
            print("Invalid choice. Please choose a valid entry point.")
            continue
            
        entry_position = self.check_position(choice) + 1
        if entry_position > 5:
          Board.player2_checkers_count['p' + str(choice)][entry_position] = 1
          self.bar -= 1
        else:  
          x = Board.board_map['p' + str(choice)][entry_position][0]
          y = Board.board_map['p' + str(choice)][entry_position][1]
          Board.player1_board_list[x] = '('
          Board.player1_board_list[y] = ')'
          Board.player2_board_list[x] = '('
          Board.player2_board_list[y] = ')'
          Board.player1_board = ''.join(Board.player1_board_list)
          Board.player2_board = ''.join(Board.player2_board_list)
          Board.player2_checkers_count['p' + str(choice)][entry_position] = 1
          self.bar -= 1
    if self.bar == 0:
      print("You have no checkers on the bar.")

  def check_start(self, dice1, dice2):
    while True:
      selection = 0
      start_position = 0
      # Get the starting position from the player
      while selection not in range(1, 25):
        try:
          selection = int(input("Choose a checker to move: "))
        except ValueError:
          print("Invalid input. Please enter a number.")
          continue      
      k = 'p'+ str(25 - selection)
      i = 'p' + str((25 - selection) + dice1)
      j = 'p' + str((25 - selection) + dice2)
      if Board.player2_checkers_count[k][1] == 1:
        if (Board.player2_checkers_count[i][1] == 1) or (Board.player2_checkers_count[j][1] == 1) or (Board.player2_checkers_count[i][1] == 0 and Board.player1_checkers_count[i][1] == 0) or (Board.player2_checkers_count[j][1] == 0 and Board.player1_checkers_count[j][1] == 0) or (Board.player1_checkers_count[i][1] == 1 and Board.player1_checkers_count[i][2] == 0) or (Board.player1_checkers_count[j][1] == 1 and Board.player1_checkers_count[j][2] == 0):
          start_position = self.check_position(25 - selection)
          break
        else:  
            print("The selection is not a valid choice.")
      else:
          print("You do not have a checker on the selected point.")
    return start_position, selection, dice1, dice2
  
  def check_stop(self, dice1, dice2, start_selection):
    while dice1 != 0 or dice2 != 0:
      selection = 0
      stop_position = 0
      # Get the stopping position from the player
      while selection not in range(1, 25):
        try:
          selection = int(input("Choose where to move the selected checker: "))
        except ValueError:
          print("Invalid input. Please enter a number.")
          continue      
      k = 'p'+ str(25 - selection)
      if (25 - selection) == (25 - start_selection) + dice1 or (25 - selection) == (25 - start_selection) + dice2:
        if (Board.player2_checkers_count[k][1] == 1) or (Board.player1_checkers_count[k][1] == 0 and Board.player2_checkers_count[k][1] == 0):
          stop_position = self.check_position(25 - selection) + 1
          if (25 - selection) == (25 - start_selection) + dice1:
            dice1 = 0
            break
          elif (25 - selection) == (25 - start_selection) + dice2:
            dice2 = 0
            break   
        elif (Board.player1_checkers_count[k][1] == 1 and Board.player1_checkers_count[k][2] == 0):
          stop_position = self.check_position(25 - selection)
          if (25 - selection) == (25 - start_selection) + dice1:
            dice1 = 0
            break
          elif (25 - selection) == (25 - start_selection) + dice2:
            dice2 = 0
            break
      else:  
        print("The selection is not a valid choice.")
    return stop_position, selection, dice1, dice2
  
  def move(self, start, stop, start_position, stop_position):
    # Move the checker from start_position to stop_position
    # Update the board and checkers count
    Board.player1_checkers_count['p' + str(25 - start)][start_position] = 0
    if start_position <= 5:
      m = Board.board_map['p' + str(25 - start)][start_position][0]
      n = Board.board_map['p' + str(25 - start)][start_position][1]
      Board.player1_board_list[m] = ' '
      Board.player1_board_list[n] = ' '
      Board.player2_board_list[m] = ' '
      Board.player2_board_list[n] = ' '
      if stop_position < 5:
        x = Board.board_map['p' + str(25 - stop)][stop_position][0]
        y = Board.board_map['p' + str(25 - stop)][stop_position][1]
        if Board.player2_checkers_count['p' + str(25 - stop)][stop_position] == 1:
          Board.player1_board_list[x] = '('
          Board.player1_board_list[y] = ')'
          Board.player2_board_list[x] = '('
          Board.player2_board_list[y] = ')'
          Board.player1_board = ''.join(Board.player1_board_list)
          Board.player2_board = ''.join(Board.player2_board_list)
          Board.player1_checkers_count['p' + str(25 - stop)][stop_position] = 1
          Board.player2_checkers_count['p' + str(25 - stop)][stop_position] = 0
        else:
          Board.player1_board_list[x] = '('
          Board.player1_board_list[y] = ')'
          Board.player2_board_list[x] = '('
          Board.player2_board_list[y] = ')'
          Board.player1_board = ''.join(Board.player1_board_list)
          Board.player2_board = ''.join(Board.player2_board_list)
          Board.player2_checkers_count['p' + str(25 - stop)][stop_position] = 1
      else:
        Board.player2_checkers_count['p' + str(25 - stop)][stop_position] = 1
 
  def check_home(self):
    # Check if the player has moved all checkers to the home board
    counter = 0
    for i in range(1, 7):
      k = 'p' + str(i)
      j = 1
      while Board.player1_checkers_count[k][j] == 1:
        counter += 1
        j += 1
    self.home = counter
    if self.home == 15:
      print("You have moved all your checkers to the home board. You can start bearing off.")
    return counter
  
  def bear_off(self, dice1, dice2):
    #Check if the player can bear off
    if self.check_home() == 15:
      while dice1 != 0 or dice2 != 0:
        while selection not in range(1, 7):
          try:
            selection = int(input("Choose a checker to bear off: "))
          except ValueError:
            print("Invalid input. Please enter a number.")
            continue
          if Board.player2_checkers_count['p' + str(25 - selection)][1] != 0:
            print("You do not have a checker on the selected point. Please select a valid point.")
            continue
          else:
            break
        try:
          dice_selection = int(input("Choose a dice to use for moving the checker: "))
        except ValueError:
          print("Invalid input. Please enter a number.")
          continue
        if dice_selection != dice1 or dice_selection != dice2:
          print("You cannot use this dice to bear off. Please select a valid dice.")
          continue
        if dice_selection == dice1:
          dice1 = 0
        elif dice_selection == dice2:
          dice2 = 0
        if (25 - selection) + dice_selection > 24:
          selected_checker = self.check_position(25 - selection)
          Board.player2_checkers_count['p' + str(25 - selection)][selected_checker] = 0
          Board.player1_board_list[Board.board_map['p' + str(25 - selection)][selected_checker][0]] = ' '
          Board.player1_board_list[Board.board_map['p' + str(25 - selection)][selected_checker][1]] = ' '
          Board.player2_board_list[Board.board_map['p' + str(25 - selection)][selected_checker][0]] = ' '
          Board.player2_board_list[Board.board_map['p' + str(25 - selection)][selected_checker][1]] = ' '
          Board.player1_board = ''.join(Board.player1_board_list)
          Board.player2_board = ''.join(Board.player2_board_list)
          self.checkers -= 1
          if self.checkers == 0:
            print("You have borne off all your checkers. You win!")
            self.winner = True            
        else:
          start_position = self.check_position(25 - selection)
          stop_position = self.check_position((25 - selection) + dice_selection)
          self.move(selection, (25 - selection) + dice_selection, start_position, stop_position)  
  
class Dice:
  def __init__(self):
    self.dice1 = 0
    self.dice2 = 0
    self.double = False

  def roll(self):
    self.dice1 = random.randint(1, 6)
    self.dice2 = random.randint(1, 6)
    if self.dice1 == self.dice2:
      self.double = True
    else:
      self.double = False
    return self.dice1, self.dice2
  
test_board = Board()
test_player1 = Player1("Player 1")
test_player2 = Player2("Player 2")
test_dice = Dice()

# player1_board = test_player1.board
# player2_board = test_player2.board

# dice = Dice()
# player1 = Player1(input("Enter Player 1 name: "))
# player2 = Player2(input("Enter Player 2 name: "))
# test = player1.check_position(6)

while True:
  player1_dice1, player1_dice2 = test_dice.roll()
  player2_dice1, player2_dice2 = test_dice.roll()
  print("Player 1 rolled:", player1_dice1, player1_dice2)
  print("Player 2 rolled:", player2_dice1, player2_dice2)
  if player1_dice1 + player1_dice2 > player2_dice1 + player2_dice2:
    print("Player 1 goes first")
    test_player1.turn = True
    test_player2.turn = False
    break
  elif player1_dice1 + player1_dice2 < player2_dice1 + player2_dice2:
    print("Player 2 goes first")
    test_player1.turn = False
    test_player2.turn = True
    break
  else:
    print("Roll again")
    test_player1.turn = False 
    test_player2.turn = False

while True:
  if test_player1.turn == True:
    print("It's Player 1's turn")
    print(test_board.player1_board)
    player1_dice1, player1_dice2 = test_dice.roll()
    if test_dice.double == True:
      print("You rolled a double! You rolled:", player1_dice1, player1_dice2)
      print("You can move four times.")
      player1_dice3 = player1_dice1
      player1_dice4 = player1_dice2
    else: 
      print("You rolled:", player1_dice1, player1_dice2)
      player1_dice3 = 0
      player1_dice4 = 0
    while player1_dice1 != 0 or player1_dice2 != 0 or player1_dice3 != 0 or player1_dice4 != 0: 
      if test_dice.double == True:
        test_player1.check_bar(player1_dice1, player1_dice2)
        test_player1.check_home()
        test_player1.bear_off(player1_dice1, player1_dice2)
        start_position, start_selection, player1_dice1, player1_dice2 = test_player1.check_start(player1_dice1, player1_dice2)
        stop_position, stop_selection, player1_dice1, player1_dice2 = test_player1.check_stop(player1_dice1, player1_dice2, start_selection)
        test_player1.move(start_selection, stop_selection, start_position, stop_position)
        print(test_board.player1_board)
        test_player1.check_bar(player1_dice3, player1_dice4)
        test_player1.check_home()
        test_player1.bear_off(player1_dice3, player1_dice4)
        start_position, start_selection, player1_dice3, player1_dice4 = test_player1.check_start(player1_dice3, player1_dice4)
        stop_position, stop_selection, player1_dice3, player1_dice4 = test_player1.check_stop(player1_dice3, player1_dice4, start_selection)
        test_player1.move(start_selection, stop_selection, start_position, stop_position)
        print(test_board.player1_board)
        test_player1.turn = False
        test_player2.turn = True
      else:
        print("You rolled:", player1_dice1, player1_dice2)
        test_player1.check_bar(player1_dice1, player1_dice2)
        test_player1.check_home()
        test_player1.bear_off(player1_dice1, player1_dice2)
        start_position, start_selection, player1_dice1, player1_dice2 = test_player1.check_start(player1_dice1, player1_dice2)
        stop_position, stop_selection, player1_dice1, player1_dice2 = test_player1.check_stop(player1_dice1, player1_dice2, start_selection)
        test_player1.move(start_selection, stop_selection, start_position, stop_position)
        print(test_board.player1_board)
      if test_player1.checkers == 0:
        test_player1.winner = True
        print("Player 1 wins!")
        break
    if player1_dice1 == 0 and player1_dice2 == 0:
        test_player1.turn = False
        test_player2.turn = True
  else:
    print("It's Player 2's turn")
    print(test_board.player2_board)
    player2_dice1, player2_dice2 = test_dice.roll()
    if test_dice.double == True:
      print("You rolled a double! You rolled:", player2_dice1, player2_dice2)
      print("You can move four times.")
      player2_dice3 = player2_dice1
      player2_dice4 = player2_dice2
    while player2_dice1 != 0 or player2_dice2 != 0 or player2_dice3 != 0 or player2_dice4 != 0:
      if test_dice.double == True:
        test_player2.check_bar(player2_dice1, player2_dice2)
        test_player2.check_home()
        test_player2.bear_off(player2_dice1, player2_dice2)
        start_position, start_selection, player2_dice1, player2_dice2 = test_player2.check_start(player2_dice1, player2_dice2)
        stop_position, stop_selection, player2_dice1, player2_dice2 = test_player2.check_stop(player2_dice1, player2_dice2, start_selection)
        test_player2.move(start_selection, stop_selection, start_position, stop_position)
        print(test_board.player2_board)
        test_player2.check_bar(player2_dice3, player2_dice4)
        test_player2.check_home()
        test_player2.bear_off(player2_dice3, player2_dice4)
        start_position, start_selection, player2_dice3, player2_dice4 = test_player2.check_start(player2_dice3, player2_dice4)
        stop_position, stop_selection, player2_dice3, player2_dice4 = test_player2.check_stop(player2_dice3, player2_dice4, start_selection)
        test_player2.move(start_selection, stop_selection, start_position, stop_position)
        print(test_board.player2_board)
      else:
        print("You rolled:", player2_dice1, player2_dice2)
        test_player2.check_bar(player2_dice1, player2_dice2)
        test_player2.check_home()
        test_player2.bear_off(player2_dice1, player2_dice2)
        start_position, start_selection, player2_dice1, player2_dice2 = test_player2.check_start(player2_dice1, player2_dice2)
        stop_position, stop_selection, player2_dice1, player2_dice2 = test_player2.check_stop(player2_dice1, player2_dice2, start_selection)
        test_player2.move(start_selection, stop_selection, start_position, stop_position)
        print(test_board.player2_board)
      if test_player2.checkers == 0:
        test_player2.winner = True
        print("Player 2 wins!")
        break
    if player2_dice1 == 0 and player2_dice2 == 0:
      test_player2.turn = False
      test_player1.turn = True      
