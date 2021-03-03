Slab1_charges=4.05

class ElectricityBill:
    def define_variables(self):
        global meter_units
        meter_units = 0

    def set_units(self,units):
         meter_units = units


    def calculate_slab1_total(self):

        if(meter_units<=0 ):
            return "Units can't be less than zero"
        elif(meter_units<=50):
            slab1_total = meter_units*Slab1_charges
            return slab1_total

        else:
            return "Upcoming feature"