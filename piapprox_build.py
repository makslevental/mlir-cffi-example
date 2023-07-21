import glob
import sys
from pathlib import Path
from cffi import FFI
import mlir._mlir_libs.include


ffibuilder = FFI()

# cdef() expects a single string declaring the C types, functions and
# globals needed to use the shared object. It must be in valid C syntax.
ffibuilder.cdef(
    """
    float pi_approx(int n);
    struct MlirContext {
      void *ptr;
    };
    typedef struct MlirContext MlirContext;
    MlirContext mlirContextCreate(void);
"""
)

HERE = Path(__file__).parent.absolute()
MLIR_LIB_PATH = Path(mlir._mlir_libs.__path__[0])
MLIR_INCLUDE_PATH = MLIR_LIB_PATH / "include"

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source(
    "_pi_cffi",
    """
    #include "pi.h"   // the C header of the library
    #include "mlir-c/IR.h"
    """,
    libraries=["piapprox", "MLIRPythonCAPI"],
    extra_link_args=[
        f"-L{HERE}/lib",
        f"-Wl,-rpath={HERE}/lib",
        f"-L{MLIR_LIB_PATH}",
        f"-Wl,-rpath={MLIR_LIB_PATH}",
    ],
    include_dirs=[str(HERE), str(MLIR_INCLUDE_PATH)],
)  # library name, for the linker

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
