open System
open FSharpExercises.Core.Helpers
open NUnit.Framework
// import the Vectors module from the Vectors.fs file
open Vectors

[<AutoOpen>]
module TestVectorsProgram =

    // ! Basic Test
    // 1+1 test to check if the test works
    [<Test>]
    let Test1Plus1() =
        let expectedValue = 2
        let actualValue = 1 + 1

        AssertEquality expectedValue actualValue

    // ! Test for Vectors2
    [<Ignore("Not implemented");Test>]
    let TestCreateVector2() =
        let expectedValue = VectorsProgram.Vector2(1.0, 2.0)
        let actualValue = Vectors.VectorsProgram.createVector2(1.0, 2.0)

        AssertEquality expectedValue actualValue

    [<Ignore("Not implemented");Test>]
    let TestDistanceToVector2() =
        let expectedValue = 1.0
        let actualValue = Vectors.VectorsProgram.distanceToVector2(VectorsProgram.Vector2(1.0, 2.0), VectorsProgram.Vector2(2.0, 2.0))

        AssertEquality expectedValue actualValue

    [<Ignore("Not implemented");Test>]
    let TestVectorMovement() =
        let expectedValue = VectorsProgram.Vector2(2.0, 2.0)
        let actualValue = Vectors.VectorsProgram.vectorMovement(VectorsProgram.Vector2(1.0, 2.0), 1.0, 0.0)
        
        AssertEquality expectedValue actualValue

    [<Ignore("Not implemented");Test>]
    let TestMidpoint() =
        let expectedValue = VectorsProgram.Vector2(1.5, 2.0)
        let actualValue = Vectors.VectorsProgram.midpoint(VectorsProgram.Vector2(1.0, 2.0), VectorsProgram.Vector2(2.0, 2.0))

        AssertEquality expectedValue actualValue

    // [<Ignore("Not implemented");Test>]
    // let TestPercentDistance() =
    //     let expectedValue = VectorsProgram.Vector2(1.5, 2.0)
    //     let actualValue = Vectors.VectorsProgram.percentDistance(VectorsProgram.Vector2(1.0, 2.0), VectorsProgram.Vector2(2.0, 2.0), 0.5)

    //     AssertEquality expectedValue actualValue

