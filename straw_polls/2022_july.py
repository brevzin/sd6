import add_macro

doc = add_macro.Document('../macros.yaml', value=202207)

# cwg motion 3: P2468R2 (The Equality Operator You Are Looking For) as a Defect Report
# The paper does not propose a feature-test macro.

# cwg motion 4: P2327R1 (De-deprecating volatile compound operations) as a Defect Report
# The paper does not propose a feature-test macro.

# cwg motion 5: P2437R1 (Support for #warning)
# The paper does not propose a feature-test macro.

# cwg motion 6: P2362R3 (Remove non-encodable wide character literals and multicharacter wide character literals)
# The paper does not propose a feature-test macro.

# cwg motion 7: P2324R2 (Labels at the end of compound statements (C compatibility))
# The paper does not propose a feature-test macro.

# cwg motion 8: P2290R3 (Delimited escape sequences)
# The paper does not propose a feature-test macro.

# cwg motion 9: P2448R2 (Relaxing some constexpr restrictions)
doc.update_language(name='__cpp_constexpr', papers='P2448R2')

# cwg motion 10: P2266R3 (Simpler implicit move)
doc.add_language(name='__cpp_implicit_move', papers='P2266R3')

# cwg motion 11: P2071R2 (Named universal character escapes)
doc.add_language(name='__cpp_named_character_escapes', papers='P2071R2')

# cwg motion 12: P1169R4 (static operator())
doc.add_language(name='__cpp_static_call_operator', papers='P1169R4')

# cwg motion 13: P2280R4 (Using unknown pointers and references in constant expressions) as a Defect Report
# The paper does not propose a feature-test macro.

# cwg motion 14: P1467R9 (Extended floating-point types and standard names)
# The paper does not propose a feature-test macro.

# cwg motion 15: P2493R0 (Missing feature test macros for C++20 core papers) as a Defect Report

# cwg motion 16: P2582R1 (Wording for class template argument deduction from inherited constructors)
# The paper does not propose a feature-test macro.

# cwg motion 17: P1774R8 (Portable assumptions)
# cwg issue 2615: Missing __has_cpp_attribute(assume)
doc.add(kind='attributes', name='assume', papers='P1774R8 CWG2615')

# cwg motion 18: P2295R6 (Support for UTF-8 as a portable source file encoding)
# The paper does not propose a feature-test macro.

# cwg motion 19: P2513R3 (char8_t Compatibility and Portability Fix) as a Defect Report
doc.update_language(name='__cpp_char8_t', papers='P2513R3')

# cwg motion 20: P2460R2 (Relax requirements on wchar_t to match existing practices) as a Defect Report
# The paper does not propose a feature-test macro.

# cwg motion 21: P2579R0 (Mitigation strategies for P2036 "Changing scope for lambda trailing-return-type") as a Defect Report
# The paper does not propose a feature-test macro.

# lwg motion 2: P0009R18 (MDSPAN)
# lwg motion 3: P2599R2 (index_type & size_type in mdspan)
# lwg motion 4: P2604R0 (mdspan: rename pointer and contiguous)
# lwg motion 5: P2613R1 (Add the missing empty to mdspan)
doc.add_library(name='__cpp_lib_mdspan', papers='P0009R18 P2599R2 P2604R0 P2613R1', headers='mdspan')

# lwg motion 6: P0429R9 (A Standard flat_map)
doc.add_library(name='__cpp_lib_flat_map', papers='P0429R9', headers='flat_map')

# lwg motion 7: P1222R4 (A standard flat_set)
# lwg issue 3751: Missing feature macro for flat_set
doc.add_library(name='__cpp_lib_flat_set', papers='P1222R4 LWG3751', headers='flat_set')

# lwg motion 8: P1223R5 (find_last)
doc.add_library(name='__cpp_lib_find_last', papers='P1223R5', headers='algorithm')

# lwg motion 9: P1642R11 (Freestanding Library: Easy [utilities], [ranges], and [iterators])
# The paper does not propose a feature-test macro.

# lwg motion 10: P1899R3 (stride_view)
doc.add_library(name='__cpp_lib_ranges_stride', papers='P1899R3', headers='ranges')

# lwg motion 11: P2093R14 (Formatted output)
doc.add_library(name='__cpp_lib_print', papers='P2093R14', headers='print ostream')

# lwg motion 12: P2165R4 (Compatibility between tuple and tuple-like objects)
doc.add_library(name='__cpp_lib_tuple_like', papers='P2165R4', headers='utility tuple map unordered_map')

# lwg motion 13: P2278R4 (cbegin should always return a constant iterator)
doc.add_library(name='__cpp_lib_ranges_as_const', papers='P2278R4', headers='ranges')

