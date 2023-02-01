@echo off

where cmake > nul
if %errorlevel% neq 0 (
echo cmake could not be found, installing cmake...
pip install cmake
)

md ..\cmake
cd ..\cmake

echo cmake_minimum_required(VERSION 3.10)>CMakeLists.txt
echo project(Vectors)>>CMakeLists.txt
echo. >>CMakeLists.txt
echo. >>CMakeLists.txt
echo # Add all the source files >>CMakeLists.txt
echo set(SOURCES ../vectors.cpp) >>CMakeLists.txt
echo. >>CMakeLists.txt
echo # Compile the library >>CMakeLists.txt
echo add_library(Vectors SHARED ${SOURCES}) >>CMakeLists.txt
echo. >>CMakeLists.txt
echo # Set the include directories >>CMakeLists.txt
echo target_include_directories(Vectors PRIVATE ../include) >>CMakeLists.txt
echo. >>CMakeLists.txt
echo # Set the output directory for the library >>CMakeLists.txt
echo set_target_properties(Vectors PROPERTIES >>CMakeLists.txt
echo LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib >>CMakeLists.txt
echo ) >>CMakeLists.txt
echo. >>CMakeLists.txt
echo # Ensure that the library is built for Windows >>CMakeLists.txt
echo if (WIN32) >>CMakeLists.txt
echo set_target_properties(Vectors PROPERTIES SUFFIX ".dll") >>CMakeLists.txt
echo endif() >>CMakeLists.txt

cmake .
cmake --build . --config Release