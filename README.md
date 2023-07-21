# cffi-example

Based on [CFFI-Overview](https://cffi.readthedocs.io/en/latest/overview.html)

## Build

```shell
$ export PIP_EXTRA_INDEX_URL=https://github.com/makslevental/wheels/releases/expanded_assets/i
$ git clean -fdx -e .idea
$ cmake . -B build -DCMAKE_INSTALL_PREFIX=$PWD && cmake --build build --target install
$ pip install -e . -v --no-build-isolation
```

## Run

First, in case you haven't, you have to symlink `libMLIRPythonCAPI.so`:
```shell
$ ln -s \
  "$(python -c "print(__import__('mlir._mlir_libs', fromlist=['*']).__path__[0])")"/libMLIRPythonCAPI.so \
  "$(python -c "print(__import__('mlir._mlir_libs', fromlist=['*']).__path__[0])")"/libMLIRPythonCAPI.so.17
```

Then run [`demo.py`]:

```shell
$ python demo.py
3.172800064086914
<cdata 'struct MlirContext' owning 8 bytes>
```