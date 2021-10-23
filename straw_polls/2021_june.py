import add_macro

doc = add_macro.Document('../macros.yaml', value=202106)

# cwg motion 2: if consteval
doc.add_language(name='__cpp_if_consteval', papers='P1938R3')

# lwg motion 4: out_ptr
doc.add_library(name='__cpp_lib_out_ptr', papers='P1132R7', headers='memory')

# lwg motion 5: constexpr type_info::operator==
doc.add_library(name='__cpp_lib_constexpr_typeinfo',
    papers='P1328R1', headers='typeinfo')

# lwg motion 6: strstream replacement
doc.add_library(name='__cpp_lib_spanstream',
    papers='P0448R4', headers='spanstream')

# lwg motion 7: iterator pair constructors
doc.add_library(name='__cpp_lib_adaptor_iterator_pair_constructor',
    papers='P1425R4', headers='stack queue')

# lwg motion 9: providing size feedback in allocator
doc.add_library(name='__cpp_lib_allocate_at_least',
    papers='P0401R6', headers='memory')

# lwg motion 10: starts_with/ends_with
doc.add_library(name='__cpp_lib_ranges_starts_ends_with'    ,
    papers='P1659R3', headers='algorithm')

# lwg motion 13: invoke_r
doc.add_library(name='__cpp_lib_invoke_r',
    papers='P2136R3', headers='functional')

# lwg motion 15: missing constexpr
doc.update_library(name='__cpp_lib_optional', papers='P2231R1')
doc.update_library(name='__cpp_lib_variant', papers='P2231R1')

# lwg motion 16: std::format improvements
doc.update_library(name='__cpp_lib_format', papers='P2216R3')

# lwg motion 19: views should not require default constructible
doc.update_library(name='__cpp_lib_ranges', papers='P2325R3')



doc.dump()
