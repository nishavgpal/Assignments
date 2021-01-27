bowling_frames = [[0 for x in range(10)] for y in range(4)]


class BowlingGame():

    def frame_score(self,frames,chances,pin_value):

        frames=frames-1
        chances=chances-1

        if ( frames<=9):
            if(chances<=1):
                if (chances == 1 and bowling_frames[0][frames]+ pin_value<=10):
                    bowling_frames[chances][frames]=pin_value
                    bowling_frames[2][frames] = bowling_frames[chances][frames] + bowling_frames[chances - 1][frames]
                    bowling_frames[3][frames]= bowling_frames[3][frames-1]+bowling_frames[2][frames]
                    return True
                elif (bowling_frames[0][frames] + pin_value <= 10):
                    bowling_frames[chances][frames] = pin_value
                    bowling_frames[2][frames] = bowling_frames[chances][frames]
                    bowling_frames[3][frames] = bowling_frames[3][frames - 1] + bowling_frames[2][frames]
                    return True
                if(bowling_frames[2][frames-1]==10):
                        bowling_frames[3][frames - 1] = bowling_frames[3][frames - 1] + bowling_frames[0][frames]
                        bowling_frames[3][frames] = bowling_frames[3][frames - 1] + bowling_frames[2][frames-1]
                if(bowling_frames[0][frames-1]==10):
                    bowling_frames[3][frames - 1] = bowling_frames[2][frames]

                else:
                    return False
            else:
                return False
        else:
            return False


    def get_score(frame):
        if frame!=1:
            return bowling_frames[3][frame-1]
        else:
            return bowling_frames[3][0]