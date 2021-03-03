from unittest import TestCase
from ElectricityBillCalculation import ElectricityBill

class Test(TestCase):
    def test_energy_charges_calculation_for_units_less_than_50(self):
        Bill_Total = ElectricityBill.set_units(self,40)
        self.assertEqual(Bill_Total,162.00)

    def test_energy_charges_calculation_for_units_less_than_0(self):
            Bill_Total = ElectricityBill.calculate_slab1_total(-1)
            self.assertEqual(Bill_Total, "Units can't be less than zero")

    def test_energy_charges_calculation_for_units_greater_than_50(self):
            Bill_Total = ElectricityBill.calculate_slab1_total(51)
            self.assertEqual(Bill_Total, "Upcoming feature")

