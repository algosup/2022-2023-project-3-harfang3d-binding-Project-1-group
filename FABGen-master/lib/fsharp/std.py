# # FABGen - The FABulous binding Generator for Go and Go
# #	Copyright (C) 2020 Thomas Simonnet

# import lang.fsharp


# def bind_std(gen):
# 	class FSharpConstCharPtrConverter(lang.fsharp.FSharpTypeConverterCommon):
# 		def __init__(self, type, to_c_storage_type=None, bound_name=None, from_c_storage_type=None, needs_c_storage_class=False):
# 			super().__init__(type, to_c_storage_type, bound_name, from_c_storage_type, needs_c_storage_class)
# 			self.go_to_c_type = "*C.char"
# 			self.go_type = "string"
			
# 		def get_type_glue(self, gen, module_name):
# 			return ''

# 		def get_type_api(self, module_name):
# 			return ''

# 		def to_c_call(self, in_var, out_var_p, is_pointer=False):
# 			if is_pointer:
# 				out = f"{out_var_p.replace('&', '_')}1 := C.CString(*{in_var})\n"
# 				out += f"{out_var_p.replace('&', '_')} := &{out_var_p.replace('&', '_')}1\n"
# 			else:
# 				out = f"{out_var_p.replace('&', '_')}, idFin{out_var_p.replace('&', '_')} := wrapString({in_var})\n"
# 				out += f"defer idFin{out_var_p.replace('&', '_')}()\n"
# 			return out

# 		def from_c_call(self, out_var, expr, ownership):
# 			return "C.GoString(%s)" % (out_var)

# 	gen.bind_type(FSharpConstCharPtrConverter("const char *"))

# 	class FSharpBasicConverter(lang.fsharp.FSharpTypeConverterCommon):
# 		def __init__(self, type, c_type, go_type, to_c_storage_type=None, bound_name=None, from_c_storage_type=None, needs_c_storage_class=False):
# 			super().__init__(type, to_c_storage_type, bound_name, from_c_storage_type, needs_c_storage_class)
# 			self.go_to_c_type = c_type
# 			self.go_type = go_type

# 		def get_type_glue(self, gen, module_name):
# 			return ''

# 		def get_type_api(self, module_name):
# 			return ''

# 		def to_c_call(self, in_var, out_var_p, is_pointer):
# 			if is_pointer:
# 				out = f"{out_var_p.replace('&', '_')} := (*{self.go_to_c_type})(unsafe.Pointer({in_var}))\n"
# 			else:
# 				out = f"{out_var_p.replace('&', '_')} := {self.go_to_c_type}({in_var})\n"
# 			return out

# 		def from_c_call(self, out_var, expr, ownership):
# 			return f"{self.go_type}({out_var})"

# 	gen.bind_type(FSharpBasicConverter("char", "C.char", "int8"))

# 	gen.bind_type(FSharpBasicConverter("unsigned char", "C.uchar", "uint8"))
# 	gen.bind_type(FSharpBasicConverter("uint8_t", "C.uchar", "uint8"))

# 	gen.bind_type(FSharpBasicConverter("short", "C.short", "int16"))
# 	gen.bind_type(FSharpBasicConverter("int16_t", "C.short", "int16"))
# 	gen.bind_type(FSharpBasicConverter("char16_t", "C.short", "int16"))

# 	gen.bind_type(FSharpBasicConverter("uint16_t", "C.ushort", "uint16"))
# 	gen.bind_type(FSharpBasicConverter("unsigned short", "C.ushort ", "uint16"))
	
# 	gen.bind_type(FSharpBasicConverter("int32", "C.int32_t", "int32"))
# 	gen.bind_type(FSharpBasicConverter("int", "C.int32_t", "int32"))
# 	gen.bind_type(FSharpBasicConverter("int32_t", "C.int32_t", "int32"))
# 	gen.bind_type(FSharpBasicConverter("char32_t", "C.int32_t", "int32"))
# 	gen.bind_type(FSharpBasicConverter("size_t", "C.size_t", "int32"))

