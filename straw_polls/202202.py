import add_macro

doc = add_macro.Document('../macros.yaml', value=202202)

# cwg motion 3
doc.update_language(name='__cpp_concepts', papers='P0848R3', value=202002)
doc.update_language(name='__cpp_constexpr', papers='P1330R0', value=202002)

# lwg motion 1
doc.remove(kind='library', name='__cpp_lib_monadic_optional', papers='LWG3621')
doc.update_library(name='__cpp_lib_optional', papers=['P0798R8', 'LWG3621'])

# lwg motion 2
doc.add_library(name='__cpp_lib_expected', papers='P0323R12', headers='expected')

# lwg motion 4
doc.add_library(name='__cpp_lib_unreachable', papers='P0627R6', headers='utility')

# lwg motion 5
doc.add_library(name='__cpp_lib_ranges_to_container', papers='P1206R7', headers='ranges')
doc.add_library(name='__cpp_lib_containers_ranges', papers='P1206R7', headers=['vector', 'list', 'forward_list', 'map', 'set', 'unordered_map', 'unordered_set', 'deque', 'queue', 'priority_queue', 'stack', 'string'])

# lwg motion 7
doc.add_library(name='__cpp_lib_reference_from_temporary', papers='P2255R2', headers='type_traits')

# lwg motion 8
doc.update_library(name='__cpp_lib_constexpr_memory', papers='P2273R3')

# lwg motion 9
doc.add_library(name='__cpp_lib_bind_back', papers='P2387R3', headers='functional') 
doc.update_library(name='__cpp_lib_ranges', papers='P2387R3')

# lwg motion 10
doc.add_library(name='__cpp_lib_ranges_iota', papers='P2440R1', headers='numeric')

# lwg motion 11
doc.add_library(name='__cpp_lib_ranges_join_with', papers='P2441R2', headers='ranges')

# lwg motion 12
doc.add_library(name='__cpp_lib_ranges_chunk', papers='P2442R1', headers='ranges')
doc.add_library(name='__cpp_lib_ranges_slide', papers='P2442R1', headers='ranges')

# lwg motion 13
doc.add_library(name='__cpp_lib_ranges_chunk_by', papers='P2443R1', headers='ranges')

doc.dump()
