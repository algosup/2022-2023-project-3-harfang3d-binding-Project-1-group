// In F#
open System.Runtime.InteropServices

open System.Diagnostics

let executeScript (fileName: string) =
    let processStartInfo = new ProcessStartInfo("/bin/bash", fileName)
    processStartInfo.UseShellExecute <- false
    processStartInfo.RedirectStandardOutput <- true
    processStartInfo.CreateNoWindow <- true
    processStartInfo.WindowStyle <- ProcessWindowStyle.Hidden
    let process = new Process()
    process.StartInfo <- processStartInfo
    process.Start()
    let output = process.StandardOutput.ReadToEnd()
    process.WaitForExit()
    output

let result = executeScript "./Requirements.sh"
printfn "Output: %s" result


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
[<DllImport("../CMake/lib/libVectors")>]
extern double v2distanceTo(Vector2 pos)

[<DllImport("../CMake/lib/libVectors")>]
extern double v2percentDistance(Vector2 pos, double percentOfDistance)

[<DllImport("../CMake/lib/libVectors")>]
extern double v3distanceTo(Vector3 pos)

[<DllImport("../CMake/lib/libVectors")>]
extern double v3percentDistance(Vector3 pos, double percentOfDistance)

// ! Vector 2 
let v2 = Vector2(1.0, 2.0)
let v2DistanceTo = v2distanceTo(v2)
let v2PercentDistance = v2percentDistance(v2, 0.5)

// ! Vector 3
let v3 = Vector3(1.0, 2.0, 3.0)
let v3DistanceTo = v3distanceTo(v3)
let v3PercentDistance = v3percentDistance(v3, 0.5)

// ! Output 
printfn "Distance to origin in Vector 2: %f" v2DistanceTo
printfn "Percent distance to origin in Vector 2: %f" v2PercentDistance
printfn "Distance to origin in Vector 3: %f" v3DistanceTo
printfn "Percent distance to origin in Vector 3: %f" v3PercentDistance
