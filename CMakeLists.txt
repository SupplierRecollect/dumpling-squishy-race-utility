cmake_minimum_required(VERSION 3.10)
project(dumpling-squishy-race-utility)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(dumpling_utility
    src/main.cpp
    src/race_utils.cpp
    src/dumpling_handler.cpp
)

target_include_directories(dumpling_utility PRIVATE src)
target_link_libraries(dumpling_utility PRIVATE fmt)