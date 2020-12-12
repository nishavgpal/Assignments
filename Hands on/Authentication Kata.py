class Initialization:
    def __init__(self):
        self.credentials = {}

class Login:
    def check(self, user, pas):
        """print(self.credentials)"""
        if user in self.credentials.keys() and pas == self.credentials[user]:
            print("Login success!")
        else:
            print('Wrong Username or Password')
class Register:
    def register(self, username, password):
        self.credentials[username] = password
        print("UserAccount created successfully")


s = Login()
r =  Register()
Stop = False

while Stop == False:
    tasks = (input('What would you like to do? enter [Register], [Login], or [quit]'))
    # Calling functions with that class object
    if tasks == 'Register':
        Name = (input('Please enter username'))
        Password = (input('Please enter password'))
        r.register(Name, Password)

    """if tasks == 'Login':
        LoginInfoUser = (input('Please enter Username'))
        LoginInfoPassword = (input('Please enter Password'))
        s.check(LoginInfoUser, LoginInfoPassword)
    if tasks == 'quit':
        print("See you later!")
        Stop = True"""
