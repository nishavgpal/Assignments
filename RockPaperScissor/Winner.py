class Winner():
    def choose_winner(round1winner,round2winner,round3winner):

        print("Game winner")

        if(round1winner == round2winner and round2winner== round3winner):
            print(round1winner)
            return round1winner
        elif(round1winner== round2winner ):
            if (round1winner == "Tie"):
                print (round3winner)
                return round3winner
            else:
                print(round1winner)
                return round1winner
        elif ( round2winner == round3winner ):
            if (round2winner == "Tie"):
                print(round1winner)
                return round1winner
            else:
                print(round2winner)
                return round2winner
        elif(round1winner == round3winner):
            if (round1winner == "Tie"):
                print(round2winner)
                return round2winner
            else:
                print(round1winner)
                return round1winner
        else:
            print("Tie")
            return "Tie"

