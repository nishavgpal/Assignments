class Name:
        #def __init__(self, name):
        #    self.name = name

        def helloName(self, inputName):
            resultStr = None
            print(inputName)
            if (inputName == None) or (inputName == ""):
                raise Exception ("Invalid Name, Name cannot be empty")
            else:
                resultStr = "Hello " + inputName
                print(resultStr)
                return resultStr

        
