cmake_minimum_required(VERSION 3.10.0)
project(CreateTask VERSION 0.1.0 LANGUAGES C CXX)

# Find the SDL2 library
find_package(SDL2 REQUIRED)
if(NOT SDL2_FOUND)
    message(FATAL_ERROR "SDL2 not found. Please check your SDL2 installation.")
endif()

include_directories(build/include)
add_compile_options(-g)

file(GLOB_RECURSE SOURCE "*.cpp")

add_executable(CreateTask ${SOURCE})

# Link against the SDL2 libraries
#target_link_directories(CreateTask PUBLIC build/lib)
target_link_libraries(CreateTask ${SDL2_LIBRARIES})