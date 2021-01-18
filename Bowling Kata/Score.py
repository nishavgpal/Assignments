
class Score:
    def Total_score(current_roll1,current_roll2):
        frame_score=[0]*10
        index=0
        for index in range(10):
            if index!=0:
                current_score= frame_score[index-1]+current_roll1+current_roll2
                frame_score.append(current_score)
                return frame_score[index]
            else:
                return frame_score[index]
