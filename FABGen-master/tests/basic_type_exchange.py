import lib


def bind_test(gen):
	gen.start('my_test')

	lib.bind_defaults(gen)

	# inject test code in the wrapper
	gen.insert_code('''\
// basic interoperability
int return_int() { return 8; }
float return_float() { return 8.f; }
const char *return_const_char_ptr() { return "const char * -> string"; }

static int static_int = 9;

int *return_int_by_pointer() { return &static_int; }
int &return_int_by_reference() { return static_int; }

// argument passing
int add_int_by_value(int a, int b) { return a + b; }
int add_int_by_pointer(int *a, int *b) { return *a + *b; }
int add_int_by_reference(int &a, int &b) { return a + b; }
\n''', True, False)

	gen.add_include('string', True)

	gen.bind_function('return_int', 'int', [])
	gen.bind_function('return_float', 'float', [])
	gen.bind_function('return_const_char_ptr', 'const char *', [])

	gen.bind_function('return_int_by_pointer', 'int*', [])
	gen.bind_function('return_int_by_reference', 'int&', [])

	gen.bind_function('add_int_by_value', 'int', ['int a', 'int b'])
	gen.bind_function('add_int_by_pointer', 'int', ['int *a', 'int *b'])
	gen.bind_function('add_int_by_reference', 'int', ['int &a', 'int &b'])

	gen.finalize()
	return gen.get_output()


test_python = '''\
import my_test

assert my_test.return_int() == 8
assert my_test.return_float() == 8
assert my_test.return_const_char_ptr() == "const char * -> string"

assert my_test.return_int_by_pointer() == 9
assert my_test.return_int_by_reference() == 9

assert my_test.add_int_by_value(3, 4) == 7
assert my_test.add_int_by_pointer(3, 4) == 7
assert my_test.add_int_by_reference(3, 4) == 7
'''

test_lua = '''\
my_test = require "my_test"

assert(my_test.return_int() == 8)
assert(my_test.return_float() == 8)
assert(my_test.return_const_char_ptr() == "const char * -> string")

assert(my_test.return_int_by_pointer() == 9)
assert(my_test.return_int_by_reference() == 9)

assert(my_test.add_int_by_value(3, 4) == 7)
assert(my_test.add_int_by_pointer(3, 4) == 7)
assert(my_test.add_int_by_reference(3, 4) == 7)
'''


test_go = '''\
package mytest

import (
	"testing"
	"github.com/stretchr/testify/assert"
)

// Test ...
func Test(t *testing.T) {
	assert.Equal(t, ReturnInt(), 8, "should be the same.")
	assert.Equal(t, ReturnFloat(), float32(8), "should be the same.")
	assert.Equal(t, ReturnConstCharPtr(), "const char * -> string", "should be the same.")

	assert.Equal(t, *ReturnIntByPointer(), 9, "should be the same.")
	assert.Equal(t, *ReturnIntByReference(), 9, "should be the same.")
	
	assert.Equal(t, AddIntByValue(3, 4), 7, "should be the same.")
	a := int32(3)
	b := int32(4)
	assert.Equal(t, AddIntByPointer(&a, &b), 7, "should be the same.")
	assert.Equal(t, AddIntByReference(&a, &b), 7, "should be the same.")
}
'''

test_fsharp = '''\
namespace FSharpTest

open System.Runtime.InteropServices
open FSharpExercises.Core.Helpers
open NUnit.Framework
open System
open System.IO

module TestReturnInt =

    let currentDirectory = System.Environment.CurrentDirectory
    let strPath = Path.Combine(currentDirectory, "my_test.dll")

    [<Literal>]
    let str = @""

    [<DllImport(str)>]
    extern int MyTestReturnInt()

    [<DllImport(str)>]
    extern float MyTestReturnFloat()

    [<DllImport(str)>]
    extern string MyTestReturnConstCharPtr()

    [<DllImport(str)>]
    extern int MyTestReturnIntByPointer()

    [<DllImport(str)>]
    extern int MyTestReturnIntByReference()

    [<DllImport(str)>]
    extern int MyTestAddIntByValue(int a, int b)

    [<DllImport(str)>]
    extern int MyTestAddIntByPointer(int a, int b)

    [<DllImport(str)>]
    extern int MyTestAddIntByReference(int a, int b)

    [<Test>]
    let TestReturnInt() = 
        let myInt = MyTestReturnInt()
        AssertEquality 8 myInt

    [<Test>]
    let TestReturnFloat() = 
        let myFloat = MyTestReturnFloat()
        AssertEquality 8 myFloat

    [<Test>]
    let TestReturnConstCharPtr() =
        let myString = MyTestReturnConstCharPtr()
        AssertEquality "const char * -> string" myString
    
    [<Test>]
    let TestReturnIntByPointer() =
        let myInt = MyTestReturnIntByPointer()
        AssertEquality 9 myInt
    
    [<Test>]
    let TestReturnIntByReference() =
        let myInt = MyTestReturnIntByReference()
        AssertEquality 9 myInt

    [<Test>]
    let TestAddIntByValue() =
        let myInt = MyTestAddIntByValue(3, 4)
        AssertEquality 7 myInt

    [<Test>]
    let TestAddIntByPointer() =
        let myInt = MyTestAddIntByPointer(3, 4)
        AssertEquality 7 myInt

    [<Test>]
    let TestAddIntByReference() =
        let myInt = MyTestAddIntByReference(3, 4)
        AssertEquality 7 myInt
        
'''