import self as self

from Authentication_Kata import Register
from Authentication_Kata import Login
from DBoperations import DBoperations
import unittest
from unittest.mock import Mock
credentials={}


def mock_db_call_register(self, name, password):
    credentials[name] = password
    return True


class Test_Register_Validations(unittest.TestCase):


    def test_validate_for_only_letters_present_pass(self):
        result = Register.user_name_validation(self,str("test"))
        self.assertTrue(result == True)

    def test_validate_for_only_letters_present_with_numbers_fail(self):
        result = Register.user_name_validation(self,"test122")
        self.assertTrue(result == False)

    def test_validate_for_minimum_length_of_password_pass(self):
        result = Register.password_validation(self,"testttt")
        self.assertFalse(result == True)

    def test_validate_for_minimum_length_of_password_fail(self):
        result = Register.password_validation(self, "test")
        self.assertTrue(result == False)

    def test_validate_for_minimum_one_alphabet_pass(self):
        result = Register.password_validation(self,"test12")
        self.assertFalse(result == True)

    def test_validate_for_minimum_one_alphabet_fail(self):
        result = Register.password_validation(self,"34512")
        self.assertTrue(result == False)

    def test_validate_for_minimum_one_digit_pass(self):
        result = Register.password_validation(self,"test12")
        self.assertFalse(result == True)

    def test_validate_for_minimum_one_digit_fail(self):
        result = Register.password_validation(self, "testtt")
        self.assertTrue(result == False)



    def test_validate_user_registered_success(self):
        mock=Mock()
        mock.patch.object(DBoperations,'db_call_register',mock_db_call_register)
        Register.register(self,"test","test123")
        result= mock.mock_db_call_register.called_once()
        print(mock_db_call_register.call_count)
        self.assertTrue(result,True)



class Test_Login_Validations(unittest.TestCase):
    Register.register(self,"test","test123")
    def test_validate_for_username_present_pass(self):
        result = Login.check(self, "test", "test123")
        self.assertTrue(result == True)

    def test_validate_for_username_present_fail(self):
        result = Login.check(self, "test", "test")
        self.assertFalse(result == True)


if __name__ == '__main__':
    unittest.main()
