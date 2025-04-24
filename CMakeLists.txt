cmake_minimum_required(VERSION 3.10.0)
project(CreateTask VERSION 0.1.0 LANGUAGES C CXX)

include_directories(SDL/x86_64-w64-mingw32/include)
add_compile_options(-g)

file(GLOB_RECURSE SOURCE "*.cpp")

add_executable(CreateTask ${SOURCE})

# Link against the SDL2 libraries
target_link_directories(CreateTask PUBLIC SDL/x86_64-w64-mingw32/lib)
target_link_libraries(CreateTask libSDL3.dll)