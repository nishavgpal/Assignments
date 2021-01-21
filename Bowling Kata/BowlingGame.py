bowling_frames = [[0 for x in range(10)] for y in range(3)]
frame_score = [0] * 10

class BowlingGame():
"""
    def frames_count(self,count):

        if (count<=9):
            return True
        else:
            return False

    def chances_count(self,count):

        if (count <= 2):
            return True
        else:
            return False
            """

    def frame_score(self,frames,chances,pin_value):

        frames=frames-1
        chances=chances-1

        if ( frames<=9):
            if(chances<=1):
                if (chances == 1 and bowling_frames[0][frames]+ pin_value<=10):
                    bowling_frames[chances][frames]=pin_value
                    bowling_frames[2][frames]=bowling_frames[chances][frames]+bowling_frames[chances-1][frames]
                    return True

                elif ( bowling_frames[0][frames]+pin_value <= 10):
                    bowling_frames[chances][frames] = pin_value
                    bowling_frames[2][frames] = bowling_frames[chances][frames]
                    return True

                else:
                    return False
            else:
                return False
        else:
            return False

    def Total_score(frame,current_frame_total):

        index=frame-1
        if index!=0:
            current_total_score= frame_score[index-1]+current_frame_total
            frame_score.append(current_total_score)
            return frame_score[index]
        else:
            frame_score.append(current_frame_total)
            return frame_score[index]
    def get_score(frame):
        if frame!=1:
            return frame_score[frame-1]
        else:
            return frame_score[0]