'''
Author name:
last Edited: 05/05/2021 (10PM)
Application: Rock, Paper, Scissors Game
Discription: This game allow for the user to play against computer
'''

# import random module
import random


def game_rules():
    """Prints the winning rules for the game"""
    txt = "Winning Rules for this game is as follows: \n"
    txt += "  Rock vs paper -> paper wins \n"
    txt += "  Rock vs scissor -> Rock wins \n"
    txt += "  paper vs scissor -> scissor wins \n"
    return txt


def game_rounds():
    """Asks the user how many rounds they want to play"""
    try:
        choice = int(input("How many rounds do you want to play? (1 to 10) "))
        if 1 <= choice <= 10:
            return choice
        else:
            raise Exception("Invalid entry")
    except:
        return False


def comp_choice():
    """Computers choice: 1. Rock, 2. Paper, 3. Scissors"""
    comp_ans = random.randint(1, 3)
    if comp_ans == 1:
        return "rock"
    elif comp_ans == 2:
        return "paper"
    else:
        return "scissors"


def user_choice():
    """User enters choice: 1. Rock, 2. Paper, 3. Scissors, 4. End program"""
    try:
        print("Enter choice \n  1.Rock \n  2.paper \n  3.scissor \n  4.End Program")
        user_ans = int(input("Choices (1 or 2 or 3 or 4): "))
        if 1 <= user_ans <= 4:
            if user_ans == 1:
                return "rock"
            elif user_ans == 2:
                return "paper"
            elif user_ans == 3:
                return "scissors"
            elif user_ans == 4:
                return "end_program"
        else:
            raise Exception("Invalid entry!")
    except:
        return False


score_tracker = []


def if_user_pick_rock(user_ans, comp_ans, txt1, txt2, txt3, txt4, txt5,
                      txt6):  # when user pick Rock, it get compared to computers choice, then print result showing who won the game

    if user_ans == "rock":
        if comp_ans == "rock":
            score_tracker.append("tie_game")
            print(txt1)  # User choice VS computer choice
            print(txt2)  # Tie Game
            print(txt5)  # Game Left
            print(txt6)  # Game Played

        elif comp_ans == "paper":
            score_tracker.append("computer_win")
            print(txt1)  # User choice VS computer choice
            print(txt3)  # Computer wins! and You Loss!"
            print(txt5)  # Game Left
            print(txt6)  # Game Played

        else:
            score_tracker.append("user_win")
            print(txt1)  # User choice VS computer choice
            print(txt4)  # You win! and Computer Loss!
            print(txt5)  # Game Left
            print(txt6)  # Game Played

    else:
        pass


# when user pick Paper, it get compared to computers choice, then print result showing who won the game
def if_user_pick_paper(user_ans, comp_ans, txt1, txt2, txt3, txt4, txt5, txt6):
    if user_ans == "paper":
        if comp_ans == "paper":
            score_tracker.append("tie_game")
            print(txt1)  # User choice VS computer choice
            print(txt2)  # Tie Game
            print(txt5)  # Game Left
            print(txt6)  # Game Played


        elif comp_ans == "scissors":
            score_tracker.append("computer_win")
            print(txt1)  # User choice VS computer choice
            print(txt3)  # Computer wins! and You Loss!"
            print(txt5)  # Game Left
            print(txt6)  # Game Played

        else:

            score_tracker.append("user_win")
            print(txt1)  # User choice VS computer choice
            print(txt4)  # You win! and Computer Loss!
            print(txt5)  # Game Left
            print(txt6)  # Game Played

    else:
        pass


