@echo off

where cmake > nul
if %errorlevel% neq 0 (
    echo cmake could not be found, installing cmake...
    pip install cmake
)


md ..\cmake
cd ..\cmake

echo cmake_minimum_required(VERSION 3.10)>CMakeLists.txt
echo set(lib_name Vectors)>>CMakeLists.txt
echo project(^%lib_name^%)>>CMakeLists.txt
echo. >>CMakeLists.txt
echo. >>CMakeLists.txt
echo # Add all the source files >>CMakeLists.txt
echo set(SOURCES >>CMakeLists.txt
echo     ..\vectors.cpp >>CMakeLists.txt
echo ) >>CMakeLists.txt
echo. >>CMakeLists.txt
echo # Compile the library >>CMakeLists.txt
echo add_library(^%lib_name^% SHARED ^%SOURCES^% ) >>CMakeLists.txt
echo. >>CMakeLists.txt
echo # Set the include directories >>CMakeLists.txt
echo target_include_directories(^%lib_name^% PRIVATE ^%CMAKE_CURRENT_SOURCE_DIR^%) >>CMakeLists.txt
echo. >>CMakeLists.txt
echo # Set the output directory for the library >>CMakeLists.txt
echo set_target_properties(^%lib_name^% PROPERTIES >>CMakeLists.txt
echo     LIBRARY_OUTPUT_DIRECTORY ^%CMAKE_BINARY_DIR^%/lib >>CMakeLists.txt
echo ) >>CMakeLists.txt
echo. >>CMakeLists.txt
echo # Ensure that the library is built for Windows >>CMakeLists.txt
echo if (WIN32) then ( >>CMakeLists.txt
echo     set_target_properties(^%lib_name^% PROPERTIES >>CMakeLists.txt
echo         SUFFIX ".dll" >>CMakeLists.txt
echo     ) >>CMakeLists.txt
echo ) >>CMakeLists.txt

cmake .
cmake --build . --config Release


