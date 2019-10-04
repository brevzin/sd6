---
title: Missing feature-test macros 2018-2019
document: D1902R0
date: today
audience: CWG, LWG
author:
    - name: Barry Revzin
      email: <barry.revzin@gmail.com>
toc: true
---

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

# 2017

## Toronto (201707)

[@P0683R1] (Default member initializers for bit-fields): no macro necessary.

[@P0704R1] (Fixing const-qualified pointers to members): no macro necessary.

[@P0409R2] (Allow lambda capture `[=, this]`): no macro necessary.

[@P0306R4] (Comma omission and comma deletion): no macro necessary.

[@P0329R4] (Designated Initialization Wording): no macro necessary. It's possible
that you could write something like:

```cpp
struct X { int first, int second; };

#if __cpp_designated_initializer
#define INIT_EQ(name) .name =
#else
#define INIT_EQ(name)
#endif

X{INIT_EQ(first) 7, INIT_EQ(second) 10};
```

That does give some benefit, in that if you get the names wrong, you'd get a
diagnostic. But would anybody actually do that?

[@P0428R2] (Familiar template syntax for generic lambdas): [this paper proposes
the macro `__cpp_familiar_template_lambda`]{.addu}. One of the things this feature
allows for is, for instance, defaulting a template parameter on a lambda,
which is arguably a feature enhancement:

```cpp
struct X { int i, j; };

auto f = 
#if __cpp_familiar_template_lambda
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
paper proposes the macro `__cpp_impl_constexpr_members_defined`]{.addu}. This issue
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

[@P0415R1] (Constexpr for `std::complex`): [this paper proposes the macro
`__cpp_lib_constexpr_complex`]{.addu}.

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
the macro `__cpp_lambda_init_capture_pack`]{.addu}. Having such a macro would
allow you to avoid using `tuple` where necessary. The motivating example
in that paper could thus conditionally improve compile throughput:

```cpp
template <class... Args>
auto delay_invoke_foo(Args... args) {
#if __cpp_lambda_init_capture_pack
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
the macro `__cpp_lib_chrono_date`]{.addu}.

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
the macro `__cpp_lib_constexpr_array_comparisons`]{.addu} for the same reason as
earlier: it allows more functions to be marked `constexpr`.

[@P0769R2] (Add shift to `<algorithm>`): [this paper proposes the macro
`__cpp_lib_shift`]{.addu}.

[@P0887R1] (The identity metafunction): [this paper proposes the macro
`__cpp_lib_type_identity`]{.addu}.

[@P0879R0] (Constexpr for swap and swap related functions): already has a macro.

[@P0758R1] (Implicit conversion traits and utility functions). [this paper proposes
the macro `__cpp_lib_nothrow_convertible`]{.addu}.

[@P0556R3] (Integral power-of-2 operations): [this paper proposes the macro
`__cpp_lib_int_pow2`]{.addu}.

[@P0019R8] (Atomic Ref): [this paper proposes the macro `__cpp_lib_atomic_ref`]{.addu}.

[@P0935R0] (Eradicating unnecessarily explicit default constructors from the
standard library): no macro necessary.

[@P0646R1] (Improving the Return Value of Erase-Like Algorithms): already has
a macro.

[@P0619R4] (Reviewing Deprecated Facilities of C++17 for C++20): no macro
necessary.

[@P0898R3] (Standard Library Concepts): already has a macro.

## San Diego (201811)

# 2019

## Kona (201902)

## Cologne (201907)

# Wording

Modify table 17 in 15.10 [cpp.predefined] with the following added:

::: bq
<table>
<tr>
<th>Macro Name</th>
<th>Value</th>
</tr>
<tr><td>[`__cpp_familiar_template_lambda`]{.addu}</td><td>[`201707L`]{.addu}</td></tr>
<tr><td>[`__cpp_concepts`]{.addu}</td><td>[`201707L`]{.addu}</td></tr>
<tr><td>[`__cpp_impl_constexpr_members_defined`]{.addu}</td><td>[`201711L`]{.addu}</td></tr>
<tr><td>[`__cpp_lambda_init_capture_pack`]{.addu}</td><td>[`201803L`]{.addu}</td></tr>
</table>
:::

Modify table 36 in 17.3.1 [support.limits.general] with the following added:

::: bq
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
<tr><td>[`__cpp_lib_constexpr_complex`]{.addu}</td><td>[`201711L`]{.addu}</td><td>[`<complex>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_atomic_shared_ptr`]{.addu}</td><td>[`201711L`]{.addu}</td><td>[`<atomic>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_atomic_float`]{.addu}</td><td>[`201711L`]{.addu}</td><td>[`<atomic>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_starts_ends_with`]{.addu}</td><td>[`201711L`]{.addu}</td><td>[`<string> <string_view>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_chrono_date`]{.addu}</td><td>[`201803L`]{.addu}</td><td>[`<chrono>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_constexpr_array_comparisons `]{.addu}</td><td>[`201806L`]{.addu}</td><td>[`<array>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_shift `]{.addu}</td><td>[`201806L`]{.addu}</td><td>[`<algorithm>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_type_identity `]{.addu}</td><td>[`201806L`]{.addu}</td><td>[`<type_traits>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_nothrow_convertible `]{.addu}</td><td>[`201806L`]{.addu}</td><td>[`<type_traits>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_int_pow2 `]{.addu}</td><td>[`201806L`]{.addu}</td><td>[`<bit>`]{.addu}</td></tr>
<tr><td>[`__cpp_lib_atomic_ref `]{.addu}</td><td>[`201806L`]{.addu}</td><td>[`<atomic>`]{.addu}</td></tr>
</table>
:::