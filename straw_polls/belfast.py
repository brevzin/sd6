import add_macro
from collections import OrderedDict

doc = add_macro.Document('macros.yaml') 

# cwg motion 8: p1907r1
doc.remove(kind='language', name='__cpp_nontype_template_parameter_class', value=201911, papers='P1907R1')
doc.update(kind='language', name='__cpp_nontype_template_args', value=201911, papers='P1907R1')

# lwg motion 1: p1917r0
doc.update(kind='library', name='__cpp_lib_constexpr_algorithms', value=201806, papers='LWG3256')
doc.update(kind='library', name='__cpp_lib_array_constexpr', value=201803, papers='LWG3257')
doc.update(kind='library', name='__cpp_lib_string_view', value=201803, papers='LWG3257')
doc.update(kind='library', name='__cpp_lib_span', value=201803, papers='LWG3274')

# lwg motion 6: p1716r3
doc.update(kind='library', name='__cpp_lib_ranges', value=201911, papers='P1716R3')

# lwg motion 7: p1869r1
doc.update(kind='library', name='__cpp_lib_jthread', value=201911, papers='P1869R1')

# lwg motion 19: p1902r2
doc.add(kind='language', name='__cpp_designated_initializers', value=201707, papers='P0329R4')
doc.update(kind='language', name='__cpp_generic_lambdas', value=201707, papers='P0428R2')
doc.add(kind='language', name='__cpp_concepts', value=201707, papers='P0734R0')
doc.update(kind='library', name='__cpp_lib_shared_ptr_arrays', value=201707, papers='P0674R1')

doc.add(kind='language', name='__cpp_constexpr_in_decltype', value=201711, papers='P0859R0')
doc.add(kind='library', name='__cpp_lib_remove_cvref', value=201711, papers='P0550R2', headers='type_traits')
doc.add(kind='library', name='__cpp_lib_syncbuf', value=201711, papers='P0053R7', headers='syncstream')
doc.add(kind='library', name='__cpp_lib_to_address', value=201711, papers='P0653R2', headers='memory')
doc.add(kind='library', name='__cpp_lib_constexpr_complex', value=201711, papers='P0415R1', headers='complex')
doc.add(kind='library', name='__cpp_lib_atomic_shared_ptr', value=201711, papers='P0718R2', headers='memory')
doc.add(kind='library', name='__cpp_lib_atomic_float', value=201711, papers='P0020R6', headers='atomic')
doc.add(kind='library', name='__cpp_lib_starts_ends_with', value=201711, papers='P0457R2', headers='string string_view')

doc.update(kind='language', name='__cpp_init_captures', value=201803, papers='P0780R2')
doc.update(kind='library', name='__cpp_lib_chrono', value=201803, papers='P0355R7')
doc.update(kind='library', name='__cpp_lib_syncbuf', value=201803, papers='P0753R2')

doc.update(kind='language', name='__cpp_constexpr', value=201806, papers='P1064R0')
doc.update(kind='library', name='__cpp_lib_array_constexpr', value=201806, papers='P1023R0')
doc.add(kind='library', name='__cpp_lib_shift', value=201806, papers='P0769R2', headers='algorithm')
doc.add(kind='library', name='__cpp_lib_type_identity', value=201806, papers='P0887R1', headers='type_traits')
doc.add(kind='library', name='__cpp_lib_nothrow_convertible', value=201806, papers='P0758R1', headers='type_traits')
doc.add(kind='library', name='__cpp_lib_int_pow2', value=201806, papers='P0556R3', headers='bit')
doc.add(kind='library', name='__cpp_lib_atomic_ref', value=201806, papers='P0019R8', headers='atomic')

doc.update(kind='language', name='__cpp_concepts', value=201811, papers='P1084R2')
doc.update(kind='language', name='__cpp_constexpr', value=201811, papers='P1002R1')
doc.update(kind='language', name='__cpp_constexpr', value=201811, papers='P1327R1')
doc.add(kind='language', name='__cpp_consteval', value=201811, papers='P1073R3')
doc.update(kind='language', name='__cpp_constexpr', value=201811, papers='P1330R0')
doc.add(kind='library', name='__cpp_lib_constexpr_memory', value=201811, papers='P1006R1', headers='memory')
doc.remove(kind='library', name='__cpp_lib_constexpr', value=201911, papers='P1902R1')
for header in ('functional', 'iterator', 'string_view', 'tuple', 'utility'):
    doc.add(kind='library', name=f'__cpp_lib_constexpr_{header}', value=201811, papers='P1032R1', headers=header)
doc.update(kind='library', name='__cpp_lib_array_constexpr', value=201811, papers='P1032R1')
doc.add(kind='library', name='__cpp_lib_unwrap_ref', value=201811, papers='P0318R1', headers='type_traits')
doc.add(kind='library', name='__cpp_lib_assume_aligned', value=201811, papers='P1007R3', headers='memory')
doc.add(kind='library', name='__cpp_lib_smart_ptr_default_init', value=201811, papers='P1020R1', headers='memory')

doc.add(kind='library', name='__cpp_lib_polymorphic_allocator', value=201902, papers='P0339R6', headers='memory')
doc.add(kind='library', name='__cpp_lib_ssize', value=201902, papers='P1227R2', headers='iterator')
# hand-editing the change for P1185R2/P1630R1
for row in doc.doc['language']:
    if row['name'] == '__cpp_impl_three_way_comparison':
       abq = OrderedDict([('value', 201711), ('papers', 'P0515R3 P0768R1')])
       kon = OrderedDict([('value', 201902), ('papers', 'P1185R2')])
       cgn = OrderedDict([('value', 201907), ('papers', 'P1630R1')])
       row['rows'] = [abq, kon, cgn]
doc.update(kind='language', name='__cpp_constexpr', value=201907, papers='P1668R1')
doc.update(kind='language', name='__cpp_concepts', value=201907, papers='P1452R2')
doc.update(kind='library', name='__cpp_lib_concepts', value=201907, papers='P1754R1')
# hand-removing the erroneous __cpp_lib_spaceship
doc.doc['library'] = [r for r in doc.doc['library'] if r['name'] != '__cpp_lib_spaceship']
doc.update(kind='library', name='__cpp_lib_three_way_comparison', value=201907, papers='P1614R2')
doc.update(kind='library', name='__cpp_lib_constexpr_functional', value=201907, papers='P1065R2')
doc.update(kind='library', name='__cpp_lib_ranges', value=201907, papers='P1035R7')

# lwg motion 20: p0883r2
doc.add(kind='library', name='__cpp_lib_atomic_value_initialization',
        value=201911, papers='P0883R2', headers='atomic memory')

# lwg motion 23: p1645r1
doc.add(kind='library', name='__cpp_lib_constexpr_numeric',
        value=201911, papers='P1645R1', headers='numeric')

doc.dump()
