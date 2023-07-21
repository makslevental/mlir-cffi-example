cmake_minimum_required(VERSION 3.22)
project(cffi_example)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_C_STANDARD 17)

add_library(piapprox SHARED pi.c)

install(TARGETS piapprox)