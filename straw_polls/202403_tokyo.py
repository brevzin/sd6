import add_macro
from collections import OrderedDict

doc = add_macro.Document('../macros.yaml', value=202403)

# cwg motion 4: P0609R3 (Attributes for Structured Bindings) 
doc.update_language(name="__cpp_structured_bindings", papers="P0609R3")

# cwg motion 9: P2573R2 (= delete("should have a reason");)
doc.add_language(name=" __cpp_deleted_function", papers="P2573R2")

# cwg motion 10:  P2893R3 (Variadic friends)
doc.add_language(name="__cpp_variadic_friend", papers="P2893R3")

# lwg motion 6: P3107R5 (Permit an efficient implementation of std::print)
doc.update_library(name="__cpp_lib_print", papers="P3107R5")

# 8. Apply the changes in P2845R8 (Formatting of std::filesystem::path) to the C++ working paper.
doc.add_library(name="__cpp_lib_format_path", papers="P2845R8", headers="filesystem")

# 9. Apply the changes in P0493R5 (Atomic minimum/maximum) to the C++ working paper.
doc.add_library(name="__cpp_lib_atomic_min_max", papers="P0493R5", headers="atomic")

# 10. Apply the changes in P2542R8 (views::concat) to the C++ working paper.
doc.add_library(name="__cpp_lib_ranges_concat", papers="P2542R8", headers="ranges")

# 11. Apply the changes in P2591R5 (Concatenation of strings and string views) to the C++ working paper.
doc.update_library(name="__cpp_lib_string_view", papers="P2591R5")

# 12. Apply the changes in P2248R8 (Enabling list-initialization for algorithms) to the C++ working paper.
doc.add_library(name="__cpp_lib_default_template_type_for_algorithm_values", papers="P2248R8", headers=["algorithm", "ranges", "string", "deque", "list", "forward_list", "vector"])

# 13. Apply the changes in P2810R4 (is_debugger_present is_replaceable) to the C++ working paper.
doc.add_library(name="__cpp_lib_debugging", papers="P2810R4", headers="debugging")

# 14. Apply the changes in P1068R11 (Vector API for random number generation) to the C++ working paper.
doc.add_library(name="__cpp_lib_generate_random", papers="P1068R11", headers="random")

# 16. Apply the changes in P2944R3 (Comparisons for reference_wrapper) to the C++ working paper.
doc.add_library(name="__cpp_lib_reference_wrapper", papers="P2944R3", headers="functional")
doc.add_library(name="__cpp_lib_constrained_equality", papers="P2944R3", headers=["utility", "tuple", "optional", "variant"])

# 17. Apply the changes in P2642R6 (Padded mdspan layouts) to the C++ working paper.
doc.update_library(name="__cpp_lib_submdspan", papers="P2642R6")

doc.dump()
