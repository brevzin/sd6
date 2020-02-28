import add_macro

doc = add_macro.Document('../macros.yaml')
PRAGUE = 202002

# lwg motion 2 (lwg issues)
doc.add(kind='library', name='__cpp_lib_constexpr_complex', value=201711, papers='P0415R1')
doc.change(kind='library', name='__cpp_lib_nothrow_convertible', args={'name':'__cpp_lib_is_nothrow_convertible'}, issue='LWG3356')
doc.change(kind='library', name='__cpp_lib_unwrap_ref', args={'header_list':'functional'}, issue='LWG3348')
doc.change(kind='language', name='__cpp_coroutines', args={'name':'__cpp_impl_coroutine'}, issue='LWG3393')
doc.add(kind='library', name='__cpp_lib_coroutine', value=201902, papers='LWG3393 P0912R5', headers='coroutine')

# lwg motion 11: p1115r3
doc.update(kind='library', name='__cpp_lib_erase_if', value=PRAGUE, papers='P1115R3')

# lwg motion 15: p1956r1
doc.update(kind='library', name='__cpp_lib_int_pow2', value=PRAGUE, papers='P1956R1')

# lwg motion 16: p1976r2
doc.update(kind='library', name='__cpp_lib_span', value=PRAGUE, papers='P1976R2')

# lwg motion 17: p1964r2
doc.update(kind='library', name='__cpp_lib_concepts', value=PRAGUE, papers='P1964R2')

# lwg motion 19: p0586r2
doc.add(kind='library', name='__cpp_lib_integer_comparison_functions', value=PRAGUE, headers='utility', papers='P0586R2')

# lwg motion 21: p1973r1
doc.change(kind='library', name='__cpp_lib_smart_ptr_default_init', args={'name':'__cpp_lib_smart_ptr_for_overwrite'}, issue='P1973R1')

doc.dump()
