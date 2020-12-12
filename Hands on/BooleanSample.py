class BooleanSample:

    def __init__(self, dayOfWeek):
     self.dayOfWeek = dayOfWeek
                
    def isWeekDay(self, dayOfWeek):
        if (("Saturday".lower() == dayOfWeek.lower()) or ("Sunday".lower() == dayOfWeek.lower())):
            print(dayOfWeek)
            return False

        elif (("Monday".lower() == dayOfWeek.lower()) or ("Tuesday".lower() == dayOfWeek.lower()) or 
        ("Wednesday".lower() == dayOfWeek.lower()) or ("Thursday".lower() == dayOfWeek.lower()) or
        ("Friday".lower() == dayOfWeek.lower())):
            print(dayOfWeek)
            return True
        
        else:
            print(dayOfWeek)
            return False


    if __name__ == "__main__":
      booleanSample = BooleanSample("abrakadabra")
      var = BooleanSample.isWeekDay()
      print(var)

