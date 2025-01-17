project('purelib-and-platlib', 'c')

# Specify location of freetds library
freetds_path   = '/cosma/local/freetds/1.4.20'
freetds_libdir = freetds_path / 'lib'
freetds_incdir = freetds_path / 'include'

py = import('python').find_installation(pure: false)

# Set library and header search paths for freetds
cc = meson.get_compiler('c')
lib_sybdb = cc.find_library('sybdb', dirs : freetds_libdir)
inc_sybdb = include_directories(freetds_incdir)

# Set location of numpy headers: required to avoid using wrong version in /usr/include on some systems
_numpy_abs = run_command(py, ['-c', 'import os; os.chdir(".."); import numpy; print(os.path.abspath(numpy.get_include() + "../../.."))'], check: true).stdout().strip()
npy_include_path = _numpy_abs / '_core' / 'include'
         
py.install_sources('pybcp.py')

# Compile the C extension module, which requires libsybdb from the freetds installation
py.extension_module(
    '_pybcp',
    '_pybcp.c',
    install: true,
    dependencies : [lib_sybdb],
    include_directories : [inc_sybdb, npy_include_path]
)
