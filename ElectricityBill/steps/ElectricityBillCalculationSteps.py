from behave import *

use_step_matcher("re")


@given("I consumed (?P<units>.+) units in a month")
def step_impl(context, units):
    raise NotImplementedError(u'STEP: Given I consumed <units> units in a month')


@when("the state ABC electricity bill gets generated")
def step_impl(context):
    raise NotImplementedError(u'STEP: When the state ABC electricity bill gets generated')


@then("the total energy charges as amounted to Rs\.(?P<slab1total>.+)")
def step_impl(context, slab1total):
    raise NotImplementedError(u'STEP: Then the total energy charges as amounted to Rs.<slab1total>')