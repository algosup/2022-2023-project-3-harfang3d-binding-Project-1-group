namespace Vectors

module Tests =

    open System
    open Xunit
    open Vectors

    [<Fact>]
    let ``My test`` () = Assert.True(true)

    [<Fact>]
    let ``Test createVector2`` () =
        let vec = Vectors.createVector2 (1.0, 2.0)
        Assert.Equal(1.0, vec.x)
        Assert.Equal(2.0, vec.y)
