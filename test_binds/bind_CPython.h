// FABgen output .h
// This file is automatically generated, do not modify manually!

#pragma once

#include <cstdint>

#include <cstddef>

struct gen_type_info {
	uint32_t type_tag;
	const char *c_type;
	const char *bound_name;

	bool (*check)(PyObject *o);
	void (*to_c)(PyObject *o, void *out);
	PyObject *(*from_c)(void *obj, OwnershipPolicy policy);
};

// return a type info from its bound name
gen_type_info *gen_get_bound_type_info(uint32_t type_tag);
// return a type info from its C name
gen_type_info *gen_get_c_type_info(const char *type);
// returns the typetag of a Python object, nullptr if not a Fabgen object
uint32_t gen_get_wrapped_object_type_tag(PyObject *o);

// type API for PyObject *
bool gen_check_PyObject_ptr(PyObject *o);
void gen_to_c_PyObject_ptr(PyObject *o, void *obj);
PyObject *gen_from_c_PyObject_ptr(void *obj, OwnershipPolicy);

// type API for bool
bool gen_check_bool(PyObject *o);
void gen_to_c_bool(PyObject *o, void *obj);
PyObject *gen_from_c_bool(void *obj, OwnershipPolicy);

// type API for char
bool gen_check_char(PyObject *o);
void gen_to_c_char(PyObject *o, void *obj);
PyObject *gen_from_c_char(void *obj, OwnershipPolicy);

// type API for short
bool gen_check_short(PyObject *o);
void gen_to_c_short(PyObject *o, void *obj);
PyObject *gen_from_c_short(void *obj, OwnershipPolicy);

// type API for int
bool gen_check_int(PyObject *o);
void gen_to_c_int(PyObject *o, void *obj);
PyObject *gen_from_c_int(void *obj, OwnershipPolicy);

// type API for long
bool gen_check_long(PyObject *o);
void gen_to_c_long(PyObject *o, void *obj);
PyObject *gen_from_c_long(void *obj, OwnershipPolicy);

// type API for int8_t
bool gen_check_int8_t(PyObject *o);
void gen_to_c_int8_t(PyObject *o, void *obj);
PyObject *gen_from_c_int8_t(void *obj, OwnershipPolicy);

// type API for int16_t
bool gen_check_int16_t(PyObject *o);
void gen_to_c_int16_t(PyObject *o, void *obj);
PyObject *gen_from_c_int16_t(void *obj, OwnershipPolicy);

// type API for int32_t
bool gen_check_int32_t(PyObject *o);
void gen_to_c_int32_t(PyObject *o, void *obj);
PyObject *gen_from_c_int32_t(void *obj, OwnershipPolicy);

// type API for char16_t
bool gen_check_char16_t(PyObject *o);
void gen_to_c_char16_t(PyObject *o, void *obj);
PyObject *gen_from_c_char16_t(void *obj, OwnershipPolicy);

// type API for char32_t
bool gen_check_char32_t(PyObject *o);
void gen_to_c_char32_t(PyObject *o, void *obj);
PyObject *gen_from_c_char32_t(void *obj, OwnershipPolicy);

// type API for unsigned char
bool gen_check_unsigned_char(PyObject *o);
void gen_to_c_unsigned_char(PyObject *o, void *obj);
PyObject *gen_from_c_unsigned_char(void *obj, OwnershipPolicy);

// type API for unsigned short
bool gen_check_unsigned_short(PyObject *o);
void gen_to_c_unsigned_short(PyObject *o, void *obj);
PyObject *gen_from_c_unsigned_short(void *obj, OwnershipPolicy);

// type API for unsigned int
bool gen_check_unsigned_int(PyObject *o);
void gen_to_c_unsigned_int(PyObject *o, void *obj);
PyObject *gen_from_c_unsigned_int(void *obj, OwnershipPolicy);

// type API for unsigned long
bool gen_check_unsigned_long(PyObject *o);
void gen_to_c_unsigned_long(PyObject *o, void *obj);
PyObject *gen_from_c_unsigned_long(void *obj, OwnershipPolicy);

// type API for uint8_t
bool gen_check_uint8_t(PyObject *o);
void gen_to_c_uint8_t(PyObject *o, void *obj);
PyObject *gen_from_c_uint8_t(void *obj, OwnershipPolicy);

// type API for uint16_t
bool gen_check_uint16_t(PyObject *o);
void gen_to_c_uint16_t(PyObject *o, void *obj);
PyObject *gen_from_c_uint16_t(void *obj, OwnershipPolicy);

// type API for uint32_t
bool gen_check_uint32_t(PyObject *o);
void gen_to_c_uint32_t(PyObject *o, void *obj);
PyObject *gen_from_c_uint32_t(void *obj, OwnershipPolicy);

// type API for int64_t
bool gen_check_int64_t(PyObject *o);
void gen_to_c_int64_t(PyObject *o, void *obj);
PyObject *gen_from_c_int64_t(void *obj, OwnershipPolicy);

// type API for uint64_t
bool gen_check_uint64_t(PyObject *o);
void gen_to_c_uint64_t(PyObject *o, void *obj);
PyObject *gen_from_c_uint64_t(void *obj, OwnershipPolicy);

// type API for intptr_t
bool gen_check_intptr_t(PyObject *o);
void gen_to_c_intptr_t(PyObject *o, void *obj);
PyObject *gen_from_c_intptr_t(void *obj, OwnershipPolicy);

// type API for size_t
bool gen_check_size_t(PyObject *o);
void gen_to_c_size_t(PyObject *o, void *obj);
PyObject *gen_from_c_size_t(void *obj, OwnershipPolicy);

// type API for float
bool gen_check_float(PyObject *o);
void gen_to_c_float(PyObject *o, void *obj);
PyObject *gen_from_c_float(void *obj, OwnershipPolicy);

// type API for double
bool gen_check_double(PyObject *o);
void gen_to_c_double(PyObject *o, void *obj);
PyObject *gen_from_c_double(void *obj, OwnershipPolicy);

// type API for const char *
struct storage_const_char_ptr;
bool gen_check_const_char_ptr(PyObject *o);
void gen_to_c_const_char_ptr(PyObject *o, void *obj, storage_const_char_ptr &storage);
PyObject *gen_from_c_const_char_ptr(void *obj, OwnershipPolicy);

// type API for std::string
bool gen_check_string(PyObject *o);
void gen_to_c_string(PyObject *o, void *obj);
PyObject *gen_from_c_string(void *obj, OwnershipPolicy);

// type API for FloatValue
bool gen_check_FloatValue(PyObject *o);
void gen_to_c_FloatValue(PyObject *o, void *obj);
PyObject *gen_from_c_FloatValue(void *obj, OwnershipPolicy);

/*
	pass the get_c_type_info function from another binding to this function to resolve external types declared in this binding.
	you will need to write a wrapper to cast the type_info * pointer to the correct type if you are using a binding prefix.
	this function returns the number of unresolved external symbols.
*/
size_t gen_link_binding(gen_type_info *(*get_c_type_info)(const char *));

