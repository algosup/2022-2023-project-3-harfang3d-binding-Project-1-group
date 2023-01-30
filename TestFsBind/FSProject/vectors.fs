// In F#
open System.Runtime.InteropServices

// ! Structure 
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

// ! DLLImport Function
[<DllImport("../CMake/lib/libTest56")>]
extern double Vector2_distanceTo(Vector2 pos)

[<DllImport("../CMake/lib/libTest56")>]
extern void Vector2_vectorMovement(Vector2 pos, double plusx, double plusy)

[<DllImport("../CMake/lib/libTest56")>]
extern Vector2 Vector2_midpoint(Vector2 pos)

[<DllImport("../CMake/lib/libTest56")>]
extern double Vector2_percentDistance(Vector2 pos, double percentOfDistance)

[<DllImport("../CMake/lib/libTest56")>]
extern double v2distanceTo(Vector2 pos)

[<DllImport("../CMake/lib/libTest56")>]
extern double v2percentDistance(Vector2 pos, double percentOfDistance)

[<DllImport("../CMake/lib/libTest56")>]
extern double v3distanceTo(Vector3 pos)

[<DllImport("../CMake/lib/libTest56")>]
extern double v3percentDistance(Vector3 pos, double percentOfDistance)

// ! Vector 2 
let v2 = Vector2(1.0, 2.0)
let v2DistanceTo = v2distanceTo(v2)
let v2PercentDistance = v2percentDistance(v2, 0.5)

// ! Vector 3
let v3 = Vector3(1.0, 2.0, 3.0)
let v3DistanceTo = v3distanceTo(v3)
let v3PercentDistance = v3percentDistance(v3, 0.5)

// ! Print 
printfn "Distance to origin in Vector 2: %f" v2DistanceTo
printfn "Percent distance to origin in Vector 2: %f" v2PercentDistance
printfn "Distance to origin in Vector 3: %f" v3DistanceTo
printfn "Percent distance to origin in Vector 3: %f" v3PercentDistance
