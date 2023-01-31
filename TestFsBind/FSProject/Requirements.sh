if ! command -v cmake &> /dev/null
then
    echo "cmake could not be found, installing cmake..."
    pip install cmake
    mkdir ../cmake
    cd ../cmake
    echo "cmake_minimum_required(VERSION 3.10)
set(lib_name Test56)
project(\${lib_name})



# Add all the source files
set(SOURCES
    ../vectors.cpp
)


# Compile the library
add_library(\${lib_name} SHARED \${SOURCES} )

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
endif()" > CMakeLists.txt | grep -v "/Users/remycharles/Desktop/Github Desktop/2022-2023-project-3-harfang3d-binding-Project-1-group/TestFsBind/FSProject/vectors.fs(12,9): warning FS0046: The identifier 'process' is reserved for future use by F# [/Users/remycharles/Desktop/Github Desktop/2022-2023-project-3-harfang3d-binding-Project-1-group/TestFsBind/FSProject/FsharpBindings.fsproj]"
    cmake .
    cmake --build . --config Release
else
    mkdir ../cmake
    cd ../cmake
    echo "cmake_minimum_required(VERSION 3.10)
set(lib_name Test56)
project(\${lib_name})



# Add all the source files
set(SOURCES
    ../vectors.cpp
)


# Compile the library
add_library(\${lib_name} SHARED \${SOURCES} )

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
endif()" > CMakeLists.txt | grep -v "/Users/remycharles/Desktop/Github Desktop/2022-2023-project-3-harfang3d-binding-Project-1-group/TestFsBind/FSProject/vectors.fs(12,9): warning FS0046: The identifier 'process' is reserved for future use by F# [/Users/remycharles/Desktop/Github Desktop/2022-2023-project-3-harfang3d-binding-Project-1-group/TestFsBind/FSProject/FsharpBindings.fsproj]"
    cmake .
    cmake --build . --config Release
    
fi