def if_user_pick_scissors(user_ans, comp_ans, txt1, txt2, txt3, txt4, txt5,
                          txt6):  # when user pick Scissors, it get compared to computers choice, then print result showing who won the game

    if user_ans == "scissors":

        if comp_ans == "scissors":
            score_tracker.append("tie_game")
            print(txt1)  # User choice VS computer choice
            print(txt2)  # Tie Game
            print(txt5)  # Game Left
            print(txt6)  # Game Played


        elif comp_ans == "rock":
            score_tracker.append("computer_win")
            print(txt1)  # User choice VS computer choice
            print(txt3)  # Computer wins! and You Loss!"
            print(txt5)  # Game Left
            print(txt6)  # Game Played


        else:
            score_tracker.append("user_win")
            print(txt1)  # User choice VS computer choice
            print(txt4)  # You win! and Computer Loss!
            print(txt5)  # Game Left
            print(txt6)  # Game Played

    else:
        pass


def play_again():  # After all attempt is exusted, function ask user if they want to play again eg. Y or y ==> yes, N or n ==> No

    try:
        user_ans = str(input("Do you want to play again?(Y/N) "))
        user_ans.lower()  # Convert input to lower case

        if user_ans == "y":
            return "y"

        elif user_ans == "n":
            return "n"

        else:
            raise Exception("Invalid entry")

    except:
        return False


def main(activeFlag=True, horizontal_line="__" * 35, quit_message="Thanks for playing",
         numb_games_played=1):
    """Function Starts program"""
    print(game_rules())
    numb_games_left = game_rounds()

    while activeFlag:
        if numb_games_left != 0 or numb_games_left < 0:
            user_ans = user_choice()

            if user_ans == False:
                print("Invalid entry!")
                continue
            else:
                comp_ans = comp_choice()
                txt1 = "\nYou pick " + user_ans.upper() + " VS Computer's " + comp_ans.upper()
                txt2 = "Win Status    ==> Round " + str(numb_games_played) + " is a tie game."
                txt3 = "Win Status    ==> Computer wins round " + str(numb_games_played)
                txt4 = "Win Status    ==> You win round " + str(numb_games_played)
                txt5 = "Attempt Left  ==> " + str(numb_games_left - 1)
                txt6 = "Games Played  ==> " + str(numb_games_played)

                if user_ans == "rock":
                    numb_games_left -= 1
                    rock = if_user_pick_rock(user_ans, comp_ans, txt1, txt2, txt3, txt4, txt5, txt6)

                elif user_ans == "paper":
                    numb_games_left -= 1
                    paper = if_user_pick_paper(user_ans, comp_ans, txt1, txt2, txt3, txt4, txt5, txt6)

                elif user_ans == "scissors":
                    numb_games_left -= 1
                    scissors = if_user_pick_scissors(user_ans, comp_ans, txt1, txt2, txt3, txt4, txt5, txt6)

                else:
                    if user_ans == "end_program":
                        print(quit_message)
                        break
                    else:
                        pass

                numb_games_played += 1
                tie_score = score_tracker.count("tie_game")
                user_score = score_tracker.count("user_win")
                comp_score = score_tracker.count("computer_win")
                game_score = "Final Score   ==> Your Score: " + str(user_score) + " , Computer Score: " + str(
                    comp_score) + " , and Ties Score:  " + str(tie_score)
                comp_win_msg = "Computer wins the series!"
                user_win_msg = "Congratulations! You win the series!"
                tie_breaker_msg = "Play again for tie breaker so there's a winner"

                if numb_games_left > 0:
                    print(game_score)
                else:
                    if user_score > comp_score:
                        print(game_score)
                        print(user_win_msg)
                    elif user_score < comp_score:
                        print(game_score)
                        print(comp_win_msg)
                    else:
                        print(game_score)
                        print(tie_breaker_msg)

                print(horizontal_line)

        else:
            if comp_score != user_score:
                score_tracker.clear()
                restart = play_again()

                if restart == "y":
                    numb_games_left = game_rounds()
                elif restart == "n":
                    print(quit_message)
                    activeFlag = False
                else:
                    print("Invalid entry")
                    continue
            else:
                numb_games_left = 2
                txt = "\nTie breaker. Best of " + str(numb_games_left) + " games."
                print(txt)


if __name__ == '__main__':
    main()
