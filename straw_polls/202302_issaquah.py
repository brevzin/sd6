import add_macro

doc = add_macro.Document('../macros.yaml', value=202302)

# cwg motion 1-6:  P2796R0 (Core Language Working Group "ready" Issues for the February, 2023 meeting)
doc.update_language(name='__cpp_range_based_for', papers='P2718R0 P2644R1 CWG2569')

# lwg motion 2-4: P2789R0 (C++ Standard Library Issues to be moved in Issaquah, Feb. 2023)
def lwg3807():
    with doc.row_for(kind='library', name='__cpp_lib_find_last') as row:
        row['name'] = '__cpp_lib_ranges_find_last'
        row['rows'][-1]['papers'] += " LWG3807"
lwg3807()

# lwg motion 6:  P2164R9 (views::enumerate)
doc.add_library(name='__cpp_lib_ranges_enumerate', papers='P2164R9', headers='ranges')

# lwg motion 8: P2609R3 (Relaxing Ranges Just A Smidge)
doc.update_library(name='__cpp_lib_ranges', papers='P2609R3')

# lwg motion 14:  P2674R1 (A trait for implicit lifetime types)
doc.add_library(name='__cpp_lib_is_implicit_lifetime', papers='P2674R1', headers='type_traits')

# lwg motion 15: P2655R3 (common_reference_t of reference_wrapper Should Be a Reference Type)
doc.add_library(name='__cpp_lib_common_reference', papers='P2655R3', headers='type_traits')
doc.add_library(name='__cpp_lib_common_reference_wrapper', papers='P2655R3', headers='functional')

# lwg motion 19:  P2588R3 (barrier’s phase completion guarantees)
doc.update_library(name='__cpp_lib_barrier', papers='P2588R3')

doc.dump()
