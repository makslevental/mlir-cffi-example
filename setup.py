from setuptools import setup

setup(
    name="cffi-example",
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=["piapprox_build.py:ffibuilder"],  # "filename:global"
    install_requires=["cffi>=1.0.0", "mlir-python-bindings"],
    py_modules=["demo", "piapprox_build"],
)
