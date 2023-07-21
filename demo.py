from _pi_cffi import ffi, lib

print(lib.pi_approx(5000))

p = lib.mlirContextCreate()
print(p)