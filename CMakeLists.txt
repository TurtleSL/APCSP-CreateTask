cmake_minimum_required(VERSION 3.10.0)
project(CreateTask VERSION 0.1.0 LANGUAGES C CXX)

file(GLOB_RECURSE SOURCE "*.cpp")

add_executable(CreateTask ${SOURCE})

target_link_libraries(CreateTask libSDL2)