# 	gen.bind_type(FSharpBasicConverter("uint32_t", "C.uint32_t", "uint32"))
# 	gen.bind_type(FSharpBasicConverter("unsigned int32_t", "C.uint32_t", "uint32"))
# 	gen.bind_type(FSharpBasicConverter("unsigned int", "C.uint32_t", "uint32"))

# 	gen.bind_type(FSharpBasicConverter("int64_t", "C.int64_t", "int64"))
# 	gen.bind_type(FSharpBasicConverter("long", "C.int64_t", "int64"))

# 	gen.bind_type(FSharpBasicConverter("float32", "C.float", "float32"))
# 	gen.bind_type(FSharpBasicConverter("float", "C.float", "float32"))
	
# 	gen.bind_type(FSharpBasicConverter("intptr_t", "C.intptr_t", "uintptr"))

# 	gen.bind_type(FSharpBasicConverter("unsigned long", "C.uint64_t", "uint64"))
# 	gen.bind_type(FSharpBasicConverter("uint64_t", "C.uint64_t ", "uint64"))
# 	gen.bind_type(FSharpBasicConverter("double", "C.double", "float64"))	
	
# 	class FSharpBoolConverter(lang.fsharp.FSharpTypeConverterCommon):
# 		def __init__(self, type, to_c_storage_type=None, bound_name=None, from_c_storage_type=None, needs_c_storage_class=False):
# 			super().__init__(type, to_c_storage_type, bound_name, from_c_storage_type, needs_c_storage_class)
# 			self.go_to_c_type = "C.bool"

# 		def get_type_glue(self, gen, module_name):
# 			return ''

# 		def get_type_api(self, module_name):
# 			return ''

# 		def to_c_call(self, in_var, out_var_p, is_pointer):
# 			if is_pointer:
# 				out = f"{out_var_p.replace('&', '_')} := (*C.bool)(unsafe.Pointer({in_var}))\n"
# 			else:
# 				out = f"{out_var_p.replace('&', '_')} := C.bool({in_var})\n"
# 			return out

# 		def from_c_call(self, out_var, expr, ownership):
# 			return "bool(%s)" % (out_var)

# 	gen.bind_type(FSharpBoolConverter('bool')).nobind = True

#####

# FABGen - The FABulous binding Generator for Go and Go
#	Copyright (C) 2020 Thomas Simonnet

import lang.fsharp

