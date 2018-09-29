from random import randint

board = []

for x in range(0, 6):
  board.append(["O"] * 6)

def print_board(board):
  for row in board:
    print (" ".join(row))

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship1_row = random_row(board)
ship1_col = random_col(board)
ship2_row = random_row(board)
ship2_col = random_col(board)
ship3_row = random_row(board)
ship3_col = random_col(board)
#print (ship1_row, ship1_col)
#print (ship2_row, ship2_col)
#print (ship3_row, ship3_col)


for turn in range(6):
  print("Tura:", turn + 1, "Powodzenia!")
  guess_row = int(input("Podaj nr rzedu (liczby od 0 do 5): "))
  guess_col = int(input("Podaj nr kolumny (liczby od 0 do 5):"))

  if (guess_row == ship1_row and guess_col == ship1_col) or \
     (guess_row == ship2_row and guess_col == ship2_col)or \
	 (guess_row == ship3_row and guess_col == ship3_col):
    print ("Brawo udalo ci sie zatopic statek!")
  elif guess_row >=6 or \
    guess_col >=6:
    print ("Oops, nie ma takiej lokalizacji uruchom program od poczadku.")
    break
  elif board[guess_row][guess_col] == "X":
    print ("Już podałes ta lokalizacje!")
  else:
    print ("Sprobuj ponownie!")

  board[guess_row][guess_col] = "X"
  if board[ship1_row][ship1_col] == "X" and board[ship2_row][ship2_col] == "X"\
    and board[ship3_row][ship3_col] == "X":
    print("Brawo wygrales!")
    break

  print_board(board)

  if turn == 5:
    board[ship1_row][ship1_col]= "*"
    board[ship2_row][ship2_col]= "*"
    board[ship3_row][ship3_col]= "*"
    print ("Koniec gry")
    print ("lokalizacja statkow zazanczona gwiazkda:")
    print_board(board)
