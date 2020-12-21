import re
class Initialization:
    def __init__(self):
        self.credentials = {}



class Login:
    def check(self, user, pas):

        if user in i.credentials.keys() and pas == i.credentials[user]:
            return True
        else:
            print('Wrong Username or Password')
            return False


class Register:

    def stringvalidation(self, name):

        if name.isalpha():
            return True
        print("Username should have only letters")
        return False



    def pwdvalidation(self, password):
        flag = True
        if (len(password) <= 6):
            flag = False
        elif not (re.search("[a-z]", password) or re.search("[A-Z]", password)):
            flag = False

        elif not re.search("[0-9]", password):
            flag = False
        else:
            flag == True

        return flag


    def register (self,name,password):
            i.credentials[name] = password



i = Initialization()
s = Login()
r = Register()
Stop = False
user_check = True


while Stop == False:
    tasks = (input('What would you like to do? enter [Register], [Login], or [quit]'))
    # Calling functions with that class object
    if tasks == 'Register':
        name = (input('Please enter username'))
        user_check = r.stringvalidation(name)

        if user_check == True:
            password = (input('Please enter password'))
            pwd_check = r.pwdvalidation(password)

            if pwd_check == True:
                r.register(name,password)
                print("User account created successfully")
                user_check == False
                pwd_check == False

            else:
                print("Invalid password")
                user_check == True


    if tasks == 'Login':
        LoginInfoUser = (input('Please enter Username'))
        LoginInfoPassword = (input('Please enter Password'))
        login_check=s.check(LoginInfoUser, LoginInfoPassword)
        if login_check == True:
            print("Login success!")
        else:
            print("Login failed")
    if tasks == 'quit':
        print("See you later!")
        Stop = True