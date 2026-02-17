cmake_minimum_required(VERSION 3.21)
project(${SKBUILD_PROJECT_NAME} LANGUAGES C)

find_package(
  Python
  COMPONENTS Interpreter Development.Module
  REQUIRED)

add_custom_command(
  OUTPUT creedsolo.c
  COMMAND
    Python::Interpreter -m cython
    "${CMAKE_CURRENT_SOURCE_DIR}/src/creedsolo/creedsolo.pyx" --output-file
    creedsolo.c
  DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/src/creedsolo/creedsolo.pyx"
  VERBATIM)

python_add_library(creedsolo MODULE creedsolo.c WITH_SOABI)

install(TARGETS creedsolo DESTINATION .)
