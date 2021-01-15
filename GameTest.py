from Game import Game
import unittest



class MyTestCase(unittest.TestCase):
    def test_game_paper_paper(self):
        result = Game.play(self,"Paper","Paper")
        self.assertEquals(result,"Tie")

    def test_game_rock_scissors(self):
        result = Game.play(self,"Rock","Scissor")
        self.assertEquals(result,"User")

    def test_game_rock_paper(self):
        result = Game.play(self, "Rock", "Paper")
        self.assertEquals(result, "System")
    def test_game_scissors_paper(self):
        result = Game.play(self, "Scissors", "Paper")
        self.assertEquals(result, "User")
    def test_game_scissors_rock(self):
        result = Game.play(self, "Scissors", "Rock")
        self.assertEquals(result, "System")
    def test_game_paper_rock(self):
        result = Game.play(self, "Paper", "Rock")
        self.assertEquals(result, "User")
    def test_game_paper_scissors(self):
        result = Game.play(self, "Paper", "Scissors")
        self.assertEquals(result, "System")
    def test_game_scissors_scissors(self):
        result = Game.play(self, "Scissors", "Scissors")
        self.assertEquals(result, "Tie")
    def test_game_rock_rock(self):
        result = Game.play(self, "Rock", "Rock")
        self.assertEquals(result, "Tie")


if __name__ == '__main__':
    unittest.main()
