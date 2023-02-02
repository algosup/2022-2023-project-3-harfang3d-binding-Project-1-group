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

    // ! DLLImport Function

    [<DllImport("../cmake/lib/libVectors")>]
    extern Vector2 createVector2(double X, double Y)

    [<DllImport("../cmake/lib/libVectors")>]
    extern double distanceToVector2(Vector2 vec1, Vector2 v2)

    [<DllImport("../cmake/lib/libVectors")>]
    extern Vector2 vectorMovement(Vector2 vec1, double movX, double movY)

    [<DllImport("../cmake/lib/libVectors")>]
    extern Vector2 midpoint(Vector2 vec1, Vector2 vec2)

    [<DllImport("../cmake/lib/libVectors")>]
    extern double percentDistance(Vector2 vec1, Vector2 vec2, double percent)

    [<DllImport("../cmake/lib/libVectors")>]
    extern Vector2 getMyVector2()

    [<DllImport("../cmake/lib/libVectors")>]
    extern Vector2 updateVector2(Vector2 inVector1, double newX, double newY)


    // ! Vector 2
    let mutable v1 = new Vector2(10.0, 10.0)
    let mutable v2 = new Vector2(20.0, 20.0)

    let d = distanceToVector2 (v1, v2)
    let perc = percentDistance (v1, v2, 50)
    let mid = midpoint (v1, v2)

    // ! Vector 3
    // WIP

    // ! Output
    printfn "Vector v1 values : %f, %f" v1.x v1.y
    printfn "Vector v2 values : %f, %f" v2.x v2.y
    printfn "Distance between v1 and v2 : %f" d
    v2 <- vectorMovement (v2, 5.0, 4.0)
    printfn "Vector v2 values after movement : %f, %f" v2.x v2.y
    v2 <- updateVector2 (v2, 5.0, 5.0)
    printfn "Vector v2 values after update : %f, %f" v2.x v2.y

    printfn "Midpoint between v1 and v2 : %f, %f" mid.x mid.y

    printfn "Percent distance between v1 and v2 : %f" perc

