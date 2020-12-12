import random

class EqualitySample:
    #def __init__(self):
        #self.name = name
        #self.principal = principal
        #self.interestRate = interestRate

    def getWelcomeMassage(self):
        print('getWelcomeMassage')
        resultStr = None
        if self.name == "":
                raise Exception ("Invalid Name, Name cannot be empty")
        else:
            print(self.name)
            resultStr = "Hello " + self.name
            print(resultStr)
            return resultStr


    def getTextApendedWithRandomNumber(self, textVar):
        print('getTextApendedWithRandomNumber')
        randomNumber = random.randint(0, 1000)
        appendedText = textVar + " " + str(randomNumber)

        print(appendedText)

        return appendedText
        
    def allWeekDays(self):
        print('allWeekDays')
        weekDaysList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return weekDaysList

    def weekDay(self):
        print('weekDay')
        weekDay = "Monday"
        return weekDay

    def getMaturityAmount(self, principal, interestRate):
        print('getMaturityAmount')

        amount = principal + (principal * interestRate)/100

        return amount