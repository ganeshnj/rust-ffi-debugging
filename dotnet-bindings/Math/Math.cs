using System.Runtime.InteropServices;

namespace Math;

public static class Math
{
    static Math()
    {
        // if debugger attached, print the pid
        if (System.Diagnostics.Debugger.IsAttached)
        {
            System.Console.WriteLine(System.Diagnostics.Process.GetCurrentProcess().Id);
        }
    }
    public static int Add(int a, int b)
    {
        return rs_add(a, b);
    }

    [DllImport("/Users/ganesh.jangir/dd/rust-ffi-debugging/math/target/debug/libmath.dylib")]
    private static extern int rs_add(int left, int right);
}