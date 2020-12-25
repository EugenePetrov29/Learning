game = False
while not game:
    print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)
    board = list(range(1,10))
    counter = 0
    win = False
    while not win:
        print("-" * 13)
        for i in range(3):
            print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
            print("-" * 13)
        if counter % 2 == 0:
            valid = False
            while not valid:
                while not valid:
                    player_token = "X"
                    player_answer = input("Куда поставим " + player_token+"? ")
                    try:
                        player_answer = int(player_answer)
                        valid = True
                    except:
                        print("Некорректный ввод. Вы уверены, что ввели число?")
                        valid = False
                if player_answer >= 1 and player_answer <= 9:
                    if(str(board[player_answer-1]) not in "X0"):
                        board[player_answer-1] = player_token
                        valid = True
                    else:
                        print("Эта клетка уже занята!")
                        valid = False
                else:
                    print("Некорректный ввод. Введите число от 1 до 9.")
                    valid = False
        else:
            valid = False
            while not valid:
                while not valid:
                    player_token = "0"
                    player_answer = input("Куда поставим " + player_token+"? ")
                    try:
                        player_answer = int(player_answer)
                        valid = True
                    except:
                        print("Некорректный ввод. Вы уверены, что ввели число?")
                        valid = False
                if player_answer >= 1 and player_answer <= 9:
                    if(str(board[player_answer-1]) not in "X0"):
                        board[player_answer-1] = player_token
                        valid = True
                    else:
                        print("Эта клетка уже занята!")
                        valid = False
                else:
                    print("Некорректный ввод. Введите число от 1 до 9.")
                    valid = False
        counter += 1
        if counter > 4:       
            win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
            for each in win_coord:
                if board[each[0]] == board[each[1]] == board[each[2]]:
                    a = board[each[0]]
                    print(a, "выиграл!")
                    win = True
            if counter == 9 and win == False:
                print("Ничья!")
                win = True
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)
    if win == True:
        s = False
        while not s:
            answer = input("Ходите начать заново? (д/н): ")
            if answer == "д":
                s = True
            elif answer == "н":
                game = True
                s = True
            else:
                print("Введите ответ д/н")