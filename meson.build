project('purelib-and-platlib', 'c')

py = import('python').find_installation(pure: false)

cc = meson.get_compiler('c')
lib_sybdb = cc.find_library('sybdb')

py.extension_module(
    '_pybcp',
    '_pybcp.c',
    install: true,
    dependencies : [lib_sybdb],
)
