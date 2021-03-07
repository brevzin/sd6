import add_macro

doc = add_macro.Document('../macros.yaml')
VALUE = 202102

# lwg motion 4: p2162r2
doc.update(kind='library', name='__cpp_lib_variant', value=VALUE, papers='P2162R2')

# lwg motion 7: p1682r2
doc.add(kind='library', name='__cpp_lib_to_underlying', value=VALUE, papers='P1682R2', headers='utility')

doc.dump()
