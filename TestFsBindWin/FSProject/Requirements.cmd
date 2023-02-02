@echo off

rem Check if cmake is installed, and install it if not
where cmake > nul
if %errorlevel% neq 0 (
echo cmake could not be found, installing cmake...
pip install cmake
)

rem Create the cmake directory and change to it
md ..\cmake
cd ..\cmake

rem Create the CMakeLists.txt file and add the necessary commands
echo cmake_minimum_required(VERSION 3.10)>CMakeLists.txt
echo set (lib_name Vectors) >>CMakeLists.txt
echo project(${lib_name})>>CMakeLists.txt
echo. >>CMakeLists.txt

echo set (SOURCES >>CMakeLists.txt
echo      ../vectors.cpp  >>CMakeLists.txt
echo ) >>CMakeLists.txt

rem Compile the library
echo # Compile the library >>CMake\Lists.txt
echo add_library(${lib_name} SHARED ${SOURCES}) >>CMakeLists.txt
echo. >>CMakeLists.txt

rem Set the include directories
echo # Set the include directories >>CMakeLists.txt
echo target_include_directories(${lib_name} PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}) >>CMakeLists.txt
echo. >>CMakeLists.txt

rem Set the output directory for the library
echo # Set the output directory for the library >>CMakeLists.txt
echo set_target_properties(${lib_name} PROPERTIES >>CMakeLists.txt
echo     LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib >>CMakeLists.txt
echo ) >>CMakeLists.txt
echo. >>CMakeLists.txt

rem Ensure the library is built for Windows
echo # Ensure that the library is built for Windows >>CMakeLists.txt
echo if (WIN32) >>CMakeLists.txt
echo     set_target_properties(${lib_name} PROPERTIES SUFFIX ".dll") >>CMakeLists.txt
echo endif() >>CMakeLists.txt

rem Build the project
cmake .
cmake --build . --config Release