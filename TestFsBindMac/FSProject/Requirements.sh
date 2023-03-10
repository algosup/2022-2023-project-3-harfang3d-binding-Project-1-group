if ! command -v cmake &> /dev/null
then
    echo "cmake could not be found, installing cmake..."
    pip install cmake
    mkdir ../cmake
    cd ../cmake
    echo "cmake_minimum_required(VERSION 3.10)
set(lib_name Vectors)
project(\${lib_name})

# Add all the header files
set(HEADERS
    ../Vectors/vectors.h
)

# Add all the source files
set(SOURCES
    ../Vectors/vectors.cpp
)

# Compile the library
add_library(\${lib_name} SHARED \${HEADERS} \${SOURCES})

# Set the include directories
target_include_directories(\${lib_name} PRIVATE \${CMAKE_CURRENT_SOURCE_DIR})

# Set the output directory for the library
set_target_properties(\${lib_name} PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY \${CMAKE_BINARY_DIR}/lib
)

# Ensure that the library is built for macOS
if (APPLE)
    set_target_properties(\${lib_name} PROPERTIES
        MACOSX_RPATH ON
    )
endif()" > CMakeLists.txt | grep ""
    cmake .
    cmake --build . --config Release
else
    mkdir ../cmake
    cd ../cmake
    echo "cmake_minimum_required(VERSION 3.10)
set(lib_name Vectors)
project(\${lib_name})

# Add all the header files
set(HEADERS
    ../Vectors/vectors.h
)

# Add all the source files
set(SOURCES
    ../Vectors/vectors.cpp
)

# Compile the library
add_library(\${lib_name} SHARED \${HEADERS} \${SOURCES})

# Set the include directories
target_include_directories(\${lib_name} PRIVATE \${CMAKE_CURRENT_SOURCE_DIR})

# Set the output directory for the library
set_target_properties(\${lib_name} PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY \${CMAKE_BINARY_DIR}/lib
)

# Ensure that the library is built for macOS
if (WIN32)
    set_target_properties(\${lib_name} PROPERTIES
        SUFFIX ".dll"
    )
elseif(APPLE)
    set_target_properties(\${lib_name} PROPERTIES
        SUFFIX ".dylib"
    )
endif()" > CMakeLists.txt | grep ""
    cmake .
    cmake --build . --config Release
    
fi


