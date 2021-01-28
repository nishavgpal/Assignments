bowling_frames = [[0 for x in range(11)] for y in range(5)]
roll1_Score = 1
frame_roll_score = 3
cumulative_frame_score = 4
current_frame=1
last_frame = current_frame - 1

class BowlingGame:

    def update_cumulative_score_double_strike(current_frame,bowling_frames):

        last_frame = current_frame - 1
        bowling_frames[cumulative_frame_score][last_frame] = bowling_frames[cumulative_frame_score][last_frame]+bowling_frames[frame_roll_score][current_frame]
        bowling_frames[cumulative_frame_score][current_frame] = bowling_frames[cumulative_frame_score][last_frame] + bowling_frames[frame_roll_score]

    def update_cumulative_score_strike(current_frame,bowling_frames):
        last_frame = current_frame - 1
        bowling_frames[cumulative_frame_score][last_frame] = bowling_frames[cumulative_frame_score][last_frame]+bowling_frames[frame_roll_score][current_frame]
        bowling_frames[cumulative_frame_score][current_frame] = bowling_frames[cumulative_frame_score][last_frame] + bowling_frames[frame_roll_score][current_frame]


    def update_cumulative_score_spare(current_frame,bowling_frames):
        last_frame = current_frame - 1

        bowling_frames[cumulative_frame_score][last_frame] = bowling_frames[cumulative_frame_score][last_frame] + bowling_frames[roll1_Score][current_frame]

        bowling_frames[cumulative_frame_score][current_frame] = bowling_frames[cumulative_frame_score][last_frame] + bowling_frames[frame_roll_score][current_frame]



    def check_spare_strike_last_frame(current_frame,current_roll_score,bowling_frames):
        last_frame = current_frame - 1


        if (bowling_frames[roll1_Score][last_frame] == 10 and current_roll_score== 2):

            BowlingGame.update_cumulative_score_strike(current_frame,bowling_frames)

        elif(bowling_frames[frame_roll_score][last_frame] == 10 and current_roll_score== 1 and bowling_frames[roll1_Score][last_frame] != 10):

            BowlingGame.update_cumulative_score_spare(current_frame,bowling_frames)




    def frame_score(current_frame, current_roll_score, pin_value):

        #roll1_Score = 1
        #frame_roll_score = 3
        #cumulative_frame_score = 4


        if (current_frame <= 10):
            last_frame = current_frame - 1
            if (current_roll_score <= 2):
                bowling_frames[current_roll_score][current_frame] = pin_value
                bowling_frames[frame_roll_score][current_frame] = bowling_frames[frame_roll_score][current_frame]+bowling_frames[current_roll_score][current_frame]
                bowling_frames[cumulative_frame_score][current_frame] = bowling_frames[cumulative_frame_score][last_frame] + bowling_frames[frame_roll_score][current_frame]
                BowlingGame.check_spare_strike_last_frame(current_frame,current_roll_score,bowling_frames)

                return True
            else:
                return False


        else:
            return False

    def get_score(current_frame):
        print(bowling_frames[cumulative_frame_score][current_frame])
        return bowling_frames[cumulative_frame_score][current_frame]

