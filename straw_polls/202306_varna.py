import add_macro
from collections import OrderedDict

doc = add_macro.Document('../macros.yaml', value=202306)

# cwg motion 6: P2738R1 (constexpr cast from void*: towards constexpr type-erasure)
doc.update_language(name='__cpp_constexpr', papers='P2738R1')

# cwg motion 9:  P2741R3 (User-generated static_assert messages)
doc.update_language(name='__cpp_static_assert', papers='P2741R3')

# cwg motion 10:  P2169R4 (A nice placeholder with no name)
doc.add_language(name='__cpp_placeholder_variables', papers='P2169R4')

# lwg motion 1: P2910R0 (C++ Standard Library Issues to be moved in Varna, Jun. 2023)
doc.update_library(name='__cpp_lib_allocate_at_least', papers='LWG3887')

# lwg motion 2:  P2497R0 (Testing for success or failure of <charconv> functions)
doc.update_library(name='__cpp_lib_to_chars', papers='P2497R0')

# lwg motion 3:  P2592R3 (Hashing support for std::chrono value classes)
doc.update_library(name='__cpp_lib_chrono', papers='P2592R3')

# lwg motion 4: P2587R3 (to_string or not to_string)
doc.add_library(name='__cpp_lib_to_string', papers='P2587R3', headers='string')

# lwg motion 5:  P2562R1 (constexpr Stable Sorting)
doc.update_library(name='__cpp_lib_constexpr_algorithms', papers='P2562R1')

# lwg motion 6: P2545R4 (Read-Copy Update (RCU))
doc.add_library(name='__cpp_lib_rcu', papers='P2545R4', headers='rcu')

# lwg motion 7: P2530R3 (Hazard Pointers for C++26)
doc.add_library(name='__cpp_lib_hazard_pointer', papers='P2545R4', headers='hazard_pointer')

# lwg motion 9: P2495R3 (Interfacing stringstreams with string_view)
doc.add_library(name='__cpp_lib_sstream_from_string_view', papers='P2495R3', headers='sstream')

# lwg motion 10: P2510R3 (Formatting pointers)
# NB: custom value
doc.update_library(name='__cpp_lib_format', papers='P2510R3', value=202304)

# lwg motion 11: P2198R7 (Freestanding Feature-Test Macros and Implementation-Defined Extensions)
for macro in ('functional',
              'iterator',
              'memory',
              'operator_new',
              'ranges',
              'ratio',
              'tuple',
              'utility'):
    doc.add_library(name=f'__cpp_lib_freestanding_{macro}', papers='P2198R7', headers=macro)

# manually add the weird one
doc.doc['library'].append(OrderedDict(
    name='__cpp_lib_freestanding_feature_test_macros',
    header_list='',
    rows=OrderedDict(value=202306, papers='P2198R7')))
doc.doc['library'].sort(key=lambda d: d['name'])

# lwg motion 12: P2338R4 (Freestanding Library: Character primitives and the C library)
new_macros = {
    'char_traits': 'string',
    'charconv': 'charconv',
    'cstdlib': 'cstdlib cmath',
    'cstring': 'cstring',
    'cwchar': 'cwchar',
    'errc': 'cerrno system_error'
}
for (k, v) in new_macros.items():
    doc.add_library(name=f'__cpp_lib_freestanding_{k}', papers='P2338R4', headers=v)

# lwg motion 15: P2363R5 (Extending associative containers with the remaining heterogeneous overloads)
doc.add_library(name='__cpp_lib_associative_heterogeneous_insertion', papers='P2363R5', headers='map set unordered_map unordered_set')

# lwg motion 16: P1901R2 (Enabling the Use of weak_ptr as Keys in Unordered Associative Containers)
doc.add_library(name='__cpp_lib_smart_pointer_owner_equality', papers='P1901R2', headers='memory')

# lwg motion 17: P1885R12 (Naming Text Encodings to Demystify Them)
doc.add_library(name='__cpp_lib_text_encoding', papers='P1885R12', headers='text_encoding')

# lwg motion 18: P0792R14 (function_ref: a type-erased callable reference)
doc.add_library(name='__cpp_lib_function_ref', papers='P0792R14', headers='functional')

# lwg motion 20: P2757R3 (Type checking format args)
# NB: custom value
doc.update_library(name='__cpp_lib_format', papers='P2757R3', value=202305)


# lwg motion 21: P2637R3 (Member visit)
doc.update_library(name='__cpp_lib_variant', papers='P2637R3')
# NB: custom value
doc.update_library(name='__cpp_lib_format', papers='P2637R3', value=202306)

# lwg motion 22: P2641R4 (Checking if a union alternative is active)
doc.add_library(name='__cpp_lib_within_lifetime', papers='P2641R4', headers='type_traits')

# lwg motion 23: P1759R6 (Native handles and file streams)
doc.add_library(name='__cpp_lib_fstream_native_handle', papers='P1759R6', headers='fstream')

# lwg motion 24: P2697R1 (Interfacing bitset with string_view)
doc.add_library(name='__cpp_lib_bitset', papers='P2697R1', headers='bitset')

# lwg motion 25: P1383R2 (More constexpr for cmath and complex)
doc.update_library(name='__cpp_lib_constexpr_cmath', papers='P1383R2')
doc.update_library(name='__cpp_lib_constexpr_complex', papers='P1383R2')

# lwg motion 26: P2734R0 (Adding the new 2022 SI prefixes)
doc.add_library(name='__cpp_lib_ratio', papers='P2734R0', headers='ratio')

# lwg motion 27: P2548R6 (copyable_function)
doc.add_library(name='__cpp_lib_copyable_function', papers='P2548R6', headers='functional')

# lwg motion 28: P2714R1 (Bind front and back to NTTP callables)
for macro in ('bind_back', 'bind_front', 'not_fn'):
    doc.update_library(name=f'__cpp_lib_{macro}', papers='P2714R1')

# lwg motion 29: P2630R4 (submdspan)
doc.add_library(name='__cpp_lib_submdspan', papers='P2630R4', headers='mdspan')

doc.dump()