def bind_std(gen):
	class FSharpConstCharPtrConverter(lang.fsharp.FSharpTypeConverterCommon):
		def __init__(self, type, to_c_storage_type=None, bound_name=None, from_c_storage_type=None, needs_c_storage_class=False):
			super().__init__(type, to_c_storage_type, bound_name, from_c_storage_type, needs_c_storage_class)
			self.fsharp_to_c_type = "string"
			self.fsharp_type = "string"
			
		def get_type_glue(self, gen, module_name):
			return ''

		def get_type_api(self, module_name):
			return ''

		def to_c_call(self, in_var, out_var_p, is_pointer=False):
			if is_pointer:
				out = f"let {out_var_p.replace('&', '_')} = {in_var} |> string\n"
				out += f"let {out_var_p.replace('&', '_')} = {out_var_p.replace('&', '_')} |> toCString\n"
			else:
				out = f"let {out_var_p.replace('&', '_')} = {in_var} |> string\n"
				out += f"let {out_var_p.replace('&', '_')} = {out_var_p.replace('&', '_')} |> toCString\n"
			return out

		def from_c_call(self, out_var, expr, ownership):
			return f"{out_var} |> fromCString"

	gen.bind_type(FSharpConstCharPtrConverter("const char*"))

	class FSharpBasicTypeConverter(lang.fsharp.FSharpTypeConverterCommon):
		def __init__(self, type, to_c_storage_type=None, bound_name=None, from_c_storage_type=None, needs_c_storage_class=False):
			super().__init__(type, to_c_storage_type, bound_name, from_c_storage_type, needs_c_storage_class)
			self.fsharp_to_c_type = type
			self.fsharp_type = type
			
		def get_type_glue(self, gen, module_name):
			return ''

		def get_type_api(self, module_name):
			return ''

		def to_c_call(self, in_var, out_var_p, is_pointer=False):
			if is_pointer:
				out = f"let {out_var_p.replace('&', '_')} = {in_var}\n"
			else:
				out = f"let {out_var_p.replace('&', '_')} = {in_var}\n"
			return out

		def from_c_call(self, out_var, expr, ownership):
			return f"{out_var}"

		
	gen.bind_type(FSharpBasicTypeConverter("char", "sbyte", "int8"))

	gen.bind_type(FSharpBasicTypeConverter("unsigned char", "byte", "uint8"))
	gen.bind_type(FSharpBasicTypeConverter("uint8_t", "byte", "uint8"))

	gen.bind_type(FSharpBasicTypeConverter("short", "int16", "int16"))
	gen.bind_type(FSharpBasicTypeConverter("int16_t", "int16", "int16"))
	gen.bind_type(FSharpBasicTypeConverter("char16_t", "int16", "int16"))

	gen.bind_type(FSharpBasicTypeConverter("uint16_t", "uint16", "uint16"))
	gen.bind_type(FSharpBasicTypeConverter("unsigned short", "uint16 ", "uint16"))

	gen.bind_type(FSharpBasicTypeConverter("int32", "int", "int32"))
	gen.bind_type(FSharpBasicTypeConverter("int", "int", "int32"))
	gen.bind_type(FSharpBasicTypeConverter("int32_t", "int", "int32"))
	gen.bind_type(FSharpBasicTypeConverter("char32_t", "int", "int32"))
	gen.bind_type(FSharpBasicTypeConverter("size_t", "int", "int32"))

	gen.bind_type(FSharpBasicTypeConverter("uint32_t", "uint32", "uint32"))
	gen.bind_type(FSharpBasicTypeConverter("unsigned int32_t", "uint32", "uint32"))
	gen.bind_type(FSharpBasicTypeConverter("unsigned int", "uint32", "uint32"))

	gen.bind_type(FSharpBasicTypeConverter("int64_t", "int64", "int64"))
	gen.bind_type(FSharpBasicTypeConverter("long", "int64", "int64"))

	gen.bind_type(FSharpBasicTypeConverter("float32", "single", "float32"))
	gen.bind_type(FSharpBasicTypeConverter("float", "single", "float32"))

	gen.bind_type(FSharpBasicTypeConverter("intptr_t", "nativeint", "uintptr"))

	gen.bind_type(FSharpBasicTypeConverter("unsigned long", "uint64", "uint64"))
	gen.bind_type(FSharpBasicTypeConverter("uint64_t", "uint64 ", "uint64"))
	gen.bind_type(FSharpBasicTypeConverter("double", "double", "float64"))

	class FSharpBoolConverter(lang.fsharp.FSharpTypeConverterCommon):
		def __init__(self, type, to_c_storage_type=None, bound_name=None, from_c_storage_type=None, needs_c_storage_class=False):
			super().__init__(type, to_c_storage_type, bound_name, from_c_storage_type, needs_c_storage_class)
			self.fsharp_to_c_type = "bool"
			
		def get_type_glue(self, module_name: str) -> str:
			return ''

		def get_type_api(self, module_name: str) -> str:
			return ''

		def to_c_call(self, in_var: str , out_var_p: str, is_pointer=False) -> str:
			if is_pointer:
				out = f"let {out_var_p.replace('&', '_')} = (&{self.fsharp_to_c_type} {in_var})\n"
			else:
				out = f"let {out_var_p.replace('&', '_')} = {self.fsharp_to_c_type} {in_var}\n"
			return out

		def from_c_call(self, out_var, expr, ownership):
			return "bool(%s)" % out_var

	gen.bind_type(FSharpBoolConverter("bool"))
