package com.agile.CodeSamplesForAssertion;

public class BooleanSamples {

	// This could qualify for multiple tests.
	// 1. Assert it for Saturday/Sunday 2. Assert it for any valid weekday
	public boolean isWeekDay(String dayOfWeek) {

		if ("Saturday".equalsIgnoreCase(dayOfWeek) || "Sunday".equalsIgnoreCase(dayOfWeek)) {
			return false;
		}
		return true;

	}

}
