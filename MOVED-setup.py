from distutils.core import setup, Extension
import numpy.distutils.misc_util

# Find numpy include dir
numpy_include_dir = numpy.distutils.misc_util.get_numpy_include_dirs()
idirs             = numpy_include_dir

# Location for FreeTDS library and headers
freetds        = "/cosma/local/freetds/1.4.20"
freetds_incdir = freetds + "/include/"
freetds_libdir = freetds + "/lib/"

# Module for SQL Server bulk imports 
pybcp_module = Extension('_pybcp', sources = ['_pybcp.c'],
                         libraries=["sybdb"],
                         library_dirs=[freetds_libdir],
                         runtime_library_dirs=[freetds_libdir],
                         include_dirs=[freetds_incdir])

setup (name         = 'PyBCP',
       version      = '0.1',
       description  = 'Provides facilities to bulk import numpy arrays to SQL Server',
       ext_modules  = [pybcp_module],
       py_modules   = ["pybcp"],
       include_dirs =idirs)

