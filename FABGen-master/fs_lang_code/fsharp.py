import gen


class FSharpTypeConverterCommon(gen.TypeConverter):
    def __init__(self, type, to_c_storage_type=None, bound_name=None, from_c_storage_type=None, needs_c_storage_class=False):
        super().__init__(type, to_c_storage_type, bound_name, from_c_storage_type, needs_c_storage_class)
    
    def get_type_api(self, module_name):
        return ''
    
    def to_c_call(self, in_var, out_var_p):
        return ''
    
    def from_c_call(self, out_var, expr, ownership):
        return ''
    
    def check_call(self, in_var):
        return ''
    
    def get_type_glue(self, gen, module_name):
        return ''
