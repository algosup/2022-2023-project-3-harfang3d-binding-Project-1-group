cmake_minimum_required(VERSION 3.10)
set(lib_name Test56)
project(${lib_name})



# Add all the source files
set(SOURCES
    ../vectors.cpp
)


# Compile the library
add_library(${lib_name} SHARED ${SOURCES} )

# Set the include directories
target_include_directories(${lib_name} PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})

# Set the output directory for the library
set_target_properties(${lib_name} PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib
)

# Ensure that the library is built for macOS
if (APPLE)
    set_target_properties(${lib_name} PROPERTIES
        MACOSX_RPATH ON
    )
endif()
