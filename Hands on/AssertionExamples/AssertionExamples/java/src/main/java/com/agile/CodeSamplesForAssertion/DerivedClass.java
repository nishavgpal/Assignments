package com.agile.CodeSamplesForAssertion;

public class DerivedClass implements Animal {

    private final static DerivedClass DERIVED_CLASS = new DerivedClass();

    //Assert to verify the instance type of this class
    //Since this is a singleton, qualifies for another assert to two instances are same
    private DerivedClass() {
    }

    public static DerivedClass getInstance() {
        return DERIVED_CLASS;
    }

    public void Move() {
        throw new UnsupportedOperationException();

    }

}