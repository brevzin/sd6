import add_macro

doc = add_macro.Document('../macros.yaml', value=202211)

# cwg motion 7: P2589R1 (static operator[])
doc.update_language(name='__cpp_multidimensional_subscript', papers='P2589R1')

# cwg motion 8: P2647R1 (Permitting static constexpr variables in constexpr functions)
doc.update_language(name='__cpp_constexpr', papers='P2647R1')

# cwg motion 9: P2564R3 (consteval needs to propagate up)
doc.update_language(name='__cpp_consteval', papers='P2564R3')

# lwg motion 7: P2703R0 (C++ Standard Library Ready Issues to be moved in Kona, Nov. 2022)
def lwg3792():
    with doc.row_for(kind='library', name='__cpp_lib_constexpr_algorithms') as row:
        if "utility" not in row["header_list"]:
            row["header_list"] = f"{row['header_list']} utility"
            row["rows"][-1]["papers"] += " LWG3792"
lwg3792()

# lwg motion 9: P2602R2 (Poison Pills are Too Toxic)
doc.update_library(name='__cpp_lib_ranges', papers='P2602R2')

# lwg motion 13 P2505R5 (Monadic Functions for std::expected)
doc.update_library(name='__cpp_lib_expected', papers='P2505R5')

doc.dump()
