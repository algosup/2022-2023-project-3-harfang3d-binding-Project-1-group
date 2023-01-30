printfn "Hello from F#"

open System.Runtime.InteropServices

[<DllImport("libMyNativeLib.dylib")>]
// extern add and factorial functions
extern int add(int a, int b) 


[<DllImport("libMyNativeLib.dylib")>]
extern int factorial(int a)


let result_sum = add(1, 2)
let result_factorial = factorial(5)


printfn "Result sum : %d" result_sum
printfn "Result factorial: %d" result_factorial






