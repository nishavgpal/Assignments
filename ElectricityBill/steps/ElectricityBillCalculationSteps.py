from behave import *
from unittest import TestCase

from self import self

import ElectricityBillCalculation


use_step_matcher("re")

object_bill = ElectricityBillCalculation.ElectricityBill()


class energy_charge_slabwise_step_definitions(TestCase):


    @given("I consumed (?P<units>.+) units in a month")
    def step_impl1(context, units):
        object_bill.set_units(units)


    @when("the state ABC electricity bill gets generated")
    def step_impl2(context):
        object_bill.calculate_slab1_total()


    @then("the total energy charges as amounted to Rs\.(?P<slab1total>.+)")

    def step_impl3(context,slab1total):
        total_charges_input= slab1total
        Bill_Total = object_bill.get_energy_charges()
        #print(total_charges_input,Bill_Total)

        TestCase.assertEqual(TestCase,total_charges_input,Bill_Total)
        """if(float(total_charges_input) == float(Bill_Total)):
            print("feature example",total_charges_input,"methodcalculated charges",Bill_Total)
        else:
            print("Slabcharges provided incorrect")"""






