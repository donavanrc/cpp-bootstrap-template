cmake_minimum_required(VERSION 3.27)

project(cpp-bootstrap-template C CXX)

if(WIN32)
    set(PYTHON_EXECUTABLE "python")
else()
    set(PYTHON_EXECUTABLE "python3")
endif()

execute_process(COMMAND ${PYTHON_EXECUTABLE} "setup.py"
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    RESULT_VARIABLE result)

if(NOT(${result} EQUAL 0))
    message(FATAL_ERROR "Failed to run setup.py")
endif()

include_directories(External/Dependencies/spdlog/include)

add_subdirectory(Examples/HelloWorld)