import lib

test_fsharp = '''\

open System
open NUnit.Framework
open my_test

[<TestFixture>]
type Test() =
	[<Test>] member this.Test1() =
		let v3 = Vector2(4.2, 2.4)
        let res = distanceTo(v3)
		Assert.AreEqual(res, 5.0)

        let v3 = Vector2(4.2, 2.4)
        let res3 = percentDistance(v3, 0.5)
		Assert.AreEqual(res3, 2.5)

    [<Test>] member this.Test2() =
        let v4 = Vector2(1.0, 3.9)
        let res = distanceTo(v4)
		Assert.AreEqual(res, 4.0)

        let v4 = Vector2(1.0, 3.9)
        let res4 = percentDistance(v4, 0.75)
		Assert.AreEqual(res4, 3.0)
'''
