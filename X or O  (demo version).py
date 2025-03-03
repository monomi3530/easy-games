# крестики нолики X or O 

def player1_input():
    player1 = input("Пожалйста выбери символ 'X' или 'O' ").upper()
    
    while player1 not in ["X", "O"]:
        print("Ошибка! Нужно ввести только 'Х' или 'О' ")
        player1 = input("Попробуй снова: ").upper()
    for p in player1:
        if p == "X":
            player2 = "O"
        else: 
            player2 = "X"
    print(f"Игрок1 выбрал {player1}, Игроку2 присвоен {player2}")
    return player1, player2


marker = "X"
def display_board(board):
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    

def stroke_capa(board1, position):
    return board1[position] == " "

def win_check(board, marker):
    for row in [0, 3, 6]:
        if board[row] == board[row + 1] == board[row + 2] == marker:
            return True
        elif board[2] == board[4] == board[6] == marker or board[0] == board[4] == board[8] == marker:
            return True
        for roww in range(3):
            if board[roww] == board[roww + 3] == board[roww + 6] == marker:
                return True
    
def player_line(marker):
     if marker == "X":
        return "O"
     else: 
         return "X" 
  
def clear(replay):
    if replay == "none":
        return False
    elif replay == "no":
        return True
    else: print("игра идёт.")
    return False

def clear_board():
    test_board  = [' ']*9

def clear_outpu():
    print("\n" * 50)

def game():
    replay = "none"
    while True:
        start = True
        test_board  = [' ']*9

        if clear(replay):
            print("Спасибо за игру! 👋")
            break

        player1, player2 = player1_input()
        marker = player1

        display_board(test_board)

        def start_game():
            while True:
                start_game = input("Хотите начать игру? (yes/no): ").lower()
                if start_game == "yes" or start_game == "да":
                    print("Игра начинается! =)")
                    display_board(test_board)
                    return False
                elif start_game == "no" or start_game == "нет":
                    print("🚪 Выход из меню, попробуйте ещё раз.")
                    return True
                    continue
                else:
                    print("❌ Ошибка: Введите 'yes' или 'no'. Попробуйте ещё раз.")

        not_start = start_game()
        while True:

            if not_start:
                break

            position = input("Введите позицию для хода 1-9: ")
            if position.lower() == "stop":
                print("🚪 Выход из игры.")
                break 

            if not position.isdigit():
                print("❌ Ошибка: Введите только числа!")````
                continue 
            
            position = int(position)-1
        
            if position > 8 or position < 0:
                print(" введите число равное количеству игровых клеток 1-9")
            elif stroke_capa(test_board, position):
                clear_outpu()
                test_board[position] = marker
                if win_check(test_board, marker):
                    print(f"игрок игравший за {marker} победил!!!")
                    replay = input("Хотите сыграть ещё раз? (yes/no): ").lower()
                    if replay == "yes":
                        break
                    elif clear(replay):
                        break
                elif " " not in test_board:
                    print("победила дружба! ничья.")
                    replay = input("Хотите сыграть ещё раз? (yes/no): ").lower()
                    if replay == "yes":
                        break
                    if clear(replay):
                        break
                    else:
                        print("{Хорошей игры!}")
                        print("\n" * 50)
                        break

                marker = player_line(marker)
                display_board(test_board)
            else:
                print(f"Эта позиция игроого поля занята {position}, выберите другую!!!")
                display_board(test_board) 

game()

# убрать смену игрового маркера при неудачном символе 
# сделать игру с началом да нет 
# добавить работоспособность стартовому выбору игрового маркера 
