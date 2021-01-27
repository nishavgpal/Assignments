bowling_frames = [[0 for x in range(10)] for y in range(4)]


class BowlingGame:

    def frame_score(frames, chances, pin_value):

        frames = frames - 1
        chances = chances - 1

        if (frames <= 9):
            if (chances <= 1):
                bowling_frames[chances][frames] = pin_value
                bowling_frames[2][frames] = bowling_frames[2][frames]+bowling_frames[chances][frames]
                bowling_frames[3][frames] = bowling_frames[3][frames - 1] + bowling_frames[2][frames]
                print(frames + 1, "frame", chances + 1, "chance", bowling_frames[3][frames - 1], "cumulative score")

                if (bowling_frames[0][frames - 1] == 10):
                        bowling_frames[3][frames - 1] = bowling_frames[3][frames - 1]+bowling_frames[2][frames]
                        bowling_frames[3][frames] = bowling_frames[3][frames - 1] + bowling_frames[2][frames]
                        print("Strike",frames+1,"frame",chances+1,"chance",bowling_frames[3][frames-1],"cumulative score")
                        return True

                elif (bowling_frames[2][frames - 1] == 10):
                        bowling_frames[3][frames - 1] = bowling_frames[3][frames - 1] + bowling_frames[0][frames]
                        bowling_frames[3][frames] = bowling_frames[3][frames - 1] + bowling_frames[2][frames]
                        print("Spare",frames+1,"frame",chances+1,"chance",bowling_frames[3][frames-1],"cumulative score")
                        return True
                else:
                        return False


            else:
                return False
        else:
            return False

    def get_score(frame):
        if frame != 1:
            return bowling_frames[3][frame - 1]
        else:
            return bowling_frames[3][0]



BowlingGame.frame_score(1, 1, 1)
BowlingGame.frame_score(1, 2, 4)
BowlingGame.frame_score(2, 1, 4)
BowlingGame.frame_score(2, 2, 5)
BowlingGame.frame_score(3, 1, 6)
BowlingGame.frame_score(3, 2, 4)
BowlingGame.frame_score(4, 1, 5)
BowlingGame.frame_score(4, 2, 5)
BowlingGame.frame_score(5, 1, 10)
BowlingGame.frame_score(5, 2, 0)
BowlingGame.frame_score(6, 1, 0)
BowlingGame.frame_score(6, 2, 1)