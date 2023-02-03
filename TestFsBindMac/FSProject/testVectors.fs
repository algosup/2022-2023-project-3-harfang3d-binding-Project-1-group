namespace TestsVectors

open System
open FSharpExercises.Core.Helpers
open NUnit.Framework
open Vectors

module TestVectorsProgram =
    // Ignore test template : [<Ignore("Not implemented");Test>]

    // ! Test for Vectors2
    [<Test>]
    let TestCreateVector2() =
        let expectedValue = VectorsProgram.Vector2(1.0, 2.0)
        let actualValue = VectorsProgram.Vector2(1.0, 2.0)
        AssertEquality expectedValue actualValue

    [<Test>]
    let TestDistanceToVector2() =
        let expectedValue = double(1.0)
        let actualValue = VectorsProgram.distanceToVector2(VectorsProgram.Vector2(1.0, 2.0), VectorsProgram.Vector2(2.0, 2.0))

        AssertEquality expectedValue actualValue

    [<Test>]
    let TestVector2Movement() =
        let expectedValue = VectorsProgram.Vector2(2.0, 2.0)
        let actualValue = VectorsProgram.vectorMovementV2(VectorsProgram.Vector2(1.0, 2.0), 1.0, 0.0)
        
        AssertEquality expectedValue actualValue

    [<Test>]
    let TestMidpointVector2() =
        let expectedValue = VectorsProgram.Vector2(1.5, 2.0)
        let actualValue = VectorsProgram.midpointV2(VectorsProgram.Vector2(1.0, 2.0), VectorsProgram.Vector2(2.0, 2.0))

        AssertEquality expectedValue actualValue

    [<Test>]
    let TestPercentDistanceVector2() =
        let vec1 = VectorsProgram.Vector2(10.0, 10.0)
        let vec2 = VectorsProgram.Vector2(20.0, 20.0)
        let percent = 50.0
        let expectedValue = 7.0710678118654755
        let actualValue = VectorsProgram.percentDistanceV2(vec1, vec2, percent)

        AssertEquality expectedValue actualValue

    [<Test>]
    let UpdateVector2() =
        let vec1 = VectorsProgram.Vector2(1.0, 1.0)
        let expectedVec1 = VectorsProgram.Vector2(10.0, 10.0)
        let actualValue = VectorsProgram.updateVector2(vec1, 10.0, 10.0)

        AssertEquality expectedVec1 actualValue



    // ! Test for Vectors3
    [<Test>]
    let TestCreateVector3() =
        let expectedValue = VectorsProgram.Vector3(1.0, 2.0, 3.0)
        let actualValue = VectorsProgram.Vector3(1.0, 2.0, 3.0)
        AssertEquality expectedValue actualValue

    [<Test>]
    let TestDistanceToVector3() =
        let expectedValue = double(1.0)
        let actualValue = VectorsProgram.distanceToVector3(VectorsProgram.Vector3(1.0, 2.0, 3.0), VectorsProgram.Vector3(2.0, 2.0, 3.0))
        AssertEquality expectedValue actualValue

    [<Test>]
    let TestVector3Movement() =
        let expectedValue = VectorsProgram.Vector3(2.0, 2.0, 3.0)
        let actualValue = VectorsProgram.vectorMovementV3(VectorsProgram.Vector3(1.0, 2.0, 3.0), 1.0, 0.0, 0.0)
        AssertEquality expectedValue actualValue

    [<Test>]
    let TestMidpointVector3() =
        let expectedValue = VectorsProgram.Vector3(1.5, 2.0, 3.0)
        let actualValue = VectorsProgram.midpointV3(VectorsProgram.Vector3(1.0, 2.0, 3.0), VectorsProgram.Vector3(2.0, 2.0, 3.0))
        AssertEquality expectedValue actualValue

    [<Test>]
    let TestPercentDistanceVector3() =
        let vec1 = VectorsProgram.Vector3(10.0, 10.0, 10.0)
        let vec2 = VectorsProgram.Vector3(20.0, 20.0, 20.0)
        let percent = 50.0
        let expectedValue = 8.660254037844387
        let actualValue = VectorsProgram.percentDistanceV3(vec1, vec2, percent)
        AssertEquality expectedValue actualValue

    [<Test>]
    let UpdateVector3() =
        let vec1 = VectorsProgram.Vector3(1.0, 1.0, 1.0)
        let expectedVec1 = VectorsProgram.Vector3(10.0, 10.0, 10.0)
        let actualValue = VectorsProgram.updateVector3(vec1, 10.0, 10.0, 10.0)
        AssertEquality expectedVec1 actualValue

