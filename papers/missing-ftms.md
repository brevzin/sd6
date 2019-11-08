---
title: Missing feature-test macros 2017-2019
document: P1902R1
date: today
audience: CWG, LWG
author:
    - name: Barry Revzin
      email: <barry.revzin@gmail.com>
toc: true
---

# Revision history

R0 [@P1902R0] of this paper was presented to SG10 in Belfast in November, 2019.
Some of the macros were renamed to be more consistent with other design decisions, and a couple more were added for papers that were missed. 
We also came up with a [constexpr policy](#constexpr-policy).

# Introduction

When [@P0941R2] was adopted both into the standard and as policy, that paper
thoroughly went through all the relevant features that existed at the time. At
the Cologne meeting in July 2019, we added signs in both the Core and Library
Working Group rooms to ensure that papers in flight did not forget - they had to
either explicitly adopt a new feature-test macro or explicitly state why they
did not need one.

In the intervening time-frame, several meetings' worth of papers were adopted
which did not have a feature-test macro. The goal is this paper is to go through
all of those papers and add the missing ones.

As a general note, [@SD6] has been updated and is current through Cologne and
through a few LWG issues following that.

## NB Comments

This paper resolves the following NB comments:

- [FI015](https://github.com/cplusplus/nbballot/issues/15)
- [GB146](https://github.com/cplusplus/nbballot/issues/145): add a macro for
concepts.
- [GB147](https://github.com/cplusplus/nbballot/issues/146): add a macro for
`consteval`.
- [US150](https://github.com/cplusplus/nbballot/issues/149): add a macro for
familiar syntax for generic lambdas.
- [US167](https://github.com/cplusplus/nbballot/issues/165): add a macro for
non-member `ssize()`
- [DE168](https://github.com/cplusplus/nbballot/issues/166): providing a 
consistent policy for `constexpr`

# `constexpr` policy

In the previous draft of this paper, there was a discussion on whether or not
we want fine-grained or coarse-grained feature test macros for all the constexpr
extensions.

The issue is: we keep extending both the language and the library functionality
for what you can do at constant evaluation time. How do we test for those? If
we only have coarse-grained macros, this is hostile to implementers (because it
requires a strict, linear adoption of features, some of which may be both large
and unrelated) and this is hostile to users (because they check this one
huge umbrella macro). If we have overly fine macros, this is harmful to the
implementation as it adds more macros that compilers need to synthesize, and
just adds more things that we have to check.

The policy discussed and agreed upon by SG10 in Belfast is as follows:

- For the language, we will have a single `__cpp_constexpr` macro. It will be
bumped every time we extend constexpr in the language. 
- For the library, we will add a specific feature test macros for significant,
special features. Otherwise, for those cases where we are just adding `constexpr`
to more things in the library, we will have a dedicated test macro _per header_
and just bump that header-specific macro on each change. That macro will be
named `__cpp_lib_constexpr_HEADER` (with the exception of a few preexisting
macros for `array` and `algorithm` which have slightly different names).

This policy leads to several changes from R0 of this paper. 

# 2017

## Toronto (201707)

[@P0683R1] (Default member initializers for bit-fields): no macro necessary.

[@P0704R1] (Fixing const-qualified pointers to members): no macro necessary.

[@P0409R2] (Allow lambda capture `[=, this]`): no macro necessary.

[@P0306R4] (Comma omission and comma deletion): no macro necessary.

[@P0329R4] (Designated Initialization Wording): Marc Mutz suggests a use case where you might only provide a constructor if designated initialization is available (using designated initializers as a proxy for named parameters). The following is slightly reduced from his example:

```cpp
class QSlider {
public:
#if __cpp_designated_initializers
   struct Properties {
       struct { int min, max; } range = {};
       bool showTickMarks = false;
   };
   explicit QSlider(Properties props);
#endif
   // traditional, pre-existing approach:
   void setShowTickMarks(bool);
   bool showTickMarks() const noexcept;

   void setRange(int min, int max);
   int minimum() const noexcept;
   int maximum() const noexcept;
};
```

Where a C++14 user could then do:

```cpp
#ifdef __cpp_designated_initializers
   auto sl = new QSlider({ .range = {0, 100}, .showTickMarks = true}, this);
#else
   auto sl = new QSlider(this);
   sl->setRange(0, 100);
   sl->setShowTickMarks(true);
#endif
```

[This paper proposes the feature test macro `__cpp_designated_initializers`]{.addu}.

[@P0428R2] (Familiar template syntax for generic lambdas): [this paper proposes
to bump the macro `__cpp_generic_lambdas`]{.addu}. One of the things this feature
allows for is, for instance, defaulting a template parameter on a lambda,
which is arguably a feature enhancement:

```cpp
struct X { int i, j; };

auto f = 
#if __cpp_generic_lambdas >= 201707
    []<class T=X>(T&& var)
#else
    [](auto&& var)
#endif
    {
    };
    
// having the macro allows this usage
f({1, 2});
```

[@P0702R1] (Language support for Constructor Template Argument Deduction): no
macro necessary.

[@P0734R0] (Wording Paper, C++ extensions for Concepts): [this paper proposes
the macro `__cpp_concepts`]{.addu}, which will be bumped later, but for SD-6
purposes will start here with the value 201707.

[@P0463R1] (Endian just Endian) to the C++ working paper: Already have a macro
from [@P1612R1].

[@P0682R1] (Repairing elementary string conversions): Already have a macro
from [@LWG3137].

[@P0674R1] (Extending make_shared to Support Arrays): [this paper proposes to
bump `__cpp_lib_shared_ptr_arrays`]{.addu}, since `make_shared` can save an
allocation.

## Albuquerque (201711)

[@P0614R1] (Range-based for statements with initializer): no macro necessary.

[@P0588R1] (Simplifying implicit lambda capture): no macro necessary.

[@P0846R0] (ADL and Function Templates that are not Visible): no macro necessary.

[@P0641R2] (Resolving Core Issue #1331 (const mismatch with defaulted copy constructor)):
no macro necessary.

[@P0859R0] (Core Issue 1581: When are constexpr member functions defined?): [this
paper proposes the macro `__cpp_constexpr_in_decltype`]{.addu}. This issue
is a blocker for library being able to implement [@P1065R2], so the library needs
to know when to be able to do that. It's unclear if users outside of standard
library implementers will need this.

[@P0515R3] (Consistent comparison) and [@P0768R1] (Library Support for the Spaceship (Comparison) Operator): already have a macro.

[@P0857R0] (Wording for “functionality gaps in constraints”): no macro necessary.

[@P0692R1] (Access Checking on Specializations): no macro necessary.

[@P0624R2] (Default constructible and assignable stateless lambdas): no macro
necessary.

[@P0767R1] (Deprecate POD): no macro necessary.

[@P0315R4] (Wording for lambdas in unevaluated contexts): no macro necessary.

[@P0550R2] (Transformation Trait remove_cvref): [this paper proposes the macro
`__cpp_lib_remove_cvref`]{.addu}.

[@P0777R1] (Treating Unnecessary decay): no macro necessary.

[@P0600R1] (nodiscard in the Library): no macro necessary.

[@P0439R0] (Make `std::memory_order` a scoped enumeration): no macro necessary

[@P0053R7] (C++ Synchronized Buffered Ostream): [this paper proposes the macro
`__cpp_lib_syncbuf`]{.addu}.

[@P0653R2] (Utility to convert a pointer to a raw pointer): [this paper proposes
the macro `__cpp_lib_to_address`]{.addu}.

[@P0202R3] (Add `constexpr` modifiers to functions in `<algorithm>` and
`<utility>` Headers): a macro was already added.

[@P0415R1] (Constexpr for `std::complex`): [this paper proposes to introduce the
macro `__cpp_lib_constexpr_complex`]{.addu}. That is, introducing a new macro
for this header.

[@P0718R2] (Atomic `shared_ptr`): [this paper proposes the macro
`__cpp_lib_atomic_shared_ptr`]{.addu}.

[@P0020R6] (Floating Point Atomic): [this paper proposes the macro
`__cpp_lib_atomic_float`]{.addu}.

[@P0616R0] (de-pessimize legacy `<numeric>` algorithms with `std::move`): no
macro necessary.

[@P0457R2] (String Prefix and Suffix Checking): [this paper proposes the macro
`__cpp_lib_starts_ends_with`]{.addu}.

# 2018

## Jacksonville (201803)

[@P0840R2] (Language support for empty objects: already has a macro.

[@P0962R1] (Relaxing the range-for loop customization point finding rules): no
macro necessary.

[@P0969R0] (Allow structured bindings to accessible members): no macro necessary.

[@P0961R1] (Relaxing the structured bindings customization point finding rules):
no macro necessary.

[@P0634R3] (Down with `typename`!): no macro necessary.

[@P0780R2] (Allow pack expansion in lambda init-capture): [this paper proposes
to bump the macro `__cpp_init_captures`]{.addu}. Having such a macro would
allow you to avoid using `tuple` where necessary. The motivating example
in that paper could thus conditionally improve compile throughput:

```cpp
template <class... Args>
auto delay_invoke_foo(Args... args) {
#if __cpp_init_captures >= 201803
    return [...args=std::move(args)]() -> decltype(auto) {
        return foo(args...);
    };
#else
    return [tup=std::make_tuple(std::move(args)...)]() -> decltype(auto) {
        return std::apply([](auto const&... args) -> decltype(auto) {
            return foo(args...);
        }, tup);
    };
#endif
}
```

[@P0479R5] (Proposed wording for likely and unlikely attributes (Revision 5)):
already have a macro.

[@P0905R1] (Symmetry for spaceship): in a vacuum, maybe, but since there isn't
an implementation of `<=>` that includes just up to this point, it's probably not
worth it.

[@P0754R2] (`<version>`): already checkable with `__has_include`.

[@P0809R0] (Comparing Unordered Containers): no macro necessary.

[@P0355R7] (Extending chrono to Calendars and Time Zones): [this paper proposes
to bump the macro `__cpp_lib_chrono`]{.addu}.

[@P0966R1] (`string::reserve` Should Not Shrink): no macro necessary.

[@P0551R3] (Thou Shalt Not Specialize `std` Function Templates!): no macro
necessary.

[@P0753R2] (Manipulators for C++ Synchronized Buffered Ostream): [this paper
proposes to bump the macro `__cpp_lib_syncbuf`]{.addu}, which is also added by
this paper.

[@P0122R7] (`<span>`): already has a macro by way of [@LWG3274].

[@P0858R0] (Constexpr iterator requirements): already has a macro.

## Rapperswil (201806)

[@P0806R2] (Deprecate implicit capture of `this` via `[=]`): no macro necessary.

[@P1042R1] (`__VA_OPT__` wording clarifications): no macro necessary.

[@P0929R2] (Checking for abstract class types): no macro necessary.

[@P0732R2] (Class Types in Non-Type Template Parameters): already has a macro.

[@P1025R1] (Update The Reference To The Unicode Standard): no macro necessary.

[@P0528R3] (The Curious Case of Padding Bits, Featuring Atomic Compare-and-Exchange):
no macro necessary.

[@P0722R3] (Efficient sized delete for variable sized classes): already has a macro.

[@P1064R0] (Allowing Virtual Function Calls in Constant Expressions): [this paper
proposes to bump `__cpp_constexpr`]{.addu}. There are functions that include
`virtual` calls that would be able to be made `constexpr`. This macro already
has a higher value in the standard, so no wording changes necessary - just to
track in SD-6.

[@P1008R1] (Prohibit aggregates with user-declared constructors): no macro necessary.

[@P1120R0] (Consistency improvements for <=> and other comparison operators):
no macro necessary.

[@P0542R5] (Support for contract based programming in C++): would have been
checked by the attribute.

[@P0941R2] (Integrating feature-test macros into the C++ WD (rev. 2)): very meta.

[@P0892R2] (`explicit(bool)`): already has a macro.

[@P0476R2] (Bit-casting object representations): already has a macro.

[@P0788R3] (Standard Library Specification in a Concepts and Contracts World): no
macro necessary.

[@P0458R2] (Checking for Existence of an Element in Associative Containers): no
macro necessary. The new algorithms are nicer to use, but if you need to support
the old code, then the old code works just as well.

[@P0759R1] (fpos Requirements): no macro necessary.

[@P1023R0] (constexpr comparison operators for `std::array`): [this paper proposes
to bump the macro `__cpp_lib_array_constexpr`]{.addu}.

[@P0769R2] (Add shift to `<algorithm>`): [this paper proposes the macro
`__cpp_lib_shift`]{.addu}.

[@P0887R1] (The identity metafunction): [this paper proposes the macro
`__cpp_lib_type_identity`]{.addu}.

[@P0879R0] (Constexpr for swap and swap related functions): already has a macro.

[@P0758R1] (Implicit conversion traits and utility functions). [this paper proposes
the macro `__cpp_lib_nothrow_convertible`]{.addu}.

[@P0556R3] (Integral power-of-2 operations): [this paper proposes the macro
`__cpp_lib_int_pow2`]{.addu}. [There are NB comments about renaming the 
features introduced by this paper, which may necessitate renaming this macro]{.ednote}

[@P0019R8] (Atomic Ref): [this paper proposes the macro `__cpp_lib_atomic_ref`]{.addu}.

[@P0935R0] (Eradicating unnecessarily explicit default constructors from the
standard library): no macro necessary.

[@P0646R1] (Improving the Return Value of Erase-Like Algorithms): already has
a macro.

[@P0619R4] (Reviewing Deprecated Facilities of C++17 for C++20): no macro
necessary.

[@P0898R3] (Standard Library Concepts): already has a macro.

## San Diego (201811)

[@P0982R1] (Weaken Release Sequences): no macro necessary.

[@P1084R2] (Today's _return-type-requirement_s Are Insufficient): [this paper
proposes to bump `__cpp_concepts`]{.addu}, which was also added by this paper.

[@P1131R2] (Core Issue 2292: _simple-template-id_ is ambiguous between
_class-name_ and _type-name_): no macro necessary.

[@P1289R1] (Access control in contract conditions): no macro necessary

[@P1002R1] (Try-catch blocks in constexpr functions): [this paper proposes to
bump `__cpp_constexpr`]{.addu}, as per previous arguments to allow more
functions to be declared `constexpr`. This one more important than the rest as
actually writing `try` in a function already makes `constexpr` ill-formed.

[@P1327R1] (Allowing `dynamic_cast`, polymorphic typeid in Constant Expressions):
[this paper proposes to bump `__cpp_constexpr`]{.addu}.

[@P1236R1] (Alternative Wording for P0907R4 Signed Integers are Two's Complement):
no macro necessary.

[@P0482R6] (`char8_t`: A type for UTF-8 characters and strings (Revision 6)):
already has a macro.

[@P1353R0] (Missing Feature Test Macros): already adopted.

[@P1073R3] (Immediate functions): [this paper proposes the macro
`__cpp_consteval`]{.addu}. There are some functions that you really only want to
run at compile time. You cannot enforce this in C++17, but having this macro
would allow you to conditionally enforce it as it becomes available.

[@P0595R2] (`std::is_constant_evaluated()`): already has a macro.

[@P1141R2] (Yet another approach for constrained declarations): no macro necessary.

[@P1094R2] (Nested Inline Namespaces): no macro necessary.

[@P1330R0] (Changing the active member of a union inside constexpr): [this paper
proposes to bump `__cpp_constexpr`]{.addu}, as per previous arguments. This would
allow making `std::optional` fully `constexpr`, for instance.

[@P1123R0] (Editorial Guidance for merging P0019r8 and P0528r3): no macro
necessary.

[@P0487R1] (Fixing `operator>>(basic_istream&, CharT*)` (LWG 2499)): no macro
necessary.

[@P0602R4] (variant and optional should propagate copy/move triviality): no
macro necessary.

[@P0655R1] (`visit<R>`: Explicit Return Type for visit): no macro necessary.

[@P0972R0] (`<chrono>` `zero()`, `min()`, and `max()` should be `noexcept`): no
macro necessary.

[@P1006R1] (Constexpr in `std::pointer_traits`): [this paper proposes to bump 
the macro `__cpp_lib_constexpr_memory`]{.addu}.

[@P1032R1] (Misc constexpr bits): This paper originally added a single feature
test macro, `__cpp_lib_constexpr_misc`, that was since renamed by [@P1424R1] to
`__cpp_lib_constexpr`. Per the policy laid out in this paper, [this paper proposes
to remove `__cpp_lib_constexpr` and instead add separate macros for each header:
`__cpp_lib_constexpr_functional`,
`__cpp_lib_constexpr_iterator`, `__cpp_lib_constexpr_string_view`, 
`__cpp_lib_constexpr_tuple`, and
`__cpp_lib_constexpr_utility` and to bump `__cpp_lib_array_constexpr`]{.addu}.

[@P1148R0] (Cleaning up Clause 20): no macro necessary.

[@P0318R1] (`unwrap_ref_decay` and `unwrap_reference`): [this paper proposes the
macro `__cpp_lib_unwrap_ref`]{.addu}.

[@P0357R3] (`reference_wrapper` for incomplete types): no macro necessary.

[@P0608R3] (A sane variant converting constructor): no macro necessary.

[@P0771R1] (`std::function` move constructor should be `noexcept`): no macro
necessary.

[@P1007R3] (`std::assume_aligned`): [this paper proposes the macro 
`__cpp_lib_assume_aligned`]{.addu}.

[@P1020R1] (Smart pointer creation with default initialization): [this paper
proposes the macro `__cpp_lib_smart_ptr_default_init`]{.addu}.

[@P1285R0] (Improving Completeness Requirements for Type Traits): no macro
necessary.

[@P1248R1] (Remove CommonReference requirement from StrictWeakOrdering (a.k.a Fixing 
Relations): no macro necessary.

[@P0591R4] (Utility functions to implement uses-allocator construction): no
macro necessary.

[@P0899R1] (LWG 3016 is Not a Defect): no macro necessary.

[@P1085R2] (Should Span be Regular?): no macro necessary.

[@P1165R1] (Make stateful allocator propagation more consistent for
`operator+(basic_string)`): no macro necessary.

[@P0896R4] (The One Ranges Proposal): already has a macro.

[@P0356R5] (Simplified partial function application): already has a macro.

[@P0919R3] (Heterogeneous lookup for unordered containers): already has a macro.

[@P1209R0] (Adopt Consistent Container Erasure from Library Fundamentals 2 for C++20):
already has a macro.

# 2019

## Kona (201902)

[@P1286R2] (Contra CWG DR1778): no macro necessary.

[@P1091R3] (Extending structured bindings to be more like variable declarations):
no macro necessary.

[@P1381R1] (Reference capture of structured bindings): no macro necessary.

[@P1041R4] (Make `char16_t`/`char32_t` string literals be UTF-16/32): no macro
necessary.

[@P1139R2] (Address wording issues related to ISO 10646): no macro necessary.

[@P1323R2] (Contract postconditions and return type deduction): contracts were
removed.

[@P0960R3] (Allow initializing aggregates from a parenthesized list of values):
already has a macro.

[@P1009R2] (Array size deduction in new-expressions): no macro necessary.

[@P1103R3] (Merging Modules): already has a macro

[@P1185R2] (`<=> != ==`): [this paper proposes to bump
`__cpp_impl_three_way_comparison`]{.addu}.

[@P0339R6] (`polymorphic_allocator<>` as a vocabulary type): [this paper proposes
the macro `__cpp_lib_polymorphic_allocator`]{.addu}.

[@P0340R3] (Making `std::underlying_type` SFINAE-friendly): no macro necessary.

[@P0738R2] (I Stream, You Stream, We All Stream for `istream_iterator`): no macro
necssary.

[@P1458R1] (Mandating the Standard Library: Clause 16 - Language support library):
no macro necessary.

[@P1459R1] (Mandating the Standard Library: Clause 18 - Diagnostics library): no
macro necessary.

[@P1462R1] (Mandating the Standard Library: Clause 20 - Strings library): no macro
necessary.

[@P1463R1] (Mandating the Standard Library: Clause 21 - Containers library): no
macro necessary.

[@P1464R1] (Mandating the Standard Library: Clause 22 - Iterators library): no
macro necessary.

[@P1164R1] (Make `create_directory()` Intuitive): no macro necessary.

[@P0811R3] (Well-behaved interpolation for numbers and pointers): already has
a macro.

[@P1001R2] (Target Vectorization Policies from Parallelism V2 TS to C++20): no
macro necessary.

[@P1227R2] (Signed `ssize()` functions, unsigned `size()` functions ): [this
paper proposes the macro `__cpp_lib_ssize`]{.addu}.

[@P1252R2] (Ranges Design Cleanup): no macro necessary.

[@P1024R3] (Usability Enhancements for `std::span`): already has a macro.

[@P0920R2] (Precalculated hash values in lookup): already had a macro, which was
subsequently removed.

[@P1357R1] (Traits for [Un]bounded Arrays): no macro necessary

## Cologne (201907)

[@P1161R3] (Deprecate uses of the comma operator in subscripting expressions):
no macro necessary.

[@P1331R2] (Permitting trivial default initialization in constexpr contexts):
already has a macro.

[@P0735R1] (Interaction of `memory_order_consume` with release sequences):
already has a macro.

[@P0848R3] (Conditionally Trivial Special Member Functions): no macro necessary.
Would people really write both?

[@P1186R3] (When do you actually use `<=>`?): this paper proposed to bump
`__cpp_impl_three_way_comparison`, but shouldn't have. This paper doesn't need
a macro.

[@P1301R4] (`[[nodiscard("should have a reason")]]`): already has a macro.

[@P1099R5] (Using Enum): already has a macro

[@P1630R1] (Spaceship needs a tune-up): [this paper proposes that the bump
of `__cpp_impl_three_way_comparison` is associated with this paper instead of
P1186R3]{.addu}.

[@P1616R1] (Using unconstrained template template parameters with constrained templates):
no macro necessary.

[@P1816R0] (Wording for class template argument deduction for aggregates): no
macro necessary. Would you choose to not provide a deduction guide for an
aggregate?

[@P1668R1] (Enabling `constexpr` Intrinsics By Permitting Unevaluated
inline-assembly in `constexpr` Functions): [this paper proposes to bump
`__cpp_constexpr`]{.addu}.

[@P1766R1] (Mitigating minor modules maladies): already has a macro.

[@P1811R0] (Relaxing redefinition restrictions for re-exportation robustness):
already has a macro.

[@P0388R4] (Permit conversions to arrays of unknown bound): no macro necessary.

[@P1823R0]: no macro necessary.

[@P1143R2] (Adding the constinit keyword): already has a macro.

[@P1452R2] (On the non-uniform semantics of return-type-requirements): [this paper proposes to bump the value of `__cpp_concepts`]{.addu}.

[@P1152R4] (Deprecating `volatile`): no macro necessary.

[@P1771R1] (`[[nodiscard]]` for constructors): already has a macro.

[@P1814R0] (Wording for Class Template Argument Deduction for Alias Templates):
already has a macro.

[@P1825R0] (Merged wording for P0527R1 and P1155R3): no macro needed, just write
`std::move()`.

[@P1703R1] (Recognizing Header Unit Imports Requires Full Preprocessing): no
macro needed.

[@P0784R7] (More constexpr containers): already has a macro. This is a significant
library feature that merits its own macro (`__cpp_lib_constexpr_dynamic_alloc`).

[@P1355R2] (Exposing a narrow contract for ceil2): no macro needed.

[@P0553R4] (Bit operations): already has a macro.

[@P1424R1] (`constexpr` feature macro concerns): already resolved.

[@P0645R10] (Text Formatting): already has a macro.

[@P1361R2] (Integration of chrono with text formatting): already has a macro.

[@P1652R1] (Printf corner cases in `std::format`): already has a macro.

[@P0631R8] (Math Constants): already has a macro.

[@P1135R6] (The C++20 Synchronization Library), [@P1643R1] (Add
wait/notify to `atomic_ref`), and [@P1644R0] (Add
wait/notify to `atomic<shared_ptr>`): already have macros.

[@P1466R3] (Miscellaneous minor fixes for chrono): already has a macro.

[@P1754R1] (Rename concepts to standard_case for C++20, while we still can):
[this paper proposes to bump `__cpp_lib_concepts`]{.addu}, even though nobody
implements this yet, because otherwise it's confusing.

[@P1614R2] (The Mothership has Landed): [erroneously introduced the
new macro `__cpp_lib_spaceship`, this paper proposes removing that macro and
instead bumping `__cpp_lib_three_way_comparison`]{.addu}.

[@P0325R4] (`to_array` from LFTS with updates): already has a macro.

[@P0408R7] (Efficient Access to `basic_stringbuf`’s Buffer): no macro necessary.
Trying to move out of the buffer will compile even without this feature, it just
won't be a move.

[@P1423R3] (`char8_t` backward compatibility remediation): already has a macro.

[@P1502R1] (Standard library header units for C++20): no macro necessary.

[@P1612R1] (Relocate Endian’s Specification): already has a macro.

[@P1661R1] (Remove dedicated precalculated hash lookup interface): already
removes a macro.

[@P1650R0] (Output `std::chrono::days` with 'd' suffix): no macro necessary.

[@P1651R0] (`bind_front` should not unwrap `reference_wrapper`): no macro
necessary.

[@P1065R2] (Constexpr INVOKE): as above, [this paper proposes to rename `__cpp_lib_constexpr_invoke`
to `__cpp_lib_constexpr_functional`]{.addu}.

[@P1207R4] (Movability of Single-pass Iterators): no macro necessary.

[@P1035R7] (Input Range Adaptors): [this paper proposes to bump the macro
`__cpp_lib_ranges`]{.addu}.

[@P1638R1] (`basic_istream_view::iterator` should not be copyable): no macro
necessary.

[@P1522R1] (Iterator Difference Type and Integer Overflow): no macro necessary.

[@P1004R2] (Making `std::vector` constexpr): already has a macro.

[@P0980R1] (Making `std::string` constexpr): already has a mcro.

[@P0660R10] (Stop Token and Joining Thread, Rev 10): already has a macro.

[@P1474R1] (Helpful pointers for `ContiguousIterator`): no macro necessary.

[@P1523R1] (Views and Size Types): no macro necessary.

[@P0466R5] (Layout-compatibility and Pointer-interconvertibility Traits):
already has a macro.

[@P1208R6] (Adopt `source_location` for C++20): already has a macro.

# Wording

Modify table 17 in 15.10 [cpp.predefined] with the following added:

<table>
<tr>
<th>Macro Name</th>
<th>Value</th>
</tr>
<tr><td>`__cpp_generic_lambdas`</td><td>[`201304L`]{.rm} [`201707L`]{.addu}</td></tr>
<tr><td>`__cpp_init_captures`</td><td>[`201304L`]{.rm} [`201803L`]{.addu}</td></tr>
<tr><td>[`__cpp_designated_initializers`]{.addu}</td><td>[`201707L`]{.addu}</td></tr>
<tr><td>[`__cpp_concepts`]{.addu}</td><td>[`201907L`]{.addu}</td></tr>
<tr><td>[`__cpp_constexpr_in_decltype`]{.addu}</td><td>[`201711L`]{.addu}</td></tr>
<tr><td>[`__cpp_consteval`]{.addu}</td><td>[`201811L`]{.addu}</td></tr>
</table>

Modify table 36 in 17.3.1 [support.limits.general] with the following added:


<table>
<tr>
<th>Macro Name</th>
<th>Value</th>
<th>Header(s)</th>
</tr>
<tr><td>[`__cpp_lib_shared_ptr_arrays`]{.addu}</td><td>[`201611L`]{.rm} [`201707L`]{.addu}</td><td>[`<memory>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_remove_cvref`]{.addu}</td><td>[`201711L`]{.addu}</td><td>[`<type_traits>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_syncbuf`]{.addu}</td><td>[`201803L`]{.addu}</td><td>[`<syncstream>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_to_address`]{.addu}</td><td>[`201711L`]{.addu}</td><td>[`<memory>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_atomic_shared_ptr`]{.addu}</td><td>[`201711L`]{.addu}</td><td>[`<memory>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_atomic_float`]{.addu}</td><td>[`201711L`]{.addu}</td><td>[`<atomic>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_starts_ends_with`]{.addu}</td><td>[`201711L`]{.addu}</td><td>[`<string> <string_view>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_shift `]{.addu}</td><td>[`201806L`]{.addu}</td><td>[`<algorithm>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_type_identity `]{.addu}</td><td>[`201806L`]{.addu}</td><td>[`<type_traits>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_nothrow_convertible `]{.addu}</td><td>[`201806L`]{.addu}</td><td>[`<type_traits>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_int_pow2 `]{.addu}</td><td>[`201806L`]{.addu}</td><td>[`<bit>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_atomic_ref `]{.addu}</td><td>[`201806L`]{.addu}</td><td>[`<atomic>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_unwrap_ref `]{.addu}</td><td>[`201811L`]{.addu}</td><td>[`<type_traits>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_assume_aligned `]{.addu}</td><td>[`201811L`]{.addu}</td><td>[`<memory>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_smart_ptr_default_init `]{.addu}</td><td>[`201811L`]{.addu}</td><td>[`<memory>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_polymorphic_allocator `]{.addu}</td><td>[`201902L`]{.addu}</td><td>[`<memory>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_ssize `]{.addu}</td><td>[`201902L`]{.addu}</td><td>[`<iterator>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_concepts `]{.addu}</td><td>[`201806L`]{.rm} [`201907L`]{.addu}</td><td>[`<concepts>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_spaceship `]{.rm}</td><td>[`201907L`]{.rm}</td><td>[`<compare>`]{.rm}</td></tr>
<tr><td>[`__cpp_lib_constexpr`]{.rm}</td><td>[`201811L`]{.rm}</td><td>[any C++ library header ...]{.rm}</td></tr>
<tr><td>`__cpp_lib_array_constexpr`</td><td>[`201803L`]{.rm} [`201811L`]{.addu}</td><td>`<array>`</td></tr>
<tr><td>[`__cpp_lib_constexpr_invoke`]{.rm} [`__cpp_lib_constexpr_functional`]{.addu}</td><td>`201907L`</td><td>[`<functional>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_constexpr_iterator`]{.addu}</td><td>[`201811L`]{.addu}</td><td>[`<iterator>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_constexpr_memory`]{.addu}</td><td>[`201811L`]{.addu}</td><td>[`<memory>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_constexpr_string_view`]{.addu}</td><td>[`201811L`]{.addu}</td><td>[`<string_view>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_constexpr_tuple`]{.addu}</td><td>[`201811L`]{.addu}</td><td>[`<tuple>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_constexpr_utility`]{.addu}</td><td>[`201811L`]{.addu}</td><td>[`<utility>`]{.addu}</td></tr>
<tr><td>`__cpp_lib_chrono`</td><td>[`201611L`]{.rm} [`201803L`]{.addu}</td><td>`<chrono>`</td></tr>
<tr><td>`__cpp_lib_three_way_comparison`</td><td>[`201711L`]{.rm} [`201907L`]{.addu}</td><td>`<compare>`</td></tr>
<tr><td>`__cpp_lib_ranges`</td><td>[`201811L`]{.rm} [`201907L`]{.addu}</td><td>`<algorithm> <functional>`
</table>
