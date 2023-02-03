namespace TestsVectors

open System
open FSharpExercises.Core.Helpers
open NUnit.Framework
open Vectors

module TestVectorsProgram =
    // Ignore test template : [<Ignore("Not implemented");Test>]
    // ! Basic Test
    // 1+1 test to check if the test works
    [<Test>]
    let Test1Plus1() =
        let expectedValue = 2
        let actualValue = 1 + 1

        AssertEquality expectedValue actualValue

    // ! Test for Vectors2
    [<Test>]
    let TestCreateVector2() =
        let expectedValue = VectorsProgram.Vector2(1.0, 2.0)
        let actualValue = VectorsProgram.Vector2(1.0, 2.0)
        AssertEquality expectedValue actualValue

    [<Test>]
    let TestDistanceToVector2() =
        let testing = true
        let expectedValue = double(1.0)
        let actualValue = VectorsProgram.distanceToVector2(VectorsProgram.Vector2(1.0, 2.0), VectorsProgram.Vector2(2.0, 2.0))

        AssertEquality expectedValue actualValue

    [<Test>]
    let TestVectorMovement() =
        let expectedValue = VectorsProgram.Vector2(2.0, 2.0)
        let actualValue = VectorsProgram.vectorMovement(VectorsProgram.Vector2(1.0, 2.0), 1.0, 0.0)
        
        AssertEquality expectedValue actualValue

    [<Test>]
    let TestMidpoint() =
        let expectedValue = VectorsProgram.Vector2(1.5, 2.0)
        let actualValue = VectorsProgram.midpoint(VectorsProgram.Vector2(1.0, 2.0), VectorsProgram.Vector2(2.0, 2.0))

        AssertEquality expectedValue actualValue

    [<Test>]
    let TestPercentDistance() =
        let vec1 = VectorsProgram.Vector2(10.0, 10.0)
        let vec2 = VectorsProgram.Vector2(20.0, 20.0)
        let percent = 50.0
        let expectedValue = 7.0710678118654755
        let actualValue = VectorsProgram.percentDistance(vec1, vec2, percent)

        AssertEquality expectedValue actualValue

    [<Test>]
    let UpdateVector2() =
        let vec1 = VectorsProgram.Vector2(1.0, 1.0)
        let expectedVec1 = VectorsProgram.Vector2(10.0, 10.0)
        let actualValue = VectorsProgram.updateVector2(vec1, 10.0, 10.0)

        AssertEquality expectedVec1 actualValue

    

