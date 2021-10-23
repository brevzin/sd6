import add_macro

doc = add_macro.Document('../macros.yaml', value=202110)

# cwg motion 2
doc.update_language(name='__cpp_constexpr', papers='P2242R3')

# cwg motion 3
doc.add_language(name='__cpp_explicit_this_parameter', papers='P0847R7')

# cwg motion 9
doc.add_language(name='__cpp_multidimensional_subscript', papers='P2128R6')

# lwg motion 2
doc.update_library(name='__cpp_lib_format', papers='P2372R3')

# lwg motion 3
doc.update_library(name='__cpp_lib_ranges', papers='P2415R2')

# lwg motion 4
doc.update_library(name='__cpp_lib_format', papers='P2418R2')

# lwg motion 6
doc.add_library(name='__cpp_lib_move_only_function',
    papers='P0288R9', headers='functional')

# lwg motion 7
doc.add_library(name='__cpp_lib_monadic_optional',
    papers='P0798R8', headers='optional')

# lwg motion 9
doc.add_library(name='__cpp_lib_string_resize_and_overwrite',
    papers='P1072R10', headers='string')

# lwg motion 11
doc.add_library(name='__cpp_lib_byteswap',
    papers='P1272R4', headers='bit')

# lwg motion 13
doc.add_library(name='__cpp_lib_associative_heterogeneous_erasure',
    papers='P2077R3', headers='map set unordered_map unordered_set')

# lwg motion 16
doc.add_library(name='__cpp_lib_ranges_zip',
    papers='P2321R2', headers='ranges tuple utility')

doc.dump()
