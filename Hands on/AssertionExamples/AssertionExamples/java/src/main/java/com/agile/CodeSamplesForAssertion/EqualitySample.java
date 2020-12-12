package com.agile.CodeSamplesForAssertion;

import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

public class EqualitySample {

	//String equality. assertEquals() or assertThat()
	public String getWelcomeMessage(String yourName) {
		return "Welcome " + yourName;
	}

	//This function could be tested using assertNotSame() or assertThat()
	public String getTextAppendWithRandomNumber(String someText) {

        Random random = new Random();

		return someText + random.nextInt();
	}

	//Integer equality. assertEquals()
	public int addTwoNumbers(int firstNumber, int secondNumber) {
		return firstNumber + secondNumber;
	}

	 //Double/Float equality. assertEquals(). Figure out how to add tolerance/delta in assertions
	public double getMaturityAmount(double principal, double interest) {

        DecimalFormat decimalFormat = new DecimalFormat("#.##");

        double amount = principal + (principal * interest / 100);
        
        return Double.parseDouble(decimalFormat.format(amount));
	}

	//This could qualify for two tests. 1. Not Empty test and 2. List equality
	public List<String> weekendDays() {

        List<String> weekendDaysList = new ArrayList<String>();

        weekendDaysList.add("Saturday");
        weekendDaysList.add("Sunday");

		return weekendDaysList;
	}

	public String getColorValue(final String key){
        Map<String, String> colorsMap = new HashMap<String, String>();
        colorsMap.put("key1", "White");
        colorsMap.put("key2", "Red");
        colorsMap.put("key3", "Green");
        return colorsMap.get(key);
	}
	
	public String[] getFruitArray(){
		String[] fruitsArray = {"apple", "mango", "grape"};
		return fruitsArray;
	}
	
}
