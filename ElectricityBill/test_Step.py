from unittest import TestCase
from ElectricityBillCalculation import ElectricityBill

class Test(TestCase):
    def test_energy_charges_calculation_for_units_less_than_50(self):
        ElectricityBill.set_units(self,40)
        Bill_Total = ElectricityBill.calculate_slab1_total(self)
        self.assertEqual(Bill_Total,162.00)

    def test_energy_charges_calculation_for_units_less_than_0(self):
            ElectricityBill.set_units(self, -1)
            Bill_Total = ElectricityBill.calculate_slab1_total(self)
            self.assertEqual(Bill_Total, "Units can't be less than zero")

    def test_energy_charges_calculation_for_units_greater_than_50(self):
        ElectricityBill.set_units(self, 51)
        Bill_Total = ElectricityBill.calculate_slab1_total(self)
        self.assertEqual(Bill_Total, "Upcoming feature")

