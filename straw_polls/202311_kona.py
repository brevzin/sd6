import add_macro
from collections import OrderedDict

doc = add_macro.Document('../macros.yaml', value=202311)

# cwg motion 3: P2662R3 (Pack Indexing)
doc.add_language(name='__cpp_pack_indexing', papers='P2662R3')

# lwg motion 2: P0543R3 (Saturation arithmetic) 
doc.add_library(name="__cpp_lib_saturation_arithmetic", papers="P0543R3", headers="numeric")

# lwg motion 3: P2407R5 (Freestanding Library: Partial Classes)
for header in ("algorithm", "array", "optional", "string_view", "variant"):
    doc.add_library(name=f"__cpp_lib_freestanding_{header}", papers="P2407R5", headers=header)

# lwg motion 4: P2546R5 (Debugging Support)
doc.add_library(name="__cpp_lib_debugging", papers="P2546R5", headers="debugging")

# lwg motion 6: P2918R2 (Runtime format strings II)
doc.update_library(name="__cpp_lib_format", papers="P2918R2")

# lwg motion 7: P2909R4 (Fix formatting of code units as integers (Dude, where’s my char?))
doc.add_library(name="__cpp_lib_format_uchar", papers="P2909R4", headers="format")

# lwg motion 9: P2447R6 (std::span over an initializer list)
doc.add_library(name="__cpp_lib_span_initializer_list", papers="P2447R6", headers="span")

# lwg motion 10: P2821R5 (span.at()) 
doc.update_library(name="__cpp_lib_span", papers="P2821R5")

# lwg motion 14: P2819R2 (Add tuple protocol to complex)
doc.update_library(name="__cpp_lib_tuple_like", papers="P2819R2")

# lwg motion 15: P2937R0 (Freestanding: Remove strtok)
doc.update_library(name="__cpp_lib_freestanding_cstring", papers="P2937R0")

# lwg motion 16: P2833R2 (Freestanding Library: inout expected span)
doc.add_library(name="__cpp_lib_freestanding_expected", papers="P2833R2", headers="expected")
doc.add_library(name="__cpp_lib_freestanding_mdspan", papers="P2833R2", headers="mdspan")
doc.update_library(name="__cpp_lib_out_ptr", papers="P2833R2")
doc.update_library(name="__cpp_lib_span", papers="P2833R2")

# lwg motion 17:P2836R1 (std::basic_const_iterator should follow its underlying type’s convertibility)
doc.update_library(name="__cpp_lib_ranges_as_const", papers="P2836R1")

# lwg motion 19: P1673R13 (A free function linear algebra interface based on the BLAS)
doc.add_library(name="__cpp_lib_linalg", papers="P1673R13", headers="linalg")

doc.dump()
