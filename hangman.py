def hangman(word):
    wrong = 0
    stages = ["",
              "______     ",
              "|          ",
              "|     |    ",
              "|          ",
              "|     0    ",
              "|    /|`   ",
              "|    / `   ",
              "|          "
                  ]
    reletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ!")


    while wrong < len(stages) - 1:
        print("\n")
        msg = "１文字を予想してね"
        char = input(msg)
        if char in reletters:
            cind = reletters.index(char)
            board[cind] = char
            reletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け!正解は{}.".format(word))

word_list = ["cat","dog","elephant","flower","fish","tsuna","microbiology"]
input_number = int(input("数字を入力してください："))
word_number = input_number % 7
word = word_list[word_number]

hangman(word)