# lwg motion 14: P2286R8 (Formatting Ranges)
# lwg issue 3750: Too many papers bump __cpp_lib_format
doc.add_library(name='__cpp_lib_format_ranges', papers='P2286R8 LWG3750', headers='format')

# lwg motion 15: P2291R3 (Add Constexpr Modifiers to Functions to_chars and from_chars for Integral Types in Header)
doc.add_library(name='__cpp_lib_constexpr_charconv', papers='P2291R3', headers='charconv')

# lwg motion 16: P2302R4 (std::ranges::contains)
doc.add_library(name='__cpp_lib_ranges_contains', papers='P2302R4', headers='algorithm')

# lwg motion 17: P2322R6 (ranges::fold)
doc.add_library(name='__cpp_lib_ranges_fold', papers='P2322R6', headers='algorithm')

# lwg motion 18: P2374R4 (views::cartesian_product)
# lwg motion 19: P2540R1 (Empty Product for certain Views)
doc.add_library(name='__cpp_lib_ranges_cartesian_product', papers='P2374R4 P2540R1', headers='ranges')

# lwg motion 20: P2404R3 (Move-only types for equality_comparable_with, totally_ordered_with, and three_way_comparable_with)
doc.update_library(name='__cpp_lib_concepts', papers='P2404R3')
for row in doc.doc['library']:
    if row['name'] == '__cpp_lib_concepts':
        row['header_list'] = 'compare concepts'

# lwg motion 21: P2408R5 (Ranges iterators as inputs to non-Ranges algorithms)
doc.add_library(name='__cpp_lib_algorithm_iterator_requirements', papers='P2408R5', headers='algorithm numeric memory')

# lwg motion 22: P2417R2 (A more constexpr bitset)
doc.add_library(name='__cpp_lib_constexpr_bitset', papers='P2417R2', headers='bitset')

# lwg motion 23: P2419R2 (Clarify handling of encodings in localized formatting of chrono types)
doc.update_library(name='__cpp_lib_format', papers='P2419R2')

# lwg motion 24: P2438R2 (std::string::substr() &&)
# The paper does not propose a feature-test macro.

# lwg motion 25: P2446R2 (views::as_rvalue)
doc.add_library(name='__cpp_lib_ranges_as_rvalue', papers='P2446R2', headers='ranges')

# lwg motion 26: P2465R3 (Standard Library Modules std and std.compat)
doc.doc['library'].append({'name': '__cpp_lib_modules', 'rows': {'value': 202207, 'papers': 'P2465R3'}})

# lwg motion 27: P2445R1 (std::forward_like)
doc.add_library(name='__cpp_lib_forward_like', papers='P2445R1', headers='utility')

# lwg motion 28: P2467R1 (Support exclusive mode for fstreams)
doc.add_library(name='__cpp_lib_ios_noreplace', papers='P2467R1', headers='ios')

# lwg motion 29: P2474R2 (views::repeat)
doc.add_library(name='__cpp_lib_ranges_repeat', papers='P2474R2', headers='ranges')

# lwg motion 30: P2494R2 (Relaxing range adaptors to allow for move only types)
doc.update_library(name='__cpp_lib_ranges', papers='P2494R2')

# lwg motion 31: P2499R0 (string_view range constructor should be explicit)
# The paper does not propose a feature-test macro.

# lwg motion 32: P2502R2 (std::generator: Synchronous Coroutine Generator for Ranges)
doc.add_library(name='__cpp_lib_generator', papers='P2502R2', headers='generator')

# lwg motion 33: P2508R1 (Exposing std::basic-format-string<charT, Args...>)
doc.update_library(name='__cpp_lib_format', papers='P2508R1')

# lwg motion 34: P2517R1 (Add a conditional noexcept specification to std::apply)
# The paper does not propose a feature-test macro.

# lwg motion 35: P2520R0 (move_iterator<T*> should be a random access iterator)
doc.add_library(name='__cpp_lib_move_iterator_concept', papers='P2520R0', headers='iterator')

# lwg motion 36: P2549R1 (std::unexpected should have error() as member accessor)
# The paper does not propose a feature-test macro.

# lwg motion 37: P2585R1 (Improving default container formatting)
# lwg issue 3750: Too many papers bump __cpp_lib_format
doc.update_library(name='__cpp_lib_format_ranges', papers='P2585R1 LWG3750')

# lwg motion 38: P2590R2 (Explicit lifetime management)
doc.add_library(name='__cpp_lib_start_lifetime_as', papers='P2590R2', headers='memory')


doc.dump()
