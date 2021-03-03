# Created by m.nisha at 3/3/2021
Feature: Energy Charges
As a user want that this feature should calculate the Energy Charges based on the units billed to the Domestic Electricity Consumer for the state ABC
With A (Slabs) and B (Rate)
Energy Charges C (Charges) = A (Unit Bifurcation) x B (Rate)

Scenario Outline:Calculate the Energy Charges for the Domestic Electricity Consumer in Slab 1 for consumption between 1 to 50 units
       Given I consumed <units> units in a month
       When the state ABC electricity bill gets generated
       Then the total energy charges as amounted to Rs.<slab1total>

       Examples:
              | units | slab1total |
              | 1     | 4.05       |
              | 40    | 162.00     |
              | 50    | 202.50     |
