Slab1_charges=4.05
global slab1_total



class ElectricityBill:

    def __init__(self):
        print("Constructor")

    def set_units(self,units):
         global meter_units
         meter_units = 0
         meter_units = units


    def calculate_slab1_total(self):

        if(meter_units <= 0 ):
            print("Units can't be less than zero")
            return "Units can't be less than zero"
        elif(meter_units <=50):
            slab1_total = meter_units*Slab1_charges
            print("Electricity Bills is",slab1_total,"for",meter_units)
            return slab1_total

        else:
            print("Upcoming feature")
            return "Upcoming feature"

    def get_energy_charges(self):
        return slab1_total