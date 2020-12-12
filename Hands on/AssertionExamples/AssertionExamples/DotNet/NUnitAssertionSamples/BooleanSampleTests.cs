using NUnit.Framework;
using CodeSamplesForAssertion;

namespace NUnitAssertionSamples
{
    public class Tests
    {
        [Test]
        public void ShouldReturnFalseWhenSaturday()
        {
            var booleanSample = new BooleanSample();
            var result = booleanSample.IsWeekDay("Saturday");

            Assert.IsFalse(result);
        }

    }
}