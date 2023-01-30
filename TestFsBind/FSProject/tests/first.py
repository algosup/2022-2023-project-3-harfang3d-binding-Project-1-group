import lib

test_fsharp = '''\

open System
open NUnit.Framework
open my_test

[<TestFixture>]
type Test() =
	[<Test>] member this.Test1() =
		let v2 = Vector2(1.0, 2.0)
        let res = distanceTo(v2)
		Assert.AreEqual(res, 3.0)

        let v2 = Vector2(1.0, 2.0)
        let res2 = percentDistance(v2, 0.5)
		Assert.AreEqual(res2, 1.5)
'''