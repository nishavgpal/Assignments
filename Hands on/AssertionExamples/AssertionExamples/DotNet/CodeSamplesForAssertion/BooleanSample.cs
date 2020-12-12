using System;

namespace CodeSamplesForAssertion
{
    public class BooleanSample
    {
        public bool IsWeekDay(string dayOfWeek)
        {
            if(string.Equals(dayOfWeek,"sunday",StringComparison.OrdinalIgnoreCase) || string.Equals(dayOfWeek,"saturday",StringComparison.OrdinalIgnoreCase))
            {
                return false;
            }
            return true;
        }
    }
}
