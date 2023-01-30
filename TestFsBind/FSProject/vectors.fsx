// In F#
open System.Runtime.InteropServices

[<Struct;StructLayout(LayoutKind.Sequential)>]
type Vector2 =
    val mutable x: double
    val mutable y: double
    new(x: double, y: double) = {x = x; y = y}

[<DllImport("libvectors2.dylib", EntryPoint="__ZN7Vector210distanceToES_")>]
extern double Vector2_distanceTo(Vector2 pos)


[<DllImport("libvectors2.dylib")>]
extern void Vector2_vectorMovement(Vector2 pos, double plusx, double plusy)

[<DllImport("libvectors2.dylib")>]
extern Vector2 Vector2_midpoint(Vector2 pos)

[<DllImport("libvectors2.dylib")>]
extern double Vector2_percentDistance(Vector2 pos, double percentOfDistance)

[<DllImport("libvectors2.dylib")>]
extern double distanceTo(Vector2 pos)

[<DllImport("libvectors2")>]
extern double percentDistance(Vector2 pos, double percentOfDistance)


let v2 = Vector2(1.0, 2.0)
let res = distanceTo(v2)
let res2 = percentDistance(v2, 0.5)
printfn "Distance to origin: %f" res
printfn "Percent distance to origin: %f" res2



// Vector2_vectorMovement(v2, 1.0, 1.0)
// printfn "Vector2 after movement: %f, %f" v2.x v2.y
