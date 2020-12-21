from Authentication_Kata import Register
from Authentication_Kata import Login
import unittest



class Test_Register_Validations(unittest.TestCase):


    def test_validate_for_only_letters_present_pass(self):
        result = Register.stringvalidation(self,str("test"))
        self.assertTrue(result == True)

    def test_validate_for_only_letters_present_with_numbers_fail(self):
        result = Register.stringvalidation(self,"test122")
        self.assertTrue(result == False)

    def test_validate_for_minimum_length_of_password_pass(self):
        result = Register.pwdvalidation(self,"testttt")
        self.assertFalse(result == True)

    def test_validate_for_minimum_length_of_password_fail(self):
        result = Register.pwdvalidation(self, "test")
        self.assertTrue(result == False)

    def test_validate_for_minimum_one_alphabet_pass(self):
        result = Register.pwdvalidation(self,"test12")
        self.assertFalse(result == True)

    def test_validate_for_minimum_one_alphabet_fail(self):
        result = Register.pwdvalidation(self,"34512")
        self.assertTrue(result == False)

    def test_validate_for_minimum_one_digit_pass(self):
        result = Register.pwdvalidation(self,"test12")
        self.assertFalse(result == True)

    def test_validate_for_minimum_one_digit_fail(self):
        result = Register.pwdvalidation(self, "testtt")
        self.assertTrue(result == False)


class Test_Login_Validations(unittest.TestCase):
    def test_validate_for_username_present_pass(self):
        result = Login.check(self, "test", "test12")
        self.assertTrue(result == False)

    def test_validate_for_username_present_pass(self):
        result = Login.check(self, "test", "test")
        self.assertFalse(result == True)


if __name__ == '__main__':
    unittest.main()
