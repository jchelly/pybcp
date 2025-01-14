# Python module for uploading numpy arrays to MS SQL Server

## Compilation

Set the location of the freetds libsybdb and then run pip:
```
SYBDB=/cosma/local/freetds/1.4.20/
LDFLAGS="-L${SYBDB}/lib/ -Wl,-rpath=${SYBDB}/lib/" CFLAGS="-I${SYBDB}/include/" pip install .
```
