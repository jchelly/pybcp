# Python module for uploading numpy arrays to MS SQL Server

## Compilation

Set the location of the freetds libsybdb by editing meson.build:
```
lib_sybdb = cc.find_library('sybdb', dirs : ['/cosma/local/freetds/1.4.20/lib'])
inc_sybdb = include_directories('/cosma/local/freetds/1.4.20/include')
```
Then the module can be compiled and installed with
```
pip install .
```
