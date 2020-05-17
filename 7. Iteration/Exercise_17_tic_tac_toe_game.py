"""
You and your friend are in a team to write a two-player game, human against computer,
such as Tic-Tac-Toe / Noughts and Crosses. Your friend will write the logic to play one round of the game,
while you will write the logic to allow many rounds of play, keep score, decide who plays, first, etc.
The two of you negotiate on how the two parts of the program will fit together,
and you come up with this simple scaffolding (which your friend will improve later):

        # Your friend will complete this function
        def play_once(human_plays_first):

                Must play one round of the game. If the parameter
                is True, the human gets to play first, else the
                computer gets to play first.  When the round ends,
                the return value of the function is one of
                -1 (human wins),  0 (game drawn),   1 (computer wins).

                # This is all dummy scaffolding code right at the moment...
            import random                  # See Modules chapter ...
            rng = random.Random()
                # Pick a random result between -1 and 1.
            result = rng.randrange(-1,2)
            print("Human plays first={0},  winner={1} "
                       .format(human_plays_first, result))
            return result


a. Write the main program which repeatedly calls this function to play the game,
and after each round it announces the outcome as “I win!”, “You win!”, or “Game drawn!”.
It then asks the player “Do you want to play again?” and either plays again, or says “Goodbye”, and terminates.

b. Keep score of how many wins each player has had, and how many draws there have been. After each round of play, also announce the scores.

c. Add logic so that the players take turns to play first.

d. Compute the percentage of wins for the human, out of all games played. Also announce this at the end of each round.

e. Draw a flowchart of your logic.
"""




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
    print("Human plays first={0},  winner={1} "
                       .format(human_plays_first, result))
    return result


def play_game():
    human_score = 0             # COUNTING THE SCORE MAY BE POSIBLE WITHOUT CREATING MULTIPLE VARIABLES BUT I COULD NOT FOUND HOW TO DO THAT.
    computer_score = 0
    draw_score = 0
    games_played = 0            # COUNTING PERCENTAGE OF WINS FOR THE HUMAN, ALSO SHOULD BE POSSIBLE WITH FUNCTION
    percentage_of_wins = 0
    while True:
        play_turns()
        games_played += 1
        human_plays_first = 0
        result = play_once(human_plays_first)
        if result == -1:
            human_score += 1
            percents_of_wins = human_score * 100 / games_played
            print("Human won:", human_score, "Win percentage: ", percents_of_wins)
        elif result == 0:
            draw_score += 1
            percents_of_wins = human_score * 100 / games_played
            print("Game drawn:", draw_score, "Win percentage: ", percents_of_wins)
        elif result == 1:
            computer_score += 1
            percents_of_wins = human_score * 100 / games_played
            print("Computer won:", computer_score, "Win percentage: ", percents_of_wins)
        play_again = input("Play again? (yes or no)")
        if play_again != "yes":
            break
    print("Goodbye!", "Games played: ", games_played, "Win percentage: ", percents_of_wins)


# C PART DETERMINE WHOSE TURN IT IS
def play_turns():
    import random
    turn = random.randint(1, 2)         # HEADS OR TAILS
    if turn == 1:
        player_turns = True
        computer_turn = False
        print("Player will go first!")
    else:
        player_turns = False
        computer_turn = True
        print("Computer will go first!")


play_game()