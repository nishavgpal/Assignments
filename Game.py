

class Game:
    def play(user_move,comp_move):

        if (user_move == comp_move):
            print(f"BOTH with {user_move} - TIE")
            return "Tie"
        elif(user_move == "Rock" and comp_move == "Scissor" or user_move == "Scissors" and comp_move == "Paper"or user_move == "Paper" and comp_move == "Rock" )  :
            print(f"USER with {user_move} - WIN")
            return "User"
        else:
            print(f"SYSTEM with {comp_move} - WIN")
            return "System"





