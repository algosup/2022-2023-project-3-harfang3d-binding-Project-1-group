# FABGen - The FABulous binding Generator for CPython and Lua and Go
# Copyright (C) 2020 Thomas Simonnet

import lang.fsharp


def bind_stl(gen):
    gen.add_include('List', True)
    gen.add_include('String', True)

    class FSharpStringConverter(lang.fsharp.FSharpTypeConverterCommon):
        def __init__(self, type, *args, **kwargs) -> None:
            super().__init__(type, *args, **kwargs)
            self.fsharp_to_c_type = "string"
            self.fsharp_type = "System.String"
        # def __init__(self, type, to_c_storage_type=None, bound_name=None, from_c_storage_type=None, needs_c_storage_class=False):
        #     super().__init__(type, to_c_storage_type, bound_name, from_c_storage_type, needs_c_storage_class)

            
        def get_type_glue(self, gen, module_name):
            return ''

        def get_type_api(self, module_name):
            return ''

        def to_c_call(self, in_var, out_var_p, is_pointer=False):
            return f"let {out_var_p} = {in_var}.ToString()"

        def from_c_call(self, out_var, expr, ownership):
            return f"System.String({out_var})"

    gen.bind_type(FSharpStringConverter("System.String"))


def bind_function_T(gen, type, bound_name=None):
    class FSharpStdFunctionConverter(lang.fsharp.FSharpTypeConverterCommon):
        def get_type_glue(self, gen, module_name):
            return ""

    return gen.bind_type(FSharpStdFunctionConverter(type))


class FSharpListToStdListConverter(lang.fsharp.FSharpTypeConverterCommon):
    def __init__(self, type, T_conv):
        native_type = f"List<{T_conv.ctype}>"
        super().__init__(type, native_type, None, native_type)
        self.T_conv = T_conv

    def get_type_glue(self, gen, module_name):
        return ''
        
    def to_c_call(self, in_var, out_var_p, is_pointer):
        return ""

    def from_c_call(self, out_var, expr, ownership):
        return ""
