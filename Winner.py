class Winner():
    def winner(round1,round2,round3):
        print("Game winner")
        if(round1 == round2 and round2== round3):
            print(round1)
            return round1
        elif(round1 == round2 ):
            if (round1!="Tie"):
                print (round1)
                return round1
            else:
                print(round3)
                return round3
        elif ( round2 == round3 ):
            if (round2 != "Tie"):
                print(round2)
                return round2
            else:
                print(round1)
                return round1
        else:
            print("Tie")
            return "Tie"