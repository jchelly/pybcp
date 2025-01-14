project('purelib-and-platlib', 'c')

py = import('python').find_installation(pure: false)

cc = meson.get_compiler('c')
lib_sybdb = cc.find_library('sybdb', dirs : ['/cosma/local/freetds/1.4.20/lib'])
inc_sybdb = include_directories('/cosma/local/freetds/1.4.20/include')

py.extension_module(
    '_pybcp',
    '_pybcp.c',
    install: true,
    dependencies : [lib_sybdb],
    include_directories : inc_sybdb
)
