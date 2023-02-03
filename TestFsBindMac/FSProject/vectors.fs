namespace Vectors
module VectorsProgram =
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
    [<Struct; StructLayout(LayoutKind.Sequential)>]
    type Vector2 =
        val x: double
        val y: double
        new(x: double, y: double) = { x = x; y = y }


    [<Struct; StructLayout(LayoutKind.Sequential)>]
    type Vector3 =
        val mutable x: double
        val mutable y: double
        val mutable z: double
        new(x: double, y: double, z: double) = { x = x; y = y; z = z }

    // ! Vector2 DLLImport Function
    [<DllImport("libVectors")>]
    extern double distanceToVector2(Vector2 vec1, Vector2 v2)

    [<DllImport("libVectors")>]
    extern Vector2 vectorMovementV2(Vector2 vec1, double movX, double movY)

    [<DllImport("libVectors")>]
    extern Vector2 midpointV2(Vector2 vec1, Vector2 vec2)

    [<DllImport("libVectors")>]
    extern double percentDistanceV2(Vector2 vec1, Vector2 vec2, double percent)

    [<DllImport("libVectors")>]
    extern Vector2 updateVector2(Vector2 inVector1, double newX, double newY)

    // ! Vector3 DLLImport Function
    [<DllImport("libVectors")>]
    extern double distanceToVector3(Vector3 vec1, Vector3 v2)

    [<DllImport("libVectors")>]
    extern Vector3 vectorMovementV3(Vector3 vec1, double movX, double movY, double movZ)

    [<DllImport("libVectors")>]
    extern Vector3 midpointV3(Vector3 vec1, Vector3 vec2)

    [<DllImport("libVectors")>]
    extern double percentDistanceV3(Vector3 vec1, Vector3 vec2, double percent)

    [<DllImport("libVectors")>]
    extern Vector3 updateVector3(Vector3 inVector1, double newX, double newY, double newZ)


    // ! Vector 2
    let mutable vec2_n1 = new Vector2(10.0, 10.0)
    let mutable vec2_n2 = new Vector2(20.0, 20.0)
    let percV2 = percentDistanceV2 (vec2_n1, vec2_n2, 0.5)
    let distV2 = distanceToVector2 (vec2_n1, vec2_n2)
    let midV2 = midpointV2 (vec2_n1, vec2_n2)

    // ! Vector 3
    let mutable vec3_n1 = new Vector3(10.0, 10.0, 10.0)
    let mutable vec3_n2 = new Vector3(20.0, 20.0, 20.0)
    let percV3 = percentDistanceV3 (vec3_n1, vec3_n2, 0.5)
    let distV3 = distanceToVector3 (vec3_n1, vec3_n2)
    let midV3 = midpointV3 (vec3_n1, vec3_n2)



    // ! Output for Vector2
    printfn "Vector2 number 1 values : %f, %f" vec2_n1.x vec2_n1.y
    printfn "Vector2 number 2 values : %f, %f" vec2_n2.x vec2_n2.y
    printfn "Distance between vec2_n1 and vec2_n2 : %f" distV2
    printfn "Percent distance between vec2_n1 and vec2_n2 : %f" percV2
    printfn "Midpoint between vec2_n1 and vec2_n2 : %f, %f" midV2.x midV2.y
    vec2_n2 <- vectorMovementV2 (vec2_n2, 5.0, 5.0)
    printfn "Vector2 number 2 values after movement : %f, %f" vec2_n2.x vec2_n2.y
    vec2_n2 <- updateVector2 (vec2_n2, 10.0, 10.0)
    printfn "Vector2 number 2 values after update : %f, %f" vec2_n2.x vec2_n2.y
    printfn "--------------------------------------------------"

    // ! Output for Vector3
    printfn "Vector3 number 1 values : %f, %f, %f" vec3_n1.x vec3_n1.y vec3_n1.z
    printfn "Vector3 number 2 values : %f, %f, %f" vec3_n2.x vec3_n2.y vec3_n2.z
    printfn "Distance between vec3_n1 and vec3_n2 : %f" distV3
    printfn "Percent distance between vec3_n1 and vec3_n2 : %f" percV3
    printfn "Midpoint between vec3_n1 and vec3_n2 : %f, %f, %f" midV3.x midV3.y midV3.z
    vec3_n2 <- vectorMovementV3 (vec3_n2, 5.0, 5.0, 5.0)
    printfn "Vector3 number 2 values after movement : %f, %f, %f" vec3_n2.x vec3_n2.y vec3_n2.z
    vec3_n2 <- updateVector3 (vec3_n2, 10.0, 10.0, 10.0)
    printfn "Vector3 number 2 values after update : %f, %f, %f" vec3_n2.x vec3_n2.y vec3_n2.z
    printfn "--------------------------------------------------"

