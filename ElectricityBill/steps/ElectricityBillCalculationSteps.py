from behave import *
from ElectricityBill import ElectricityBillCalculation

use_step_matcher("re")

object_bill = ElectricityBillCalculation.ElectricityBill()


class energy_charge_slabwise_step_definitions:


    @given("I consumed (?P<units>.+) units in a month")
    def step_impl1(context, units):
        object_bill.set_units(units)


    @when("the state ABC electricity bill gets generated")
    def step_impl2(context):
        object_bill.calculate_slab1_total()


    @then("the total energy charges as amounted to Rs\.(?P<slab1total>.+)")

    def step_impl3(context, slab1total):

        Bill_Total = object_bill.get_energy_charges()
        if(Bill_Total==slab1total):
            print("Electricity Bill is",Bill_Total)
