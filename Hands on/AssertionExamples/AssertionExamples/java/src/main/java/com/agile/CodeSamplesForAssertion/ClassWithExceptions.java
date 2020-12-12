package com.agile.CodeSamplesForAssertion;


public class ClassWithExceptions {

    //This could qualify for two exception tests.
    //1. Assert it throws the correct exception. 2. Assert correct exception message
	public String sayHello(String name) throws Exception{
		if (name == null)
            {
                throw new NullPointerException("Name is Null");
            }
            return "Hello " + name;

	}

}
