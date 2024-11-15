namespace Math.Tests;

public class MathTests
{
    [Test]
    public void TestAdd()
    {
        Assert.That(Math.Add(2, 2), Is.EqualTo(4));
    }
}