import unittest
from Winner import Winner

class MyTestCase(unittest.TestCase):
    def test_winner_Tie_for_Round1Tie_Round2Tie_Round3Tie(self):
        result= Winner.winner(self,"Tie","Tie","Tie")
        self.assertEqual(result, "Tie")
    def test_winner_User_for_Round1User_Round2User_Round3User(self):
        result= Winner.winner(self,"User","User","User")
        self.assertEqual(result, "User")
    def test_winner_System_for_Round1System_Round2System_Round3System(self):
        result= Winner.winner(self,"System","System","System")
        self.assertEqual(result, "System")
    def test_winner_User_for_Round1User_Round2User_Round3System(self):
        result = Winner.winner(self, "User", "User", "System")
        self.assertEqual(result, "User")
    def test_winner_System_for_Round1System_Round2System_Round3User(self):
        result = Winner.winner(self, "System", "System", "User")
        self.assertEqual(result, "System")
    def test_winner_User_for_Round1User_Round2Tie_Round3Tie(self):
        result = Winner.winner(self, "User", "Tie", "Tie")
        self.assertEqual(result, "User")
    def test_winner_System_for_Round1System_Round2Tie_Round3Tie(self):
        result = Winner.winner(self, "System", "Tie", "Tie")
        self.assertEqual(result, "System")

    def test_winner_Tie_for_Round1System_Round2User_Round3Tie(self):
            result = Winner.winner(self, "System", "User", "Tie")
            self.assertEqual(result, "Tie")


if __name__ == '__main__':
    unittest.main()
