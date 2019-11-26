# Your friend will complete this function
def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random                  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first = {0},  winner = {1} "
                       .format(human_plays_first, result))
    return result


def play_one_game(a):
    human = 0
    comp = 0
    draw = 0
    answer = "y"
    global human_first
    human_first = not human_first
    while answer != "n":
        if answer == "y":
            a = play_once(a)
            if a == -1:
                human += 1
                print("Human wins")
            elif a == 1:
                comp += 1
                print("Computer wins")
            else:
                draw += 1
                print("Draw")
            print("Scores: Human:", human, "Computer:", comp, "Draws:", draw)
        else:
            print("Invalid response")
        answer = input("Do you want to play again? (y/n)\n")


def who_plays_first():
    a = None
    while a == None:
        answer = input("Human plays first (y/n)?\n")
        if answer == "y":
            a = True
            return a
        elif answer == "n":
            a = False
            return a
        else:
            print("Invalid response.\n")


human_first = True
who_plays_first()
play_one_game(human_first)
play_one_game(human_first)
print("Goodbye.")