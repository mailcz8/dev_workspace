import random

class TicTacToe(object):
  def __init__(self):
    pass

  def clear_output(self):
    print('\n'*10)

  def display_board(self, board):
    print('-'*9)
    print(board[7]+' | '+board[8]+' | '+board[9]+'\n'+'-'*9)
    print(board[4]+' | '+board[5]+' | '+board[6]+'\n'+'-'*9)
    print(board[1]+' | '+board[2]+' | '+board[3]+'\n'+'-'*9)

  def player_input(self):
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    marker = ''
    # Keep asking player 1 to choose X or O
    while marker.upper() != 'X' and marker.upper() != 'O':
      marker = input('Player 1, choose X or O: ').upper()
    # Assign player 2, the opposite marker
    if marker == 'X':
      # print('='*10,'Gamers get ready!!!','='*10)
      # print('Player1 marker = ',player1 + '; Player2  marker = ',player2)
      # print('='*10,'!!!Let the game begin!!!','='*10)
      return ('X','O')
    else:
      return ('O','X')

  def win_check(self, board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

  def place_marker(self, board, marker, position):
    board[position] = marker

  def choose_first(self):
    flip = random.randint(0,1)
    if flip == 0:
      return 'Player 1'
    else:
      return 'Player 2'

  def space_check(self, board, position):
    return board[position] == ' '

  def full_board_check(self, board):
    for i in range(0,9):
      if self.space_check(board, i):
        return False
      # Board is full when retrun True
      else:
        return True

  def player_choice(self, player, board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not self.space_check(board,position):
      position = int(input(player+', choose a position: (1-9): '))
    return position

  def replay(self):
    choice = input('Play again? Enter Yes or No: ').lower()
    # print('choice =',choice)
    return choice == 'yes'

  # While loop to keep running the game
  print('Welcome to Tic Tac Toe')

  def play_game(self):
    while True:
      # Play the game
      ## Set everything up (Board, Who first, choose marker X,O)
      the_board = [' ']*10

      player1_marker, player2_marker = self.player_input()
      print(player1_marker, player2_marker)

      turn = self.choose_first()
      print(turn,'will go first.')

      # play_game = input('Ready to play? y or n? ').lower()
      #
      # if play_game == 'y':
      #   game_on = True
      # else:
      #   game_on = False
      game_on = True

      while game_on:
        self.clear_output()
        if turn == 'Player 1':
          # Show the board
          self.display_board(the_board)
          # Choose a position
          position = self.player_choice(turn, the_board)
          # Place the marke on the position
          self.place_marker(the_board,player1_marker,position)
          # Or check if won
          if self.win_check(the_board,player1_marker):
            self.clear_output()
            self.display_board(the_board)
            print('Player 1 has Won!!!')
            game_on = False
          else:
            if self.full_board_check(the_board):
              self.display_board(the_board)
              print('Tie game, player 1 block')
              game_on = False
            else:
              turn = 'Player 2'
        else:
          self.display_board(the_board)
          # Choose a position
          position = self.player_choice(turn, the_board)
          # Place the marke on the position
          self.place_marker(the_board,player2_marker,position)
          # Or check if won
          if self.win_check(the_board,player2_marker):
            self.clear_output()
            self.display_board(the_board)
            print('Player 2 has Won!!!')
            game_on = False
          else:
            if self.full_board_check(the_board):
              self.display_board(the_board)
              print('Tie game, player2 block')
              game_on = False
            else:
              turn = 'Player 1'

      if not self.replay():
        print('Game Over!!!')
        break

if __name__ == '__main__':
  start_board = ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-']
  x = TicTacToe()
  x.play_game()
