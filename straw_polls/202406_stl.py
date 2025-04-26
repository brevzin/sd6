import add_macro

doc = add_macro.Document('../macros.yaml', value=202406)

# CWG Polls
# 3. Apply the changes in P2747R2 (constexpr placement new) to the C++ Working Paper.
doc.update_language(name="__cpp_constexpr", papers="P2747R2")
doc.add_library(name="__cpp_lib_constexpr_new", papers="P2747R2", headers="new")

# LWG polls
# 2. Apply the changes in P2997R1 (Removing the common reference requirement from the indirectly invocable concepts) to the C++ working paper.
doc.update_library(name="__cpp_lib_ranges", papers="P2997R1")

# 3. Apply the changes in P2389R2 (dextents Index Type Parameter) to the C++ working paper.
doc.update_library(name="__cpp_lib_mdspan", papers="P2389R2")

# 4. Apply the changes in P3168R2 (Give std::optional Range Support) to the C++ working paper.
doc.add_library(name="__cpp_lib_optional_range_support", papers="P3168R2", headers="optional")

# 6. Apply the changes in P2985R0 (A type trait for detecting virtual base classes) to the C++ working paper.
doc.add_library(name="__cpp_lib_is_virtual_base_of", papers="P2985R0", headers="type_traits")

# 7. Apply the changes in P0843R14 (inplace_vector) to the C++ working paper.
doc.add_library(name="__cpp_lib_inplace_vector", papers="P0843R14", headers="inplace_vector")

# 8. Accept as a Defect Report and apply the changes in P3235R3 (std::print more types faster with less memory) to the C++ working paper.
doc.update_library(name="__cpp_lib_print", papers="P3235R3")

# 10. Apply the changes in P2075R6 (Philox as an extension of the C++ RNG engines) to the C++ working paper.
doc.add_library(name="__cpp_lib_philox_engine", papers="P2075R6", headers="random")

# 12. Apply the changes in P2300R10 (std::execution) to the C++ working paper.
doc.add_library(name="__cpp_lib_senders", papers="P2300R10", headers="execution")

doc.dump()