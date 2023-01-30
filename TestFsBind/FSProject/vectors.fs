// In F#
open System.Runtime.InteropServices

[<Struct;StructLayout(LayoutKind.Sequential)>]
type Vector2 =
    val mutable x: double
    val mutable y: double
    new(x: double, y: double) = {x = x; y = y}

[<Struct;StructLayout(LayoutKind.Sequential)>]
type Vector3 =
    val mutable x: double
    val mutable y: double
    val mutable z: double
    new(x: double, y: double, z: double) = {x = x; y = y; z = z}



[<DllImport("../lib/libvectors.dylib")>]
extern double Vector2_distanceTo(Vector2 pos)


[<DllImport("../lib/libvectors.dylib")>]
extern void Vector2_vectorMovement(Vector2 pos, double plusx, double plusy)

[<DllImport("../lib/libvectors.dylib")>]
extern Vector2 Vector2_midpoint(Vector2 pos)

[<DllImport("../lib/libvectors.dylib")>]
extern double Vector2_percentDistance(Vector2 pos, double percentOfDistance)

[<DllImport("../lib/libvectors.dylib")>]
extern double v2distanceTo(Vector2 pos)

[<DllImport("../lib/libvectors.dylib")>]
extern double v2percentDistance(Vector2 pos, double percentOfDistance)

[<DllImport("../lib/libvectors.dylib")>]
extern double v3distanceTo(Vector3 pos)

[<DllImport("../lib/libvectors.dylib")>]
extern double v3percentDistance(Vector3 pos, double percentOfDistance)


let v2 = Vector2(1.0, 2.0)
let res = v2distanceTo(v2)
let res2 = v2percentDistance(v2, 0.5)
let v3 = Vector3(1.0, 2.0, 3.0)
let res3 = v3distanceTo(v3)
let res4 = v3percentDistance(v3, 0.5)
printfn "Distance to origin in Vector 2: %f" res
printfn "Percent distance to origin in Vector 2: %f" res2
printfn "Distance to origin in Vector 3: %f" res3
printfn "Percent distance to origin in Vector 3: %f" res4



// Vector2_vectorMovement(v2, 1.0, 1.0)
// printfn "Vector2 after movement: %f, %f" v2.x v2.y
